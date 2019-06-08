#! /usr/bin/python3
# coding = utf-8

import sys
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal, QThread, QMutexLocker, QMutex
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication
import cv2
from ui.video_test import Ui_videoTest
from utils import normal_utils
import logging


class VideoForm(QtWidgets.QWidget, Ui_videoTest):
    """
    参数设置
    """
    def __init__(self):
        super(VideoForm, self).__init__()
        self.setupUi(self)
        # rtsp://184.72.239.149/vod/mp4://BigBuckBunny_175k.mov
        self.thread = VideoThread('rtsp://admin:qwer6961@192.168.31.64')
        # self.thread = VideoThread('rtsp://184.72.239.149/vod/mp4://BigBuckBunny_175k.mov')
        # 注册信号处理函数
        self.thread.breakSignal.connect(self.showCamer)
        # 启动线程
        self.thread.start()
        self.pushButton.clicked.connect(self.shot_change)
        self.thread.shortImage.connect(self.shot_info)

    def shot_info(self, flag):
        if flag:
            QtWidgets.QMessageBox.information(self, '本程序', "保存图片成功！")

    def shot_change(self):
        self.thread.shot_image()

    def showCamer(self, qpixmap):
        """
        读取摄像头
        :param qpixmap:
        :return:
        """
        self.label_1.setPixmap(qpixmap)
        # self.label_4.setPixmap(qpixmap)
        # self.label_2.setPixmap(qpixmap)

    def resizeEvent(self, a0):
        """
        窗口改变
        :return:
        """
        super(VideoForm, self).resizeEvent(a0)
        width = self.label_1.size().width()
        height = self.label_1.size().height()
        # self.thread.set_size(width, height)


class VideoThread(QThread):
    """
    读取摄像头
    """
    # 定义信号
    breakSignal = pyqtSignal(QPixmap)
    # 定义参数为str类型
    shortImage = pyqtSignal(str)

    def __init__(self, url):
        super().__init__()
        self.stoped = False
        self.url = url
        self.video_width = 360
        self.video_height = 270
        self.mutex = QMutex()
        self.shot_flag = False
        self.is_running = False
        self.read_retry = 0

    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False
        is_connect = normal_utils.is_connected(self.url)
        if is_connect:
            logging.info('camera can connect.')
        else:
            logging.error('camera connect failed.')
            return
        cap = cv2.VideoCapture(self.url)
        while cap.isOpened() and not self.stoped:
            self.is_running = True
            try:
                ret, frame = cap.read()
                # 读取失败，有可能连接断开或没有视频文件
                if not ret:
                    self.read_retry += 1
                    logging.error("carema read failed.")
                    if self.read_retry > 1:
                        self.read_retry = 0
                        cap.release()
                        time.sleep(0.5)
                        if normal_utils.is_connected(self.url):
                            cap.open(self.url)
                            logging.error("carema open again success.")
                        else:
                            logging.error("carema open again failed.")
                    continue
                frame_mini = cv2.resize(frame, (self.video_width, self.video_height))
                height, width, bytesPerComponent = frame_mini.shape
                bytesPerLine = bytesPerComponent * width
                # 变换彩色空间顺序
                cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame_mini)
                image = QImage(frame_mini.data, width, height, bytesPerLine, QImage.Format_RGB888)
                self.breakSignal.emit(QPixmap.fromImage(image))
                if self.shot_flag:
                    logging.info('camera shot image! saved in %s.' % self.path)
                    cv2.imwrite(self.path, frame)
                    self.shot_flag = False
                    self.shortImage.emit(self.path)
                # 50毫秒发送一次信号
                # time.sleep(0.03)
            except Exception as e:
                logging.error(e)
                time.sleep(0.5)
                continue
        self.breakSignal.emit( QPixmap(""))
        cap.release()
        self.is_running = False

    def set_size(self, width, height):
        """
        设置视频大小
        :param width:
        :param height:
        :return:
        """
        self.video_width = width
        self.video_height = height

    def shot_image(self, path):
        """
        截图操作
        :return:
        """
        self.shot_flag = True
        self.path =path

    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped= True

    def isStoped(self):
        with QMutexLocker(self.mutex):
            return self.stoped and not self.is_running


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = VideoForm()
    myshow.show()
    sys.exit(app.exec_())