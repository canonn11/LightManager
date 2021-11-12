from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys

class Login_Page(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()
    ID = '0'
    Password = '0'

    def setupUi(self, LoginForm):
        LoginForm.setObjectName("Form")
        LoginForm.resize(1280, 720)
        self.Background = QtWidgets.QLabel(LoginForm)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("UI/imgsource/white-background.png"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.LoginButton = QtWidgets.QPushButton(LoginForm)
        self.LoginButton.setGeometry(QtCore.QRect(400, 510, 480, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        #Login Pushbutton
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("QPushButton{\n"
                                       "background-color: rgb(55, 168, 255);\n"
                                       "border-radius:12px;\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgb(159, 159, 159);\n"
                                       "border-radius : 12px;\n"
                                       "} \n"
                                       "QPushButton:pressed{\n"
                                       "background-color: rgb(132, 132, 132);\n"
                                       "border-radius : 12px;\n"
                                       "}")
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.clicked.connect(self.switch_login_page)

        # Login border Label
        self.LoginLabel = QtWidgets.QLabel(LoginForm)
        self.LoginLabel.setGeometry(QtCore.QRect(400, 370, 480, 60))
        self.LoginLabel.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border:2px solid rgba(105,118,132,255);\n"
                                      "border-radius:12px;\n"
                                      "color:rgba(255,255,255,230);\n"
                                      "padding-bottom:\n"
                                      "")
        self.LoginLabel.setObjectName("LoginLabel")

        # Login Logo Label
        self.LoginLogo = QtWidgets.QLabel(LoginForm)
        self.LoginLogo.setGeometry(QtCore.QRect(410, 380, 41, 41))
        self.LoginLogo.setText("")
        self.LoginLogo.setPixmap(QtGui.QPixmap("UI/imgsource/login-id.png"))
        self.LoginLogo.setScaledContents(True)
        self.LoginLogo.setObjectName("LoginLogo")

        # Password border Label
        self.PasswordLabel = QtWidgets.QLabel(LoginForm)
        self.PasswordLabel.setGeometry(QtCore.QRect(400, 440, 480, 60))
        self.PasswordLabel.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                         "border:2px solid rgba(105,118,132,255);\n"
                                         "border-radius:12px;\n"
                                         "color:rgba(255,255,255,230);\n"
                                         "padding-bottom:\n"
                                         "")
        self.PasswordLabel.setObjectName("PasswordLabel")

        #Password Logo Label
        self.PasswordLogo = QtWidgets.QLabel(LoginForm)
        self.PasswordLogo.setGeometry(QtCore.QRect(410, 450, 41, 41))
        self.PasswordLogo.setText("")
        self.PasswordLogo.setPixmap(QtGui.QPixmap("UI/imgsource/login-password.png"))
        self.PasswordLogo.setScaledContents(True)
        self.PasswordLogo.setObjectName("PasswordLogo")

        #Login Separator Label
        self.LoginSeparator = QtWidgets.QLabel(LoginForm)
        self.LoginSeparator.setGeometry(QtCore.QRect(460, 380, 2, 41))
        self.LoginSeparator.setStyleSheet("background-color:rgba(0,0,0,0)\n"
                                          "border-none;\n"
                                          "border-left:2px solid rgba(105,118,132,255);")
        self.LoginSeparator.setText("")
        self.LoginSeparator.setPixmap(QtGui.QPixmap("UI/imgsource/black-background.jpg"))
        self.LoginSeparator.setObjectName("LoginSeparator")

        #Password Separator Label
        self.PasswordSeparator = QtWidgets.QLabel(LoginForm)
        self.PasswordSeparator.setGeometry(QtCore.QRect(460, 450, 2, 41))
        self.PasswordSeparator.setStyleSheet("background-color:rgba(0,0,0,0)\n"
                                   "border-none;\n"
                                   "border-left:2px solid rgba(105,118,132,255);")
        self.PasswordSeparator.setText("")
        self.PasswordSeparator.setPixmap(QtGui.QPixmap("UI/imgsource/black-background.jpg"))
        self.PasswordSeparator.setObjectName("PasswordSeparator")

        #Linedeit ID
        self.lineEdit_ID = QtWidgets.QLineEdit(LoginForm)
        self.lineEdit_ID.setGeometry(QtCore.QRect(470, 380, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setStyleSheet("border:none;")
        self.lineEdit_ID.setObjectName("lineEdit_ID")

        #Lineedit Password
        self.lineEdit_Password = QtWidgets.QLineEdit(LoginForm)
        self.lineEdit_Password.setGeometry(QtCore.QRect(470, 450, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_Password.setFont(font)
        self.lineEdit_Password.setStyleSheet("border:none;")
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setCursorPosition(0)
        self.lineEdit_Password.setObjectName("lineEdit_Password")

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LoginButton.setText(_translate("Form", "L O G I N"))
        self.LoginLabel.setText(_translate("Form", "TextLabel"))
        self.PasswordLabel.setText(_translate("Form", "TextLabel"))
        self.lineEdit_ID.setPlaceholderText(_translate("Form", "Username"))
        self.lineEdit_Password.setPlaceholderText(_translate("Form", "Password"))


    # 여기에 id,pw 오류처리 및 확인과정 들어가야됨
    def switch_login_page(self):
        self.ID = self.lineEdit_SID.text()
        self.Password = self.lineEdit_Name.text()
        self.switch_window_to_main.emit()