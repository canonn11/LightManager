from UI.LoginPage import Login_Page
from UI.MainPage import Main_Page
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import pymysql


class UIHandler:
    def __init__(self):
        self.connection = pymysql.connect(
            host='112.172.221.228',
            port=3306,
            user='software',
            passwd='1234',
            db='light_control', charset='utf8', autocommit=True)

        # prepare a cursor object using cursor() method
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT VERSION()")

        version = self.cursor.fetchone()

        print("Database version : %s " % version)

        self.login_page = Login_Page()
        self.main_page = Main_Page()

        self.LoginForm = QtWidgets.QWidget()
        self.MainForm = QtWidgets.QWidget()

    def show_login_page(self):
        self.login_page.cursor = self.cursor
        self.MainForm.close()
        self.login_page.setupUi(self.LoginForm)
        self.login_page.switch_window_to_main.connect(self.show_main_page)
        self.login_page.show_login_warning.connect(self.show_login_warning)
        self.LoginForm.show()

    def show_main_page(self):
        self.main_page.ID = self.login_page.ID
        self.main_page.Password = self.login_page.Password
        self.LoginForm.close()
        self.main_page.setupUi(self.MainForm)
        #self.main_page.switch_window_to_webcam.connect(self.show_webcam_page)
        self.MainForm.show()

    def show_login_warning(self):
        login_alert = QMessageBox()
        login_alert.setIcon(QMessageBox.Warning)
        login_alert.setText("로그인에 실패하였습니다.")
        login_alert.setWindowTitle("Warning")
        login_alert.setInformativeText('아이디 또는 비밀번호를 확인해주세요.')
        login_alert.exec_()