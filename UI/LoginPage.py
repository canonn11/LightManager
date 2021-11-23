from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import UIhandler


class Login_Page(QWidget):
    switch_window_to_main = QtCore.pyqtSignal()
    show_login_warning = QtCore.pyqtSignal()
    ID = '0'
    Password = '0'

    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(1280, 720)
        self.Background = QtWidgets.QLabel(LoginForm)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1280, 800))
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
        #self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.clicked.connect(self.switch_login_page)

        # Logo Text
        self.LogoText = QtWidgets.QLabel(LoginForm)
        self.LogoText.setGeometry(QtCore.QRect(590, 120, 291, 171))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.LogoText.setFont(font)
        self.LogoText.setStyleSheet("color: rgb(55, 168, 255);")
        self.LogoText.setObjectName("LogoText")

        # Logo Separator
        self.LogoSeparator = QtWidgets.QLabel(LoginForm)
        self.LogoSeparator.setGeometry(QtCore.QRect(550, 140, 5, 137))
        self.LogoSeparator.setPixmap(QtGui.QPixmap("UI/imgsource/rgb(55,168,255).png"))
        self.LogoSeparator.setScaledContents(True)
        self.LogoSeparator.setObjectName("LogoSeparator")

        # Logo Image
        self.LogoImage = QtWidgets.QLabel(LoginForm)
        self.LogoImage.setGeometry(QtCore.QRect(350, 110, 221, 191))
        self.LogoImage.setPixmap(QtGui.QPixmap("UI/imgsource/logoimage.png"))
        self.LogoImage.setScaledContents(True)
        self.LogoImage.setObjectName("LogoImage")

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
        self.PasswordLogo.setPixmap(QtGui.QPixmap("UI/imgsource/login-password.png"))
        self.PasswordLogo.setScaledContents(True)
        self.PasswordLogo.setObjectName("PasswordLogo")

        #Login Separator Label
        self.LoginSeparator = QtWidgets.QLabel(LoginForm)
        self.LoginSeparator.setGeometry(QtCore.QRect(460, 380, 2, 41))
        self.LoginSeparator.setPixmap(QtGui.QPixmap("UI/imgsource/black-background.jpg"))
        self.LoginSeparator.setObjectName("LoginSeparator")

        #Password Separator Label
        self.PasswordSeparator = QtWidgets.QLabel(LoginForm)
        self.PasswordSeparator.setGeometry(QtCore.QRect(460, 450, 2, 41))
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

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "LightManager"))
        LoginForm.setWindowIcon(QIcon("UI/imgsource/lightbulb.png"))
        self.LoginButton.setText(_translate("LoginForm", "L O G I N"))
        self.LoginLabel.setText(_translate("LoginForm", "TextLabel"))
        self.PasswordLabel.setText(_translate("LoginForm", "TextLabel"))
        self.lineEdit_ID.setPlaceholderText(_translate("LoginForm", "Username"))
        self.lineEdit_Password.setPlaceholderText(_translate("LoginForm", "Password"))
        self.LogoText.setText(_translate("LoginForm", "Light\n"
                                                 "Manager"))


    # LoginButton Event Handler
    def switch_login_page(self):
        self.ID = self.lineEdit_ID.text()
        self.Password = self.lineEdit_Password.text()
        self.switch_window_to_main.emit()

        """login_procedure = "call check_login_success('"+self.ID+"','"+self.Password+"',"+"@output"+")"
        self.cursor.execute(login_procedure)
        self.output = "select @output"
        self.cursor.execute(self.output)
        self.login_result = self.cursor.fetchone()

        #Login Success => go mainpage
        if(self.login_result[0]==0):
            self.switch_window_to_main.emit()
        #Login Failed => Warning Message
        else:
            self.show_login_warning.emit()"""