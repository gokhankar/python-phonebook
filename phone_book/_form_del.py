# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_form_del.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_del(object):
    def setupUi(self, form_del):
        form_del.setObjectName("form_del")
        form_del.resize(329, 573)
        form_del.setStyleSheet("background-color:#ff9900;")
        self.formLayoutWidget = QtWidgets.QWidget(form_del)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 190, 291, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_dogum = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_dogum.sizePolicy().hasHeightForWidth())
        self.lineEdit_dogum.setSizePolicy(sizePolicy)
        self.lineEdit_dogum.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_dogum.setInputMask("")
        self.lineEdit_dogum.setObjectName("lineEdit_dogum")
        self.gridLayout.addWidget(self.lineEdit_dogum, 4, 0, 1, 1)
        self.lineEdit_soyisim = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_soyisim.sizePolicy().hasHeightForWidth())
        self.lineEdit_soyisim.setSizePolicy(sizePolicy)
        self.lineEdit_soyisim.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_soyisim.setObjectName("lineEdit_soyisim")
        self.gridLayout.addWidget(self.lineEdit_soyisim, 1, 0, 1, 1)
        self.lineEdit_isim = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_isim.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_isim.sizePolicy().hasHeightForWidth())
        self.lineEdit_isim.setSizePolicy(sizePolicy)
        self.lineEdit_isim.setMouseTracking(True)
        self.lineEdit_isim.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_isim.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_isim.setClearButtonEnabled(True)
        self.lineEdit_isim.setObjectName("lineEdit_isim")
        self.gridLayout.addWidget(self.lineEdit_isim, 0, 0, 1, 1)
        self.lineEdit_email = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_email.sizePolicy().hasHeightForWidth())
        self.lineEdit_email.setSizePolicy(sizePolicy)
        self.lineEdit_email.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.gridLayout.addWidget(self.lineEdit_email, 3, 0, 1, 1)
        self.lineEdit_tel = QtWidgets.QLineEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_tel.sizePolicy().hasHeightForWidth())
        self.lineEdit_tel.setSizePolicy(sizePolicy)
        self.lineEdit_tel.setStyleSheet("background-color:#f7f7f7;\n"
"color: #464646;\n"
"padding-top:3px;\n"
"padding-left: 10px;\n"
"box-shadow: 2px 2px 6px #000;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.gridLayout.addWidget(self.lineEdit_tel, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(form_del)
        self.label_7.setGeometry(QtCore.QRect(80, 10, 161, 161))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("user-512.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.layoutWidget = QtWidgets.QWidget(form_del)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 490, 291, 72))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
"  background-color: #4CAF50;\n"
"  color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
"  background-color: #4CAF50;\n"
"  color: white;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(form_del)
        QtCore.QMetaObject.connectSlotsByName(form_del)

    def retranslateUi(self, form_del):
        _translate = QtCore.QCoreApplication.translate
        form_del.setWindowTitle(_translate("form_del", "Form"))
        self.lineEdit_dogum.setPlaceholderText(_translate("form_del", "Doğum Tarihi"))
        self.lineEdit_soyisim.setPlaceholderText(_translate("form_del", "Soyisim"))
        self.lineEdit_isim.setPlaceholderText(_translate("form_del", "İsim"))
        self.lineEdit_email.setPlaceholderText(_translate("form_del", "E-Posta"))
        self.lineEdit_tel.setPlaceholderText(_translate("form_del", "Telefon Numarası"))
        self.pushButton.setText(_translate("form_del", "Kişiyi sil"))
        self.pushButton_2.setText(_translate("form_del", "Kişiyi güncelle"))
