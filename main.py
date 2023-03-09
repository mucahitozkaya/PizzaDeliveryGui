import logging,os,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from threading import Thread
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import csv,datetime
from pizza import *

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

from PyQt5.uic import loadUiType
ui,_ = loadUiType(resource_path('pizza.ui')) 


# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

class QTextEditLogger(logging.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = parent.log
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.insertPlainText(msg)


class MainApp(QMainWindow , ui):
    def __init__(self , parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUi()
        self.HandleButtons()

    def InitUi(self):

        #Logging setupp
        logTextBox = QTextEditLogger(self)
        logTextBox.setFormatter(logging.Formatter('%(message)s\n')) # logger format
        logging.getLogger().addHandler(logTextBox)
        # You can control the logging level
        logging.getLogger().setLevel(logging.DEBUG)

        self.orderListDesc = {"pizza":"","sos":[]}
        self.orderList = {"pizza":"","sos":[]}
        self.totalPrice = 0

        self.pizzaDict = {
            1:KlasikPizza(80,"Klasik Pizza"),
            2:TurkPizza(80,"Türk Pizza"),
            3:MargheritaPizza(70,"Margarita Pizza"),
            4:DominosPizza(70,"Sade Pizza"),
            5:Zeytin(10,"Zeytin"),
            6:Mantar(10,"Mantar"),
            7:KeciPeyniri(10,"Keçi Peyniri"),
            8:Et(20,"Et"),
            9:Sogan(10,"Soğan"),
            10:Misir(10,"Mısır"),
        }

    def HandleButtons(self):
        self.klasik_pizza.clicked.connect(lambda x: self.onChange(1))
        self.turk_pizza.clicked.connect(lambda x: self.onChange(2))
        self.margarita_pizza.clicked.connect(lambda x: self.onChange(3))
        self.sade_pizza.clicked.connect(lambda x: self.onChange(4))
        self.zeytin.stateChanged.connect(lambda x: self.onChange(5))
        self.mantar.stateChanged.connect(lambda x: self.onChange(6))
        self.keci_peynir.stateChanged.connect(lambda x: self.onChange(7))
        self.et.stateChanged.connect(lambda x: self.onChange(8))
        self.sogan.stateChanged.connect(lambda x: self.onChange(9))
        self.misir.stateChanged.connect(lambda x: self.onChange(10))

        self.toolButton.clicked.connect(lambda x: self.write_csv())

    
    def onChange(self,sender):
        self.totalPrice = 0
        if sender in (1,2,3,4):
            self.orderList["pizza"] = self.pizzaDict[sender]
            self.orderListDesc["pizza"] = self.pizzaDict[sender].get_description()
        else:
            if self.pizzaDict[sender] in self.orderList["sos"]:
                self.orderList["sos"].remove(self.pizzaDict[sender])
                self.orderListDesc["sos"].remove(self.pizzaDict[sender].get_description())
            else:
                self.orderList["sos"].append(self.pizzaDict[sender])
                self.orderListDesc["sos"].append(self.pizzaDict[sender].get_description())
            
        
        for i in self.orderList["sos"]:
            self.totalPrice += i.get_cost()
        self.totalPrice += self.orderList["pizza"].get_cost()
        self.toplam_fiyat.setText(str(self.totalPrice))

        logging.info(self.pizzaDict[sender].get_description())
    
    def write_csv(self):

        name = self.ad_soyad.text()
        kart_id = self.kart_no.text()
        kart_password = self.kart_parola.text()
        tc_no = self.tcno.text()

        orders = (f"{name},{tc_no},{kart_id},{kart_password},{self.orderListDesc},{datetime.datetime.now()}")

        orderFile = open("Orders_Database.csv","a")
        orderFile.write(orders)
        orderFile.close()  

        self.result_label.setText("Siparişiniz Başarıyla Alındı.")

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()

