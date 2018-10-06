# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ETH_Gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ETH(object):
    def setupUi(self, ETH):
        ETH.setObjectName("ETH")
        ETH.resize(636, 362)
        self.centralwidget = QtWidgets.QWidget(ETH)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 631, 331))
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(70, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 270, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 130, 72, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(160, 40, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(170, 80, 341, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(70, 50, 72, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 120, 361, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(170, 160, 341, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(70, 210, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 200, 361, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(170, 240, 341, 16))
        self.label_6.setObjectName("label_6")
        ETH.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ETH)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 26))
        self.menubar.setObjectName("menubar")
        ETH.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ETH)
        self.statusbar.setObjectName("statusbar")
        ETH.setStatusBar(self.statusbar)

        self.retranslateUi(ETH)
        QtCore.QMetaObject.connectSlotsByName(ETH)

    def retranslateUi(self, ETH):
        _translate = QtCore.QCoreApplication.translate
        ETH.setWindowTitle(_translate("ETH", "MainWindow"))
        self.groupBox.setTitle(_translate("ETH", "以太报文"))
        self.pushButton.setText(_translate("ETH", "确定"))
        self.pushButton_2.setText(_translate("ETH", "取消"))
        self.label.setText(_translate("ETH", "目的Mac："))
        self.label_2.setText(_translate("ETH", "格式：00-11-22-33-44-55"))
        self.label_3.setText(_translate("ETH", "源Mac："))
        self.label_4.setText(_translate("ETH", "格式：00-11-22-33-44-55"))
        self.label_5.setText(_translate("ETH", "3层报文："))
        self.label_6.setText(_translate("ETH", "类型代码（例如：IPv4-0800）"))

