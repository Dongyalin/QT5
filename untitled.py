# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_zhengze = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_zhengze.setGeometry(QtCore.QRect(20, 230, 141, 22))
        self.comboBox_zhengze.setObjectName("comboBox_zhengze")
        self.pushButton_zhengze = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zhengze.setGeometry(QtCore.QRect(230, 230, 93, 28))
        self.pushButton_zhengze.setObjectName("pushButton_zhengze")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(470, 160, 211, 111))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_History = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_History.setGeometry(QtCore.QRect(460, 360, 221, 87))
        self.textEdit_History.setObjectName("textEdit_History")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 130, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 330, 72, 15))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 310, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_zhengze.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "此次结果"))
        self.label_2.setText(_translate("MainWindow", "历史记录"))

