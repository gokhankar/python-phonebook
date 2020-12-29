import sqlite3
from PyQt5.QtWidgets import *
from _form_add_new import Ui_form_add_new


class FormAdd(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_add_new()
        self.ui.setupUi(self)
        self.ui.btn_kisiyi_ekle.clicked.connect(self.kisiyi_db_ekle)

    def kisiyi_db_ekle(self):
        name = self.ui.lineEdit_isim_ekle.text()
        surname = self.ui.lineEdit_soyisim_ekle.text()
        tel_number = self.ui.lineEdit_tel_ekle.text()
        email = self.ui.lineEdit_eposta_ekle.text()
        birthday = self.ui.lineEdit_tarih_ekle.text()
        print(name, surname, email, birthday, tel_number)

        connection = sqlite3.connect("people.db")
        print("Bağlandı")
        cursor = connection.cursor()

        sql = """INSERT INTO people (isim, soyisim, telefon, e_posta, dogum_tarihi) VALUES(?,?,?,?,?)"""
        values = (name, surname, tel_number, email, birthday)
        cursor.execute(sql, values)

        connection.commit()
        connection.close()
        print("Bağlantı sonlandı")
