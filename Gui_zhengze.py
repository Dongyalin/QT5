#! python3

from PyQt5 import QtCore, QtGui, uic, QtWidgets
import zhengzelist
import ETH_GUI_1
import IPv4_GUI
import selfDeF_GUI
import IPv4oETH

import combre
import sys
import re

dictClassZhengZe={}

#设置自定义带匹配的报文段
class showSelfDeF(selfDeF_GUI.Ui_selfDefine ,QtWidgets.QDialog, combre.rebase):

    def __init__(self):
        super(showSelfDeF, self).__init__()
        self.setupUi(self)
        self.pushButton_ok.clicked.connect(self.click_ok)
        self.pushButton_cancel.clicked.connect(self.click_cancel)

    def click_ok(self):
        self.constructionRe(self.lineEdit_PKT.text())
        zhengzelist.ReClass.constructionRe(self.reStr)
        self.close()

    def click_cancel(self):
        self.close()

dictClassZhengZe["自定义"] = showSelfDeF



#设置带匹配的以太报文格式
class showETH(ETH_GUI_1.Ui_ETH ,QtWidgets.QDialog, combre.Eth):
    def __init__(self):
        #QtWidgets.QMainWindow.__init__(self)
        super(showETH, self).__init__()
        #ETH_Gui.Ui_ETH.__init__(self)

        self.setupUi(self)
        self.pushButton_ok.clicked.connect(self.click_ok)
        self.pushButton_cancel.clicked.connect(self.click_cancel)

    def click_ok(self):

        SMac = self.__Mactpye(self.lineEdit_ETH_SMAC.text())
        zhengzelist.dictZhengZepara["SMAC"] = SMac
        self.setSmac(SMac)

        DMac = self.__Mactpye(self.lineEdit_ETH_DMAC.text())
        zhengzelist.dictZhengZepara["DMAC"] = DMac
        self.setDmac(DMac)

        if(self.__isETH_NType(self.lineEdit_ETH_L3.text())):
            tmp =  self.lineEdit_ETH_L3.text()
            zhengzelist.dictZhengZepara["ETH_L3"] = tmp
            self.setEthNeType(tmp)
        self.combationETH()
        zhengzelist.ReClass.constructionRe(self.reStr)
        self.close()

    def click_cancel(self):
        self.close()

    #将mac地址从00-11-22-33-44-55转换为001122334455
    def __Mactpye(self, macstr):
        tmplist = []
        macstr1 = macstr.strip(" ")
        tmplist = macstr1.split("-")
        tmpsrc = ''
        isHex = re.compile(r"^[0-9a-fA-F]{2}$")
        for item in tmplist:
            if (isHex.search(item) != None):
                tmpsrc = tmpsrc + item

        return tmpsrc

    def __isETH_NType(self, type):
        type1 = type.strip(" ")
        isETHT = re.compile(r"^[0-9a-fA-F]{4}$")
        if(isETHT.search(type1) != None):
            return True
        return False

dictClassZhengZe["ETH"] = showETH

#设置带匹配的IPv4报文格式
class showIPv4(IPv4_GUI.Ui_IPv4 ,QtWidgets.QDialog, combre.IP4):
    def __init__(self):
        super(showIPv4, self).__init__()
        self.setupUi(self)
        self.pushButton_ok.clicked.connect(self.click_ok)
        self.pushButton_cancel.clicked.connect(self.click_cancel)

    def click_ok(self):


        DIP = self.__IPtohex(self.lineEdit_IPv4_DIP.text())
        zhengzelist.dictZhengZepara["DIPv4"] = DIP
        self.setDIP(DIP)


        SIP = self.__IPtohex(self.lineEdit_IPv4_SIP.text())
        zhengzelist.dictZhengZepara["SIPv4"] = SIP
        self.setSIP(SIP)

        if self.__isNType(self.lineEdit_IPv4_L4.text()):
            tmp = self.lineEdit_IPv4_L4.text()
            zhengzelist.dictZhengZepara["IPv4_L4"] = tmp
            self.setProtocol(tmp)
        self.combationIP4()
        zhengzelist.ReClass.constructionRe(self.reStr)
        self.close()

    def click_cancel(self):
        self.close()

    def __IPtohex(self, strIP):
        strIP = strIP.strip(" ")
        tmplist = strIP.split(".")
        returnstr = ''
        for item in tmplist:
            if item.isdecimal():
                tmpint = int(item)
                tmphex = hex(tmpint)
                tmpstr = str(tmphex)
                tmpstr = tmpstr.lstrip("0x")
                tmpstr = tmpstr.rjust(2, "0")
                returnstr = returnstr + tmpstr

        return returnstr

    def __isNType(self, type):
        type1 = type.strip(" ")
        isETHT = re.compile(r"^[0-9a-fA-F]{4}$")
        if(isETHT.search(type1) != None):
            return True
        return False


dictClassZhengZe["IPv4"] = showIPv4


#设置带匹配的IPv4onETH报文格式
class showIPv4oETH(IPv4oETH.Ui_IPv4oETH ,QtWidgets.QDialog, combre.IP4oETH):
    def __init__(self):
        super(showIPv4oETH, self).__init__()
        self.setupUi(self)
        self.pushButton_ok.clicked.connect(self.click_ok)
        self.pushButton_cancel.clicked.connect(self.click_cancel)

    def click_ok(self):
        SMac = self.__Mactpye(self.lineEdit_ETH_SMAC.text())
        zhengzelist.dictZhengZepara["SMAC"] = SMac
        self.setSmac(SMac)

        DMac = self.__Mactpye(self.lineEdit_ETH_DMAC.text())
        zhengzelist.dictZhengZepara["DMAC"] = DMac
        self.setDmac(DMac)

        #if(self.__isETH_NType(self.lineEdit_ETH_L3.text())):
           # zhengzelist.dictZhengZepara["ETH_L3"] = self.lineEdit_ETH_L3.text()


        DIP = self.__IPtohex(self.lineEdit_IPv4_DIP.text())
        zhengzelist.dictZhengZepara["DIPv4"] = DIP
        self.setDIP(DIP)


        SIP = self.__IPtohex(self.lineEdit_IPv4_SIP.text())
        zhengzelist.dictZhengZepara["SIPv4"] = SIP
        self.setSIP(SIP)

        if self.__isNType(self.lineEdit_IPv4_L4.text()):
            tmp = self.lineEdit_IPv4_L4.text()
            zhengzelist.dictZhengZepara["IPv4_L4"] = tmp
            self.setProtocol(tmp)

        self.combationIP4oEth()
        zhengzelist.ReClass.constructionRe(self.reStr)
        self.close()

    def click_cancel(self):
        self.close()

    def __Mactpye(self, macstr):
        tmplist = []
        macstr1 = macstr.strip(" ")
        tmplist = macstr1.split("-")
        tmpsrc = ''
        isHex = re.compile(r"^[0-9a-fA-F]{2}$")
        for item in tmplist:
            if (isHex.search(item) != None):
                tmpsrc = tmpsrc + item

        return tmpsrc

    def __IPtohex(self, strIP):
        strIP = strIP.strip(" ")
        tmplist = strIP.split(".")
        returnstr = ''
        for item in tmplist:
            if item.isdecimal():
                tmpint = int(item)
                tmphex = hex(tmpint)
                tmpstr = str(tmphex)
                tmpstr = tmpstr.lstrip("0x")
                tmpstr = tmpstr.rjust(2, "0")
                returnstr = returnstr + tmpstr

        return returnstr

    def __isNType(self, type):
        type1 = type.strip(" ")
        isETHT = re.compile(r"^[0-9a-fA-F]{4}$")
        if(isETHT.search(type1) != None):
            return True
        return False

dictClassZhengZe["IPv4onETH"] = showIPv4oETH

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = dictClassZhengZe["ETH"]()
    window.show()

