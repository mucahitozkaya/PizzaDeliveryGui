import sys
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
        

    def klasik(self):
        if self.klasik_pizza.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+80))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-80))

    def turk(self):
        if self.turk_pizza.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+80))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-80))

    def margarita(self):
        if self.margarita_pizza.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+70))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-70))

    def sade(self):
        if self.sade_pizza.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+70))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-70))

    def zeytin_fiyat(self):
        if self.zeytin.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))

    def mantar_fiyat(self):
        if self.mantar.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))

    def keci_peynir_fiyat(self):
        if self.keci_peynir.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))

    def et_fiyat(self):
        if self.et.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+20))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-20))

    def sogan_fiyat(self):
        if self.sogan.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))

    def misir_fiyat(self):
        if self.misir.isChecked():
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())+10))
        else:
            self.toplam_fiyat.setText(str(int(self.toplam_fiyat.text())-10))

    def get_description(self):

        name = self.ad_soyad.text()
        kart_id = self.kart_no.text()
        kart_password = self.kart_parola.text()
        
        export = open("Orders_Databases.csv","a")
        export.write(f"{name},{kart_id},{kart_password}")
        export.write("\n")
        export.close()        

        self.result_label.setText("Siparişiniz Başarıyla Alındı.")

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_())