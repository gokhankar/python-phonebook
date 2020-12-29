import sys
import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTableWidgetItem
from _main_window import Ui_MainWindow
from form_add_new import FormAdd
from form_del import FormDel


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_people()
        self.load_details()
        self.ui.btn_add_new.clicked.connect(self.open_form_add_new)
        self.ui.btn_del.clicked.connect(self.open_form_del)
        self.form_add_new = FormAdd()
        self.form_del = FormDel()

    def load_people(self):
        connection = sqlite3.connect("people.db")
        cursor = connection.cursor()
        cursor.execute("select isim, soyisim, telefon, e_posta, dogum_tarihi from people")
        data = cursor.fetchall()
        connection.close()
        print(data)
        self.ui.tableWidget_show.setRowCount(len(data))
        self.ui.tableWidget_show.setColumnCount(3)
        self.ui.tableWidget_show.setColumnWidth(0, 120)
        self.ui.tableWidget_show.setColumnWidth(1, 120)
        self.ui.tableWidget_show.setColumnWidth(2, 90)

        """self.ui.tableWidget_show.setStyleSheet("background-color:#f7f7f7;\n"
                                            "color: #8e8e8e;\n"
                                            "padding-top:3px;\n"
                                            "padding-left: 10px;\n"
                                            "")"""


        data = sorted(data, key=lambda item: item[0].lower())
        rowIndex = 0
        dataIndex = 0
        for person in data:
            self.ui.tableWidget_show.setItem(rowIndex, 0, QTableWidgetItem(data[dataIndex][0]))
            self.ui.tableWidget_show.setItem(rowIndex, 1, QTableWidgetItem(data[dataIndex][1]))
            self.ui.tableWidget_show.setItem(rowIndex, 2, QTableWidgetItem(str(data[dataIndex][2])))
            rowIndex += 1
            dataIndex += 1

    def load_details(self):
        connection = sqlite3.connect("people.db")
        cursor = connection.cursor()
        cursor.execute("select isim, soyisim, telefon, e_posta, dogum_tarihi from people")
        data = cursor.fetchall()
        connection.close()
        print(data)
        """self.ui.listView_details.row
        self.ui.listView_details.setRowCount(5)
        self.ui.listView_details.setColumnCount(2)
        self.ui.listView_details.setColumnWidth(0, 100)
        self.ui.listView_details.setColumnWidth(1, 100)"""
        pass



    def open_form_add_new(self):
        self.form_add_new.show()


    def open_form_del(self):
        self.form_del.show()
