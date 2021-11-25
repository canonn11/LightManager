from UI.LoginPage import Login_Page
from UI.MainPage import Main_Page
from UI.AddAccount import Add_Account
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
        self.add_account = Add_Account()

        self.LoginForm = QtWidgets.QWidget()
        self.MainForm = QtWidgets.QWidget()
        self.AccountForm = QtWidgets.QWidget()

    def show_login_page(self):
        self.login_page.cursor = self.cursor
        self.MainForm.close()
        self.login_page.setupUi(self.LoginForm)
        self.login_page.switch_window_to_main.connect(self.show_main_page)
        self.login_page.show_login_warning.connect(self.show_login_warning)
        self.LoginForm.show()

    def show_main_page(self):
        self.main_page.cursor = self.cursor
        self.main_page.AUTH = self.login_page.AUTH
        self.LoginForm.close()
        self.main_page.setupUi(self.MainForm)
        self.main_page.show_logout_warning.connect(self.show_logout_message)
        self.main_page.show_add_account_page.connect(self.show_add_account)
        self.main_page.add_update.connect(self.main_page.add_list_update)
        self.MainForm.show()

    def show_add_account(self):
        self.add_account.cursor = self.cursor
        self.add_account.setupUi(self.AccountForm)
        self.add_account.add_account_success.connect(self.add_account_success)
        self.add_account.show_add_account_warning.connect(self.show_add_account_warning)
        self.add_account.close_add_account_page.connect(self.close_add_account_page)
        self.AccountForm.show()

    def add_account_success(self):
        self.AccountForm.close()
        self.main_page.NAME =self.add_account.NAME
        self.main_page.add_update.emit()

    def close_add_account_page(self):
        self.AccountForm.close()

    def show_login_warning(self):
        login_alert = QMessageBox()
        login_alert.setIcon(QMessageBox.Warning)
        login_alert.setText("로그인에 실패하였습니다.")
        login_alert.setWindowTitle("Warning")
        login_alert.setInformativeText('아이디 또는 비밀번호를 확인해주세요.')
        login_alert.exec_()

    def show_add_account_warning(self):
        login_alert = QMessageBox()
        login_alert.setIcon(QMessageBox.Warning)
        login_alert.setText("계정 추가에 실패하였습니다.")
        login_alert.setWindowTitle("Warning")
        login_alert.setInformativeText('빈칸을 확인해주세요')
        login_alert.exec_()

    def show_logout_message(self):
        result=0
        logout_alert = QMessageBox()
        logout_alert.setWindowTitle("Warning")
        logout_alert.setText("로그아웃 하시겠습니까?")
        logout_alert.setIcon(QMessageBox.Question)
        logout_alert.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        logout_alert.setDefaultButton(QMessageBox.Ok)

        result = logout_alert.exec()
        if result == QMessageBox.Ok:
            self.show_login_page()


