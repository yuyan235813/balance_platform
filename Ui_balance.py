# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\workspace\python3\balance_platform\balance.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(mainWindow)
        self.centralWidget.setObjectName("centralWidget")
        mainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menuBar.setObjectName("menuBar")
        self.qmenuSystemSetup = QtWidgets.QMenu(self.menuBar)
        self.qmenuSystemSetup.setObjectName("qmenuSystemSetup")
        self.qmenuBasicInfoSetup = QtWidgets.QMenu(self.menuBar)
        self.qmenuBasicInfoSetup.setObjectName("qmenuBasicInfoSetup")
        self.qmenuQuery = QtWidgets.QMenu(self.menuBar)
        self.qmenuQuery.setObjectName("qmenuQuery")
        self.qmenuHelp = QtWidgets.QMenu(self.menuBar)
        self.qmenuHelp.setObjectName("qmenuHelp")
        mainWindow.setMenuBar(self.menuBar)
        self.actionBalanceFormSetup = QtWidgets.QAction(mainWindow)
        self.actionBalanceFormSetup.setObjectName("actionBalanceFormSetup")
        self.actionParameterSetup = QtWidgets.QAction(mainWindow)
        self.actionParameterSetup.setObjectName("actionParameterSetup")
        self.actionUserPermission = QtWidgets.QAction(mainWindow)
        self.actionUserPermission.setObjectName("actionUserPermission")
        self.actionSystemParameterSetup = QtWidgets.QAction(mainWindow)
        self.actionSystemParameterSetup.setObjectName("actionSystemParameterSetup")
        self.actionCarInfo = QtWidgets.QAction(mainWindow)
        self.actionCarInfo.setObjectName("actionCarInfo")
        self.actionSupplier = QtWidgets.QAction(mainWindow)
        self.actionSupplier.setObjectName("actionSupplier")
        self.actionReceiving = QtWidgets.QAction(mainWindow)
        self.actionReceiving.setObjectName("actionReceiving")
        self.actionGoodsName = QtWidgets.QAction(mainWindow)
        self.actionGoodsName.setObjectName("actionGoodsName")
        self.actionBalanceQuery = QtWidgets.QAction(mainWindow)
        self.actionBalanceQuery.setObjectName("actionBalanceQuery")
        self.actionHelp = QtWidgets.QAction(mainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.qmenuSystemSetup.addAction(self.actionBalanceFormSetup)
        self.qmenuSystemSetup.addAction(self.actionParameterSetup)
        self.qmenuSystemSetup.addAction(self.actionUserPermission)
        self.qmenuSystemSetup.addAction(self.actionSystemParameterSetup)
        self.qmenuBasicInfoSetup.addAction(self.actionCarInfo)
        self.qmenuBasicInfoSetup.addAction(self.actionSupplier)
        self.qmenuBasicInfoSetup.addAction(self.actionReceiving)
        self.qmenuBasicInfoSetup.addAction(self.actionGoodsName)
        self.qmenuQuery.addAction(self.actionBalanceQuery)
        self.qmenuHelp.addAction(self.actionHelp)
        self.qmenuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.qmenuSystemSetup.menuAction())
        self.menuBar.addAction(self.qmenuBasicInfoSetup.menuAction())
        self.menuBar.addAction(self.qmenuQuery.menuAction())
        self.menuBar.addAction(self.qmenuHelp.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "牛逼的称重系统"))
        self.qmenuSystemSetup.setTitle(_translate("mainWindow", "系统设置"))
        self.qmenuBasicInfoSetup.setTitle(_translate("mainWindow", "基本信息设置"))
        self.qmenuQuery.setTitle(_translate("mainWindow", "查询"))
        self.qmenuHelp.setTitle(_translate("mainWindow", "帮助"))
        self.actionBalanceFormSetup.setText(_translate("mainWindow", "磅单设置"))
        self.actionParameterSetup.setText(_translate("mainWindow", "参数设置"))
        self.actionUserPermission.setText(_translate("mainWindow", "用户和权限管理"))
        self.actionSystemParameterSetup.setText(_translate("mainWindow", "系统参数设置"))
        self.actionCarInfo.setText(_translate("mainWindow", "车辆设置"))
        self.actionSupplier.setText(_translate("mainWindow", "供货单位"))
        self.actionReceiving.setText(_translate("mainWindow", "收获单位"))
        self.actionGoodsName.setText(_translate("mainWindow", "货物名称"))
        self.actionBalanceQuery.setText(_translate("mainWindow", "程中查询"))
        self.actionHelp.setText(_translate("mainWindow", "帮助信息"))
        self.actionAbout.setText(_translate("mainWindow", "关于"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

