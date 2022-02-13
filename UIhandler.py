from UI.LoginPage import Login_Page
from UI.MainPage import Main_Page
from UI.AddAccount import Add_Account
from UI.AddLight import Add_Light
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import pymysql


class UIHandler:
    def __init__(self):
        """self.connection = pymysql.connect(
            host=' ',
            port= ,
            user=' ',
            passwd=' ',
            db=' ', charset='utf8', autocommit=True)"""

        # prepare a cursor object using cursor() method
        self.cursor = self.connection.cursor()

        self.cursor.execute("SELECT VERSION()")

        version = self.cursor.fetchone()

        print("Database version : %s " % version)

        self.login_page = Login_Page()
        self.main_page = Main_Page()
        self.add_account = Add_Account()
        self.add_light = Add_Light()

        self.LoginForm = QtWidgets.QWidget()
        self.MainForm = QtWidgets.QWidget()
        self.AccountForm = QtWidgets.QWidget()
        self.LightForm = QtWidgets.QWidget()

        self.login_page.switch_window_to_main.connect(self.show_main_page)
        self.login_page.show_login_warning.connect(self.show_login_warning_alert)

        self.main_page.show_logout_warning.connect(self.show_logout_message)
        self.main_page.show_add_account_page.connect(self.show_add_account)
        self.main_page.add_update.connect(self.main_page.add_list_update_account)
        self.main_page.show_auth_warning_account.connect((self.show_auth_warning_account))
        self.main_page.show_auth_warning_light.connect((self.show_auth_warning_light))
        self.main_page.show_auth_check.connect((self.show_auth_check))
        self.main_page.show_account_delete_warning.connect((self.show_account_delete_warning))
        self.main_page.show_add_light_page.connect(self.show_add_light)
        self.main_page.add_update_light.connect(self.main_page.add_list_update_light)

        self.add_account.add_account_success.connect(self.add_account_success)
        self.add_account.show_add_account_warning.connect(self.show_add_account_warning)
        self.add_account.close_add_account_page.connect(self.close_add_account_page)
        self.add_account.id_duplicate_warning.connect(self.id_duplicate_warning)

        self.add_light.light_duplicate_warning.connect(self.light_duplicate_warning)
        self.add_light.show_add_light_warning.connect(self.show_add_light_blank_warning)
        self.add_light.add_light_success.connect(self.add_light_success)
        self.add_light.close_add_light_page.connect(self.close_add_light_page)




    def show_login_page(self):
        self.login_page.cursor = self.cursor
        self.MainForm.close()
        self.login_page.setupUi(self.LoginForm)
        self.LoginForm.show()

    def show_main_page(self):
        self.main_page.cursor = self.cursor
        self.main_page.AUTH = self.login_page.AUTH
        self.main_page.loginID = self.login_page.loginID
        self.LoginForm.close()
        self.main_page.setupUi(self.MainForm)
        self.MainForm.show()

    def show_add_account(self):
        self.add_account.cursor = self.cursor
        self.add_account.loginAUTH = self.login_page.AUTH
        self.add_account.setupUi(self.AccountForm)
        self.AccountForm.show()

    def show_add_light(self):
        self.add_light.cursor = self.cursor
        self.add_light.loginAUTH = self.login_page.AUTH
        self.add_light.setupUi(self.LightForm)
        self.LightForm.show()


    def show_login_warning_alert(self):
        login_alert = QMessageBox()
        login_alert.setIcon(QMessageBox.Warning)
        login_alert.setText("로그인에 실패하였습니다.")
        login_alert.setWindowTitle("Warning")
        login_alert.setInformativeText('아이디 또는 비밀번호를 확인해주세요.')
        login_alert.setStandardButtons(QMessageBox.Ok)
        login_alert.setDefaultButton(QMessageBox.Ok)
        result = login_alert.exec()
        if result == QMessageBox.Ok:
            login_alert.close()

    def show_add_account_warning(self):
        self.account_alert = QMessageBox()
        self.account_alert.setIcon(QMessageBox.Warning)
        self.account_alert.setText("계정 추가에 실패하였습니다.")
        self.account_alert.setWindowTitle("Warning")
        self.account_alert.setInformativeText('빈칸을 확인해주세요')
        self.account_alert.exec_()

    def show_add_light_blank_warning(self):
        self.light_alert = QMessageBox()
        self.light_alert.setIcon(QMessageBox.Warning)
        self.light_alert.setText("조명 추가에 실패하였습니다.")
        self.light_alert.setWindowTitle("Warning")
        self.light_alert.setInformativeText('빈칸을 확인해주세요')
        self.light_alert.exec_()


    def add_account_success(self):
        self.AccountForm.close()
        self.main_page.ID =self.add_account.ID
        self.main_page.add_update.emit()

    def add_light_success(self):
        self.LightForm.close()
        self.main_page.lightID = self.add_light.ID
        print(self.add_light.ID)
        print(self.main_page.lightID)
        self.main_page.add_update_light.emit()

    def close_add_account_page(self):
        self.AccountForm.close()

    def close_add_light_page(self):
        self.LightForm.close()

    def show_auth_warning_account(self):
        self.auth_alert = QMessageBox()
        self.auth_alert.setIcon(QMessageBox.Warning)
        self.auth_alert.setText("계정 관리에 실패하였습니다.")
        self.auth_alert.setWindowTitle("Warning")
        self.auth_alert.setInformativeText('계정 추가 및 제거는 관리자만 가능합니다.')
        self.auth_alert.exec_()

    def show_auth_warning_light(self):
        self.auth_alert = QMessageBox()
        self.auth_alert.setIcon(QMessageBox.Warning)
        self.auth_alert.setText("조명 관리에 실패하였습니다.")
        self.auth_alert.setWindowTitle("Warning")
        self.auth_alert.setInformativeText('조명 추가 및 제거는 관리자만 가능합니다.')
        self.auth_alert.exec_()

    def show_auth_check(self):
        self.auth_check = QMessageBox()
        self.auth_check.setIcon(QMessageBox.Warning)
        self.auth_check.setText("권한 제어에 실패하였습니다.")
        self.auth_check.setWindowTitle("Warning")
        self.auth_check.setInformativeText('권한을 확인해주세요')
        self.auth_check.exec_()

    def show_account_delete_warning(self):
        self.delete_alert = QMessageBox()
        self.delete_alert.setIcon(QMessageBox.Warning)
        self.delete_alert.setText("계정 삭제에 실패하였습니다.")
        self.delete_alert.setWindowTitle("Warning")
        self.delete_alert.setInformativeText('현재 로그인중인 계정은 삭제할 수 없습니다.')
        self.delete_alert.exec_()

    def id_duplicate_warning(self):
        self.duplicate_warning = QMessageBox()
        self.duplicate_warning.setIcon(QMessageBox.Warning)
        self.duplicate_warning.setText("계정 추가에 실패하였습니다.")
        self.duplicate_warning.setWindowTitle("Warning")
        self.duplicate_warning.setInformativeText('이미 존재하는 ID입니다.')
        self.duplicate_warning.exec_()

    def light_duplicate_warning(self):
        self.duplicate_warning = QMessageBox()
        self.duplicate_warning.setIcon(QMessageBox.Warning)
        self.duplicate_warning.setText("조명 추가에 실패하였습니다.")
        self.duplicate_warning.setWindowTitle("Warning")
        self.duplicate_warning.setInformativeText('이미 존재하는 ID입니다.')
        self.duplicate_warning.exec_()

    def show_logout_message(self):
        result=0
        logout_alert = QMessageBox()
        logout_alert.setWindowTitle("Warning")
        logout_alert.setText("로그아웃 하시겠습니까?")
        logout_alert.setIcon(QMessageBox.Question)
        logout_alert.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        logout_alert.setDefaultButton(QMessageBox.Ok)

        result = logout_alert.exec_()
        if result == QMessageBox.Ok:
            logout_alert.close()
            self.show_login_page()
        elif result == QMessageBox.Cancel:
            logout_alert.close()


