# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_form_add_new.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_add_new(object):
    def setupUi(self, form_add_new):
        form_add_new.setObjectName("form_add_new")
        form_add_new.resize(330, 518)
        form_add_new.setStyleSheet("background-color:#C0C0C0;  border-radius: 10px;")
        self.btn_kisiyi_ekle = QtWidgets.QPushButton(form_add_new)
        self.btn_kisiyi_ekle.setGeometry(QtCore.QRect(40, 460, 247, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_kisiyi_ekle.setFont(font)
        self.btn_kisiyi_ekle.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_kisiyi_ekle.setStyleSheet("QPushButton{\n"
"background-color: #4e4e4e;\n"
"color: #fafafa;\n"
"font-size:15px;\n"
"border:1px solid #4e4e4e;\n"
"box-shadow: 2px 2px 6px #000;\n"
"border-radius: 10px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"transition-duration: 0.4s;\n"
"cursor: pointer;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #969696;\n"
"  color: white;\n"
"}")
        self.btn_kisiyi_ekle.setObjectName("btn_kisiyi_ekle")
        self.label_7 = QtWidgets.QLabel(form_add_new)
        self.label_7.setGeometry(QtCore.QRect(100, 10, 131, 121))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("user-512.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(form_add_new)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 180, 251, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self._2 = QtWidgets.QFormLayout(self.layoutWidget)
        self._2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self._2.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self._2.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self._2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self._2.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self._2.setContentsMargins(0, 4, 0, 25)
        self._2.setHorizontalSpacing(2)
        self._2.setVerticalSpacing(36)
        self._2.setObjectName("_2")
        self.lineEdit_isim_ekle = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit_isim_ekle.sizePolicy().hasHeightForWidth())
        self.lineEdit_isim_ekle.setSizePolicy(sizePolicy)
        self.lineEdit_isim_ekle.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_isim_ekle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_isim_ekle.setFont(font)
        self.lineEdit_isim_ekle.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;")
        self.lineEdit_isim_ekle.setInputMask("")
        self.lineEdit_isim_ekle.setText("")
        self.lineEdit_isim_ekle.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_isim_ekle.setClearButtonEnabled(True)
        self.lineEdit_isim_ekle.setObjectName("lineEdit_isim_ekle")
        self._2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_isim_ekle)
        self.lineEdit_soyisim_ekle = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit_soyisim_ekle.sizePolicy().hasHeightForWidth())
        self.lineEdit_soyisim_ekle.setSizePolicy(sizePolicy)
        self.lineEdit_soyisim_ekle.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_soyisim_ekle.setFont(font)
        self.lineEdit_soyisim_ekle.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;")
        self.lineEdit_soyisim_ekle.setInputMethodHints(QtCore.Qt.ImhUppercaseOnly)
        self.lineEdit_soyisim_ekle.setInputMask("")
        self.lineEdit_soyisim_ekle.setText("")
        self.lineEdit_soyisim_ekle.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_soyisim_ekle.setClearButtonEnabled(True)
        self.lineEdit_soyisim_ekle.setObjectName("lineEdit_soyisim_ekle")
        self._2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_soyisim_ekle)
        self.lineEdit_tel_ekle = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit_tel_ekle.sizePolicy().hasHeightForWidth())
        self.lineEdit_tel_ekle.setSizePolicy(sizePolicy)
        self.lineEdit_tel_ekle.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_tel_ekle.setFont(font)
        self.lineEdit_tel_ekle.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;")
        self.lineEdit_tel_ekle.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_tel_ekle.setInputMask("")
        self.lineEdit_tel_ekle.setText("")
        self.lineEdit_tel_ekle.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_tel_ekle.setClearButtonEnabled(True)
        self.lineEdit_tel_ekle.setObjectName("lineEdit_tel_ekle")
        self._2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tel_ekle)
        self.lineEdit_eposta_ekle = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit_eposta_ekle.sizePolicy().hasHeightForWidth())
        self.lineEdit_eposta_ekle.setSizePolicy(sizePolicy)
        self.lineEdit_eposta_ekle.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_eposta_ekle.setFont(font)
        self.lineEdit_eposta_ekle.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;")
        self.lineEdit_eposta_ekle.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.lineEdit_eposta_ekle.setInputMask("")
        self.lineEdit_eposta_ekle.setText("")
        self.lineEdit_eposta_ekle.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_eposta_ekle.setClearButtonEnabled(True)
        self.lineEdit_eposta_ekle.setObjectName("lineEdit_eposta_ekle")
        self._2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_eposta_ekle)
        self.lineEdit_tarih_ekle = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.lineEdit_tarih_ekle.sizePolicy().hasHeightForWidth())
        self.lineEdit_tarih_ekle.setSizePolicy(sizePolicy)
        self.lineEdit_tarih_ekle.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_tarih_ekle.setFont(font)
        self.lineEdit_tarih_ekle.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;")
        self.lineEdit_tarih_ekle.setInputMethodHints(QtCore.Qt.ImhDate)
        self.lineEdit_tarih_ekle.setInputMask("")
        self.lineEdit_tarih_ekle.setText("")
        self.lineEdit_tarih_ekle.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_tarih_ekle.setClearButtonEnabled(True)
        self.lineEdit_tarih_ekle.setObjectName("lineEdit_tarih_ekle")
        self._2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_tarih_ekle)

        self.retranslateUi(form_add_new)
        QtCore.QMetaObject.connectSlotsByName(form_add_new)

    def retranslateUi(self, form_add_new):
        _translate = QtCore.QCoreApplication.translate
        form_add_new.setWindowTitle(_translate("form_add_new", "Yeni Kişi Ekle"))
        self.btn_kisiyi_ekle.setText(_translate("form_add_new", "Kişiyi Ekle"))
        self.lineEdit_isim_ekle.setPlaceholderText(_translate("form_add_new", "İsim"))
        self.lineEdit_soyisim_ekle.setPlaceholderText(_translate("form_add_new", "Soyisim"))
        self.lineEdit_tel_ekle.setPlaceholderText(_translate("form_add_new", "Telefon Numarası"))
        self.lineEdit_eposta_ekle.setPlaceholderText(_translate("form_add_new", "E-Posta"))
        self.lineEdit_tarih_ekle.setPlaceholderText(_translate("form_add_new", "Doğum Tarihi"))
