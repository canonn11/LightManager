from UI.LoginPage import Login_Page
from UI.MainPage import Main_Page
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class UIHandler:
    def __init__(self):
        self.login_page = Login_Page()
        self.main_page = Main_Page()

        self.LoginForm = QtWidgets.QWidget()
        self.MainForm = QtWidgets.QWidget()

    def show_login_page(self):
        self.MainForm.close()
        self.login_page.setupUi(self.LoginForm)
        self.login_page.switch_window_to_main.connect(self.show_main_page)
        self.LoginForm.show()

    def show_main_page(self):
        self.main_page.ID = self.login_page.ID
        self.main_page.Password = self.login_page.Password
        self.LoginForm.close()
        self.main_page.setupUi(self.MainForm)
        #self.main_page.switch_window_to_webcam.connect(self.show_webcam_page)
        self.MainForm.show()