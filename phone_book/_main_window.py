# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 618)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("family-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:#C0C0C0;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView_details = QtWidgets.QListView(self.centralwidget)
        self.listView_details.setGeometry(QtCore.QRect(10, 250, 341, 311))
        self.listView_details.setStyleSheet("background-color::#d4d4d4;\n"
"color: #8e8e8e;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"")
        self.listView_details.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.listView_details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.listView_details.setObjectName("listView_details")
        self.btn_details = QtWidgets.QLabel(self.centralwidget)
        self.btn_details.setGeometry(QtCore.QRect(10, 230, 141, 16))
        self.btn_details.setObjectName("btn_details")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 180, 341, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("background-color:#f7f7f7;\n"
"color: #363636;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.btn_search = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_search.sizePolicy().hasHeightForWidth())
        self.btn_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(-1)
        self.btn_search.setFont(font)
        self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_search.setStyleSheet("background-color: #4e4e4e;\n"
"color: #fafafa;\n"
"font-size:15px;\n"
"border:1px solid #4e4e4e;\n"
"box-shadow: 2px 2px 6px #000;\n"
"border-bottom-right-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"hover:: background-color: #4CAF50;\n"
"\n"
"\n"
"")
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout_2.addWidget(self.btn_search)
        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 5)
        self.tableWidget_show = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_show.setGeometry(QtCore.QRect(360, 90, 391, 471))
        self.tableWidget_show.setStyleSheet("background-color:#d4d4d4;\n"
"color: #545454;\n"
"padding-top:5px;\n"
"padding-left: 20px;")
        self.tableWidget_show.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.tableWidget_show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableWidget_show.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_show.setAlternatingRowColors(True)
        self.tableWidget_show.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_show.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_show.setGridStyle(QtCore.Qt.NoPen)
        self.tableWidget_show.setObjectName("tableWidget_show")
        self.tableWidget_show.setColumnCount(0)
        self.tableWidget_show.setRowCount(0)
        self.tableWidget_show.horizontalHeader().setVisible(False)
        self.tableWidget_show.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget_show.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_show.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 181, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("customers-512.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setEnabled(True)
        self.btn_exit.setGeometry(QtCore.QRect(360, 10, 391, 69))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(-1)
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setStyleSheet("background-color: #4e4e4e;\n"
"color: #fafafa;\n"
"font-size:15px;\n"
"border:1px solid #4e4e4e;\n"
"box-shadow: 2px 2px 6px #000;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"hover:: background-color: #4CAF50;\n"
"\n"
"\n"
"")
        self.btn_exit.setObjectName("btn_exit")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 10, 141, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_add_new = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_new.sizePolicy().hasHeightForWidth())
        self.btn_add_new.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.btn_add_new.setFont(font)
        self.btn_add_new.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_new.setMouseTracking(False)
        self.btn_add_new.setTabletTracking(False)
        self.btn_add_new.setStyleSheet("QPushButton{\n"
"background-color: #4e4e4e;\n"
"color: #fafafa;\n"
"font-size:15px;\n"
"border:1px solid #4e4e4e;\n"
"box-shadow: 2px 2px 6px #2b2b2b;\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"}\n"
"QPushButton:hover { color: white }\n"
"\n"
"\n"
"")
        self.btn_add_new.setAutoDefault(False)
        self.btn_add_new.setDefault(False)
        self.btn_add_new.setFlat(False)
        self.btn_add_new.setObjectName("btn_add_new")
        self.verticalLayout.addWidget(self.btn_add_new)
        self.btn_del = QtWidgets.QPushButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(-1)
        self.btn_del.setFont(font)
        self.btn_del.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_del.setStyleSheet("background-color: #4e4e4e;\n"
"color: #fafafa;\n"
"font-size:15px;\n"
"border:1px solid #4e4e4e;\n"
"box-shadow: 2px 2px 6px #000;\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"hover:: background-color: #4CAF50;\n"
"\n"
"\n"
"")
        self.btn_del.setObjectName("btn_del")
        self.verticalLayout.addWidget(self.btn_del)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.btn_search)
        MainWindow.setTabOrder(self.btn_search, self.tableWidget_show)
        MainWindow.setTabOrder(self.tableWidget_show, self.listView_details)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telefon Defteri"))
        self.btn_details.setText(_translate("MainWindow", "Ayrıntılar"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Kişilerde ara"))
        self.btn_search.setText(_translate("MainWindow", "Ara"))
        self.tableWidget_show.setSortingEnabled(False)
        self.btn_exit.setText(_translate("MainWindow", "Çıkış"))
        self.btn_add_new.setText(_translate("MainWindow", "Yeni Kişi Ekle"))
        self.btn_del.setText(_translate("MainWindow", "Kişiyi Düzenle/Sil"))
