from PyQt5.QtWidgets import *
from _form_del import Ui_form_del


class FormDel(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_del()
        self.ui.setupUi(self)
