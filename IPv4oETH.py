# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IPv4oETH.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IPv4oETH(object):
    def setupUi(self, IPv4oETH):
        IPv4oETH.setObjectName("IPv4oETH")
        IPv4oETH.resize(628, 508)
        self.groupBox = QtWidgets.QGroupBox(IPv4oETH)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 631, 511))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 130, 72, 21))
        self.label.setObjectName("label")
        self.lineEdit_ETH_SMAC = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ETH_SMAC.setGeometry(QtCore.QRect(170, 40, 361, 31))
        self.lineEdit_ETH_SMAC.setObjectName("lineEdit_ETH_SMAC")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 341, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_ETH_DMAC = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ETH_DMAC.setGeometry(QtCore.QRect(170, 120, 361, 31))
        self.lineEdit_ETH_DMAC.setObjectName("lineEdit_ETH_DMAC")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 50, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 160, 341, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(180, 240, 231, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(50, 200, 91, 41))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(180, 400, 341, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_IPv4_DIP = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_IPv4_DIP.setGeometry(QtCore.QRect(170, 280, 361, 31))
        self.lineEdit_IPv4_DIP.setObjectName("lineEdit_IPv4_DIP")
        self.lineEdit_IPv4_L4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_IPv4_L4.setGeometry(QtCore.QRect(170, 360, 361, 31))
        self.lineEdit_IPv4_L4.setObjectName("lineEdit_IPv4_L4")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(50, 290, 101, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_IPv4_SIP = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_IPv4_SIP.setGeometry(QtCore.QRect(170, 200, 361, 31))
        self.lineEdit_IPv4_SIP.setObjectName("lineEdit_IPv4_SIP")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(50, 360, 111, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(180, 320, 231, 16))
        self.label_10.setObjectName("label_10")
        self.pushButton_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ok.setGeometry(QtCore.QRect(80, 460, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cancel.setGeometry(QtCore.QRect(440, 460, 93, 28))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(IPv4oETH)
        QtCore.QMetaObject.connectSlotsByName(IPv4oETH)

    def retranslateUi(self, IPv4oETH):
        _translate = QtCore.QCoreApplication.translate
        IPv4oETH.setWindowTitle(_translate("IPv4oETH", "Dialog"))
        self.groupBox.setTitle(_translate("IPv4oETH", "IPv4OnETH"))
        self.label.setText(_translate("IPv4oETH", "目的Mac："))
        self.label_2.setText(_translate("IPv4oETH", "格式：00-11-22-33-44-55"))
        self.label_3.setText(_translate("IPv4oETH", "源Mac："))
        self.label_4.setText(_translate("IPv4oETH", "格式：00-11-22-33-44-55"))
        self.label_5.setText(_translate("IPv4oETH", "格式：168.192.1.1"))
        self.label_6.setText(_translate("IPv4oETH", "IPv4-源IP:"))
        self.label_7.setText(_translate("IPv4oETH", "类型代码（例如：IPv4-0800）"))
        self.label_8.setText(_translate("IPv4oETH", "IPv4-目的IP:"))
        self.label_9.setText(_translate("IPv4oETH", "IPv4-4层报文:"))
        self.label_10.setText(_translate("IPv4oETH", "格式：168.192.1.1"))
        self.pushButton_ok.setText(_translate("IPv4oETH", "确定"))
        self.pushButton_cancel.setText(_translate("IPv4oETH", "取消"))

