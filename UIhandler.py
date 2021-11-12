from UI.LoginPage import Login_Page
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class UIHandler:
    def __init__(self):
        self.login_page = Login_Page()

        self.LoginForm = QtWidgets.QWidget()

    def show_login_page(self):
        #self.MainForm.close()
        self.login_page.setupUi(self.LoginForm)
        #self.login_page.switch_window_to_main.connect(self.show_main_page)
        self.LoginForm.show()