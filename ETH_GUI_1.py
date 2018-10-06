# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ETH_GUI_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ETH(object):
    def setupUi(self, ETH):
        ETH.setObjectName("ETH")
        ETH.resize(628, 333)
        self.groupBox = QtWidgets.QGroupBox(ETH)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 631, 331))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_ok = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_ok.setGeometry(QtCore.QRect(70, 280, 93, 28))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancel = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_cancel.setGeometry(QtCore.QRect(430, 280, 93, 28))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 130, 72, 21))
        self.label.setObjectName("label")
        self.lineEdit_ETH_SMAC = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ETH_SMAC.setGeometry(QtCore.QRect(160, 40, 361, 31))
        self.lineEdit_ETH_SMAC.setObjectName("lineEdit_ETH_SMAC")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(170, 80, 341, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 50, 72, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_ETH_DMAC = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ETH_DMAC.setGeometry(QtCore.QRect(160, 120, 361, 31))
        self.lineEdit_ETH_DMAC.setObjectName("lineEdit_ETH_DMAC")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(170, 160, 341, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(70, 210, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_ETH_L3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ETH_L3.setGeometry(QtCore.QRect(160, 200, 361, 31))
        self.lineEdit_ETH_L3.setObjectName("lineEdit_ETH_L3")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(170, 240, 341, 16))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(ETH)
        QtCore.QMetaObject.connectSlotsByName(ETH)

    def retranslateUi(self, ETH):
        _translate = QtCore.QCoreApplication.translate
        ETH.setWindowTitle(_translate("ETH", "Dialog"))
        self.groupBox.setTitle(_translate("ETH", "以太报文"))
        self.pushButton_ok.setText(_translate("ETH", "确定"))
        self.pushButton_cancel.setText(_translate("ETH", "取消"))
        self.label.setText(_translate("ETH", "目的Mac："))
        self.label_2.setText(_translate("ETH", "格式：00-11-22-33-44-55"))
        self.label_3.setText(_translate("ETH", "源Mac："))
        self.label_4.setText(_translate("ETH", "格式：00-11-22-33-44-55"))
        self.label_5.setText(_translate("ETH", "3层报文："))
        self.label_6.setText(_translate("ETH", "类型代码（例如：IPv4-0800）"))

