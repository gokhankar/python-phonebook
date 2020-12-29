from PyQt5.QtWidgets import *
from _form_edit import Ui_form_edit


class FormEdit(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_form_edit()
        self.ui.setupUi(self)
