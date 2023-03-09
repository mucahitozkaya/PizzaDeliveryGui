import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget
from PyQt5 import uic

class Pencere(QMainWindow):
    def __init__(self):
        super(Pencere, self).__init__()                                                    
        uic.loadUi('pizza.ui', self) 

        self.klasik_pizza.stateChanged.connect(self.klasik)
        self.turk_pizza.stateChanged.connect(self.turk)
        self.margarita_pizza.stateChanged.connect(self.margarita)
        self.sade_pizza.stateChanged.connect(self.sade)
        self.zeytin.stateChanged.connect(self.zeytin_fiyat)
        self.mantar.stateChanged.connect(self.mantar_fiyat)
        self.keci_peynir.stateChanged.connect(self.keci_peynir_fiyat)
        self.et.stateChanged.connect(self.et_fiyat)
        self.sogan.stateChanged.connect(self.sogan_fiyat)
        self.misir.stateChanged.connect(self.misir_fiyat)
        self.toolButton.clicked.connect(self.get_description)
        self.klasik_pizza_desc = ""
        self.turk_pizza_desc = ""
        self.sade_pizza_desc = ""
        self.margarita_pizza_desc = ""
        self.mantar_desc = ""
        self.zeytin_desc = ""
        self.keci_peynir_desc = ""
        self.et_desc = ""
        self.sogan_desc = ""
        self.misir_desc = ""
        

    def klasik(self):
        if self.klasik_pizza.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+80))
            self.klasik_pizza_desc = "Klasik Pizza"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-80))
            self.klasik_pizza_desc = ""

    def turk(self):
        if self.turk_pizza.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+80))
            self.turk_pizza_desc = "Türk Pizza"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-80))
            self.turk_pizza_desc = ""

    def margarita(self):
        if self.margarita_pizza.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+70))
            self.margarita_pizza_desc = "Margarita Pizza"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-70))
            self.margarita_pizza_desc = ""

    def sade(self):
        if self.sade_pizza.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+70))
            self.sade_pizza_desc = "Sade Pizza"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-70))
            self.sade_pizza_desc = ""

    def zeytin_fiyat(self):
        if self.zeytin.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
            self.zeytin_desc = "Zeytin"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))
            self.zeytin_desc = ""

    def mantar_fiyat(self):
        if self.mantar.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
            self.mantar_desc = "Mantar"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))
            self.mantar_desc = ""

    def keci_peynir_fiyat(self):
        if self.keci_peynir.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
            self.keci_peynir_desc = "Keçi Peyniri"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))
            self.keci_peynir_desc = ""

    def et_fiyat(self):
        if self.et.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+20))
            self.et_desc = "Et"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-20))
            self.et_desc = ""

    def sogan_fiyat(self):
        if self.sogan.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
            self.sogan_desc = "Soğan"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))
            self.sogan_desc = ""

    def misir_fiyat(self):
        if self.misir.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
            self.misir_desc = "Mısır"
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))
            self.misir_desc = ""

    def get_description(self):

        name = self.ad_soyad.text()
        kart_id = self.kart_no.text()
        kart_password = self.kart_parola.text()
        now = datetime.now()


        export = open("Orders_Databases.csv","a")
        export.write(f"{name},{kart_id},{kart_password},{self.klasik_pizza_desc},{self.turk_pizza_desc},{self.sade_pizza_desc},{self.margarita_pizza_desc},{self.zeytin_desc},{self.mantar_desc},{self.et_desc},{self.keci_peynir_desc},{self.misir_desc},{self.sogan_desc},{now}")
        export.write("\n")
        export.close()        

        self.result_label.setText("Siparişiniz Başarıyla Alındı.")

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())