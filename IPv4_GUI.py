# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IPv4_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IPv4(object):
    def setupUi(self, IPv4):
        IPv4.setObjectName("IPv4")
        IPv4.resize(617, 340)
        self.groupBox = QtWidgets.QGroupBox(IPv4)
        self.groupBox.setGeometry(QtCore.QRect(-10, 0, 631, 341))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 50, 91, 21))
        self.label.setObjectName("label")
        self.lineEdit_IPv4_SIP = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_IPv4_SIP.setGeometry(QtCore.QRect(170, 40, 311, 31))
        self.lineEdit_IPv4_SIP.setObjectName("lineEdit_IPv4_SIP")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 101, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_IPv4_DIP = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_IPv4_DIP.setGeometry(QtCore.QRect(170, 120, 311, 31))
        self.lineEdit_IPv4_DIP.setObjectName("lineEdit_IPv4_DIP")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 200, 111, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_IPv4_L4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_IPv4_L4.setGeometry(QtCore.QRect(170, 200, 311, 31))
        self.lineEdit_IPv4_L4.setObjectName("lineEdit_IPv4_L4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 80, 231, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(180, 160, 231, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(180, 240, 341, 16))
        self.label_6.setObjectName("label_6")
        self.pushButton_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ok.setGeometry(QtCore.QRect(60, 280, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cancel.setGeometry(QtCore.QRect(430, 280, 93, 28))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(IPv4)
        QtCore.QMetaObject.connectSlotsByName(IPv4)

    def retranslateUi(self, IPv4):
        _translate = QtCore.QCoreApplication.translate
        IPv4.setWindowTitle(_translate("IPv4", "Dialog"))
        self.groupBox.setTitle(_translate("IPv4", "IPv4"))
        self.label.setText(_translate("IPv4", "IPv4-源IP:"))
        self.label_2.setText(_translate("IPv4", "IPv4-目的IP:"))
        self.label_3.setText(_translate("IPv4", "IPv4-4层报文:"))
        self.label_4.setText(_translate("IPv4", "格式：168.192.1.1"))
        self.label_5.setText(_translate("IPv4", "格式：168.192.1.1"))
        self.label_6.setText(_translate("IPv4", "类型代码（例如：IPv4-0800）"))
        self.pushButton_ok.setText(_translate("IPv4", "确定"))
        self.pushButton_cancel.setText(_translate("IPv4", "取消"))

