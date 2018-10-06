# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selfDeF_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_selfDefine(object):
    def setupUi(self, selfDefine):
        selfDefine.setObjectName("selfDefine")
        selfDefine.resize(622, 378)
        self.groupBox = QtWidgets.QGroupBox(selfDefine)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 621, 381))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ok.setGeometry(QtCore.QRect(50, 290, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cancel.setGeometry(QtCore.QRect(410, 290, 93, 28))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.lineEdit_PKT = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_PKT.setGeometry(QtCore.QRect(60, 160, 421, 21))
        self.lineEdit_PKT.setObjectName("lineEdit_PKT")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 120, 231, 16))
        self.label.setObjectName("label")

        self.retranslateUi(selfDefine)
        QtCore.QMetaObject.connectSlotsByName(selfDefine)

    def retranslateUi(self, selfDefine):
        _translate = QtCore.QCoreApplication.translate
        selfDefine.setWindowTitle(_translate("selfDefine", "Dialog"))
        self.groupBox.setTitle(_translate("selfDefine", "自定义"))
        self.pushButton_ok.setText(_translate("selfDefine", "确定"))
        self.pushButton_cancel.setText(_translate("selfDefine", "取消"))
        self.label.setText(_translate("selfDefine", "输入带匹配的报文段："))

