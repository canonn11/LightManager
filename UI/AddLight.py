from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Add_Light(QWidget):
    show_add_light_warning = QtCore.pyqtSignal()
    add_light_success = QtCore.pyqtSignal()
    close_add_light_page = QtCore.pyqtSignal()
    light_duplicate_warning = QtCore.pyqtSignal()

    def setupUi(self, LightForm):
        LightForm.setObjectName("LightForm")
        LightForm.resize(480, 290)

        #Background label
        self.background_label = QtWidgets.QLabel(LightForm)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 480, 290))
        self.background_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.background_label.setText("")
        self.background_label.setObjectName("background_label")

        #Title label
        self.title_textlabel = QtWidgets.QLabel(LightForm)
        self.title_textlabel.setGeometry(QtCore.QRect(30, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.title_textlabel.setFont(font)
        self.title_textlabel.setObjectName("title_textlabel")

        #id text label
        self.id_textlabel = QtWidgets.QLabel(LightForm)
        self.id_textlabel.setGeometry(QtCore.QRect(40, 80, 61, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.id_textlabel.setFont(font)
        self.id_textlabel.setObjectName("id_textlabel")

        #loc text label
        self.loc_textlabel = QtWidgets.QLabel(LightForm)
        self.loc_textlabel.setGeometry(QtCore.QRect(40, 140, 61, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.loc_textlabel.setFont(font)
        self.loc_textlabel.setObjectName("loc_textlabel")

        #ok button
        self.ok_button = QtWidgets.QPushButton(LightForm)
        self.ok_button.setGeometry(QtCore.QRect(90, 210, 111, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setPointSize(12)
        self.ok_button.setFont(font)
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

        #cancel button
        self.cancel_button = QtWidgets.QPushButton(LightForm)
        self.cancel_button.setGeometry(QtCore.QRect(260, 210, 111, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setPointSize(12)
        self.cancel_button.setFont(font)
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

        #id_border
        self.id_border = QtWidgets.QLabel(LightForm)
        self.id_border.setGeometry(QtCore.QRect(120, 80, 301, 41))
        self.id_border.setStyleSheet("border:2px solid rgba(105,118,132,255);\n"
                                    "background-color:rgba(0,0,0,0);\n"
                                    "border-radius:12px;")
        self.id_border.setText("")
        self.id_border.setObjectName("id_border")

        #loc_border
        self.loc_border = QtWidgets.QLabel(LightForm)
        self.loc_border.setGeometry(QtCore.QRect(120, 140, 301, 41))
        self.loc_border.setStyleSheet("border:2px solid rgba(105,118,132,255);\n"
                                    "background-color:rgba(0,0,0,0);\n"
                                    "border-radius:12px;")
        self.loc_border.setText("")
        self.loc_border.setObjectName("loc_border")

        #id_lineedit
        self.id_lineedit = QtWidgets.QLineEdit(LightForm)
        self.id_lineedit.setGeometry(QtCore.QRect(130, 85, 282, 30))
        self.id_lineedit.setStyleSheet("border-radius:2px;")
        self.id_lineedit.setObjectName("id_lineedit")

        #loc lineedit
        self.loc_lineedit = QtWidgets.QLineEdit(LightForm)
        self.loc_lineedit.setGeometry(QtCore.QRect(130, 145, 282, 30))
        self.loc_lineedit.setStyleSheet("border-radius:2px;")
        self.loc_lineedit.setObjectName("loc_lineedit")

        self.retranslateUi(LightForm)
        QtCore.QMetaObject.connectSlotsByName(LightForm)

    def retranslateUi(self, LightForm):
        _translate = QtCore.QCoreApplication.translate
        LightForm.setWindowTitle(_translate("AccountForm", "조명 추가"))
        LightForm.setWindowIcon(QIcon("UI/imgsource/lightbulb.png"))
        self.title_textlabel.setText(_translate("LightForm", "조명 추가"))
        self.id_textlabel.setText(_translate("LightForm", "ID"))
        self.loc_textlabel.setText(_translate("LightForm", "위치"))
        self.ok_button.setText(_translate("LightForm", "OK"))
        self.cancel_button.setText(_translate("LightForm", "Cancel"))


    def add_ok(self):
        self.ID = ''
        self.LOC = ''
        self.ID = self.id_lineedit.text()
        self.LOC = self.loc_lineedit.text()
        duplicate_check = "select * from light_list where light_id = '"+self.ID+"';"
        self.cursor.execute(duplicate_check)
        result = self.cursor.fetchone()
        if(self.ID == '') or (self.LOC == ''):
            self.show_add_light_warning.emit()
        else:
            if (result is not None):
                self.light_duplicate_warning.emit()
            else:
                add_procedure = "call plus_light(" +self.ID+","+self.LOC+");"
                self.cursor.execute(add_procedure)
                self.add_light_success.emit()

    def close_page(self):
        self.close_add_light_page.emit()