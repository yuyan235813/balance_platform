#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Time    : 2018/8/17 下午9:54
@Author  : lizhiran
@Email   : 794339312@qq.com
"""
from PyQt5 import QtWidgets
from ui.system_params_setup import Ui_systemParamsSetupForm
from PyQt5.QtCore import *
from utils.sqllite_util import EasySqlite


class SystemParamsForm(QtWidgets.QWidget, Ui_systemParamsSetupForm):
    """
    参数设置
    """
    def __init__(self):
        super(SystemParamsForm, self).__init__()
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.db = EasySqlite(r'rmf/db/balance.db')
        self.cancelPushButton.clicked.connect(self.close)
        self.savePushButton.clicked.connect(self.save)

    def show(self):
        """
        显示ui
        :return:
        """
        super(SystemParamsForm, self).show()
        query_sql = "select * from t_system_params_conf where id = 1;"
        ret = self.db.query(query_sql)
        if not ret:
            return
        params = ret[0]
        self.comboBox.setCurrentText(params.get('unit', '吨'))
        self.companyLineEdit.setText(params.get('company', ''))
        if params.get('auto_save', 0):
            self.checkBox.setChecked(True)
        self.priceDoubleSpinBox.setValue(params.get('price', 0.0))
        self.roundComboBox.setCurrentText(params.get('precision', '元'))

    def save(self):
        """
        保存设置
        :return:
        """
        unit = self.comboBox.currentText()
        company = self.companyLineEdit.text()
        auto_save = 1 if self.checkBox.isChecked() else 0
        price = float(self.priceDoubleSpinBox.text())
        precision = self.roundComboBox.currentText()
        update_sql = 'replace into t_system_params_conf(id,unit, company, auto_save, price, `precision`)' \
                     ' values(1, ?, ?, ?, ?, ?)'
        ret = self.db.update(update_sql, [unit, company, auto_save, price, precision])
        if ret:
            QtWidgets.QMessageBox.warning(self, u'本程序', u'保存失败:\n', QtWidgets.QMessageBox.Ok)
        else:
            QtWidgets.QMessageBox.information(self, u'本程序', u'保存成功!', QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = SystemParamsForm()
    myshow.show()
    sys.exit(app.exec_())