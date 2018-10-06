
from PyQt5 import QtCore, QtGui, uic, QtWidgets

from untitled import *
import Gui_zhengze
import zhengzelist
import sys

#dictzhengze = ["自定义", "ETH", "IPv4", "IPv4oETH"]

class Myapp(QtWidgets.QMainWindow, Ui_MainWindow ):
    def __init__(self):
        #QtWidgets.QMainWindow.__init__(self)
        #Ui_MainWindow.__init__(self)
        super(Myapp, self).__init__()

        self.setupUi(self)
        for item_zhengze in  Gui_zhengze.dictClassZhengZe.keys():
            self.comboBox_zhengze.addItem(item_zhengze)

        self.pushButton_zhengze.clicked.connect(self.zhengze_OK)

        #self.textBrowser_zhengze.setText(self.comboBox_zhengze.currentText())

    def zhengze_OK(self):

        zhengzeclass = Gui_zhengze.dictClassZhengZe[self.comboBox_zhengze.currentText()]()
        zhengzeclass.show()
        zhengzeclass.exec_()

        print(zhengzelist.dictZhengZepara)
        print(zhengzelist.ReClass.getreStr())

    def __del__(self):
        print("123456")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    window.textBrowser.append("123456")#追加显示
    window.textBrowser.append("456789")
    window.textBrowser.append("zxcvb")
    app.exec_()
    sys.exit()