from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Add_Account(QWidget):
    add_account_success = QtCore.pyqtSignal()
    show_add_account_warning = QtCore.pyqtSignal()
    close_add_account_page = QtCore.pyqtSignal()
    id_duplicate_warning = QtCore.pyqtSignal()
    ID = ''
    PW=''
    NAME = ''
    LOC = ''
    AUTH = ''
    def setupUi(self, AccountForm):


        AccountForm.setObjectName("AccountForm")
        AccountForm.resize(480, 480)
        self.background_label = QtWidgets.QLabel(AccountForm)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 480, 480))
        self.background_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")

        # Title Text Label
        self.title_textlabel = QtWidgets.QLabel(AccountForm)
        self.title_textlabel.setGeometry(QtCore.QRect(30, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_textlabel.setFont(font)
        self.title_textlabel.setObjectName("title_textlabel")

        # GroupBox for Check Radiobutton
        self.groupBox = QtWidgets.QGroupBox(AccountForm)
        self.groupBox.setGeometry(QtCore.QRect(30, 320, 401, 71))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")

        # radiobutton for admin
        self.admin_radiobutton = QtWidgets.QRadioButton(self.groupBox)
        self.admin_radiobutton.setGeometry(QtCore.QRect(70, 30, 108, 19))
        self.admin_radiobutton.setObjectName("admin_radiobutton")

        #radiobutton for user
        self.user_radiobutton = QtWidgets.QRadioButton(self.groupBox)
        self.user_radiobutton.setGeometry(QtCore.QRect(250, 30, 108, 19))
        self.user_radiobutton.setObjectName("user_radiobutton")

        #textlabel for id
        self.id_textlabel = QtWidgets.QLabel(AccountForm)
        self.id_textlabel.setGeometry(QtCore.QRect(40, 80, 61, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.id_textlabel.setFont(font)
        self.id_textlabel.setObjectName("id_textlabel")

        #textlabel for pw
        self.pw_textlabel = QtWidgets.QLabel(AccountForm)
        self.pw_textlabel.setGeometry(QtCore.QRect(20, 140, 81, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.pw_textlabel.setFont(font)
        self.pw_textlabel.setObjectName("pw_textlabel")

        #textlabel for name
        self.name_textlabel = QtWidgets.QLabel(AccountForm)
        self.name_textlabel.setGeometry(QtCore.QRect(33, 200, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.name_textlabel.setFont(font)
        self.name_textlabel.setObjectName("name_textlabel")

        #textlabel for location
        self.loc_textlabel = QtWidgets.QLabel(AccountForm)
        self.loc_textlabel.setGeometry(QtCore.QRect(33, 260, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.loc_textlabel.setFont(font)
        self.loc_textlabel.setObjectName("loc_textlabel")

        #pushbutton for OK
        self.ok_button = QtWidgets.QPushButton(AccountForm)
        self.ok_button.setGeometry(QtCore.QRect(110, 410, 111, 41))
        self.ok_button.setStyleSheet("QPushButton{\n"
                                              "background-color: rgb(53, 174, 255);\n"
                                              "border-radius:12px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgb(153, 153, 153);\n"
                                              "border-radius:12px;\n"
                                              "}")
        self.ok_button.setObjectName("ok_button")
        self.ok_button.clicked.connect(self.add_ok)

        #pushbutton for Cancel
        self.cancel_button = QtWidgets.QPushButton(AccountForm)
        self.cancel_button.setGeometry(QtCore.QRect(250, 410, 111, 41))
        self.cancel_button.setStyleSheet("QPushButton{\n"
                                     "background-color: rgb(153, 153, 153);\n"
                                     "border-radius:12px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgb(95, 95, 95);\n"
                                     "border-radius:12px;\n"
                                     "}")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.clicked.connect(self.close_page)

        #border for id
        self.id_border = QtWidgets.QLabel(AccountForm)
        self.id_border.setGeometry(QtCore.QRect(120, 80, 301, 41))
        self.id_border.setStyleSheet("border:2px solid rgba(105,118,132,255);\n"
                                    "background-color:rgba(0,0,0,0);\n"
                                    "border-radius:12px;")
        self.id_border.setObjectName("id_border")

        #border for pw
        self.pw_border = QtWidgets.QLabel(AccountForm)
        self.pw_border.setGeometry(QtCore.QRect(120, 140, 301, 41))
        self.pw_border.setStyleSheet("border:2px solid rgba(105,118,132,255);\n"
                                    "background-color:rgba(0,0,0,0);\n"
                                    "border-radius:12px;")
        self.pw_border.setObjectName("pw_border")

        #border for name
        self.name_border = QtWidgets.QLabel(AccountForm)
        self.name_border.setGeometry(QtCore.QRect(120, 200, 301, 41))
        self.name_border.setStyleSheet("border:2px solid rgba(105,118,132,255);\n"
                                        "background-color:rgba(0,0,0,0);\n"
                                        "border-radius:12px;")
        self.name_border.setObjectName("name_border")

        #border for location
        self.loc_border = QtWidgets.QLabel(AccountForm)
        self.loc_border.setGeometry(QtCore.QRect(120, 260, 301, 41))
        self.loc_border.setStyleSheet("border:2px solid rgba(105,118,132,255);\n"
                                        "background-color:rgba(0,0,0,0);\n"
                                        "border-radius:12px;")
        self.loc_border.setObjectName("loc_border")

        #lineedit for id
        self.id_lineedit = QtWidgets.QLineEdit(AccountForm)
        self.id_lineedit.setGeometry(QtCore.QRect(130, 85, 282, 30))
        self.id_lineedit.setStyleSheet("border-radius:2px;")
        self.id_lineedit.setObjectName("id_lineedit")

        #lineedit for pw
        self.pw_lineedit = QtWidgets.QLineEdit(AccountForm)
        self.pw_lineedit.setGeometry(QtCore.QRect(130, 145, 282, 30))
        self.pw_lineedit.setStyleSheet("border-radius:2px;")
        self.pw_lineedit.setObjectName("pw_lineedit")

        #lineedit for name
        self.name_lineedit = QtWidgets.QLineEdit(AccountForm)
        self.name_lineedit.setGeometry(QtCore.QRect(130, 205, 282, 30))
        self.name_lineedit.setStyleSheet("border-radius:2px;")
        self.name_lineedit.setObjectName("name_button")

        #lineedit for button
        self.loc_lineedit = QtWidgets.QLineEdit(AccountForm)
        self.loc_lineedit.setGeometry(QtCore.QRect(130, 265, 282, 30))
        self.loc_lineedit.setStyleSheet("border-radius:2px;")
        self.loc_lineedit.setObjectName("loc_button")

        self.retranslateUi(AccountForm)
        QtCore.QMetaObject.connectSlotsByName(AccountForm)

    def retranslateUi(self, AccountForm):
        _translate = QtCore.QCoreApplication.translate
        AccountForm.setWindowTitle(_translate("AccountForm", "계정 추가"))
        AccountForm.setWindowIcon(QIcon("UI/imgsource/lightbulb.png"))
        self.title_textlabel.setText(_translate("AccountForm", "계정 추가"))
        self.groupBox.setTitle(_translate("AccountForm", "권한"))
        self.admin_radiobutton.setText(_translate("AccountForm", "관리자"))
        self.user_radiobutton.setText(_translate("AccountForm", "유저"))
        self.id_textlabel.setText(_translate("AccountForm", "ID"))
        self.pw_textlabel.setText(_translate("AccountForm", "Password"))
        self.name_textlabel.setText(_translate("AccountForm", "이름"))
        self.loc_textlabel.setText(_translate("AccountForm", "위치"))
        self.ok_button.setText(_translate("AccountForm", "OK"))
        self.cancel_button.setText(_translate("AccountForm", "Cancel"))


    def add_ok(self):
        self.ID = ''
        self.PW = ''
        self.NAME = ''
        self.LOC = ''
        self.AUTH = ''
        self.ID = self.id_lineedit.text()
        self.PW = self.pw_lineedit.text()
        self.NAME = self.name_lineedit.text()
        self.LOC = self.loc_lineedit.text()
        if self.admin_radiobutton.isChecked():
            self.AUTH = '1'
        elif self.user_radiobutton.isChecked():
            self.AUTH = '0'
        else:
            self.AUTH = None
        duplicate_check = "select * from id_table where user_id = '"+self.ID+"';"
        self.cursor.execute(duplicate_check)
        result = self.cursor.fetchone()
        if(self.ID == '') or (self.PW == '') or (self.NAME == '') or (self.LOC == '') or (self.AUTH == None):
            self.show_add_account_warning.emit()
        else:
            if (result is not None):
                self.id_duplicate_warning.emit()
            else:
                add_procedure = "call user_plus('" + self.NAME + "','" + self.ID + "','" + self.PW + "','" + self.LOC + "'," + self.AUTH + ")"
                self.cursor.execute(add_procedure)
                self.add_account_success.emit()

    def close_page(self):
        self.close_add_account_page.emit()