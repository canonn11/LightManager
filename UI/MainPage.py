from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Main_Page(QWidget):
    #switch_window_to_webcam = QtCore.pyqtSignal()

    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1280, 720)
        self.Background = QtWidgets.QLabel(MainForm)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.Background.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.Clock = QtWidgets.QLabel(MainForm)
        self.Clock.setGeometry(QtCore.QRect(900, 0, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)


        #Blue Menubar
        self.Menubar = QtWidgets.QLabel(MainForm)
        self.Menubar.setGeometry(QtCore.QRect(0, 0, 64, 720))
        self.Menubar.setStyleSheet("background-color: rgb(11, 55, 255);")
        self.Menubar.setScaledContents(False)
        self.Menubar.setObjectName("Menubar")

        #White label background
        self.Top_Whitelabel = QtWidgets.QLabel(MainForm)
        self.Top_Whitelabel.setGeometry(QtCore.QRect(64, 0, 1216, 61))
        self.Top_Whitelabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Top_Whitelabel.setObjectName("Top_Whitelabel")

        #White label background 2
        self.Top_Whitelabel_2 = QtWidgets.QLabel(MainForm)
        self.Top_Whitelabel_2.setGeometry(QtCore.QRect(64, 65, 1216, 61))
        self.Top_Whitelabel_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Top_Whitelabel_2.setObjectName("Top_Whitelabel_2")

        #Lightmanager letter label
        self.LightManager = QtWidgets.QLabel(MainForm)
        self.LightManager.setGeometry(QtCore.QRect(80, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LightManager.setFont(font)
        self.LightManager.setStyleSheet("color: rgb(11, 55, 255);")
        self.LightManager.setObjectName("LightManager")

        #System overview letter label
        self.System_Overview = QtWidgets.QLabel(MainForm)
        self.System_Overview.setGeometry(QtCore.QRect(80, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.System_Overview.setFont(font)
        self.System_Overview.setObjectName("System_Overview")

        #Overview Background Label #1
        self.Overview1 = QtWidgets.QLabel(MainForm)
        self.Overview1.setGeometry(QtCore.QRect(100, 170, 511, 501))
        self.Overview1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Overview1.setObjectName("Overview1")

        # Overview Background Label #2
        self.Overview2 = QtWidgets.QLabel(MainForm)
        self.Overview2.setGeometry(QtCore.QRect(640, 170, 611, 241))
        self.Overview2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Overview2.setObjectName("Overview2")

        # Overview Background Label #3
        self.Overview3 = QtWidgets.QLabel(MainForm)
        self.Overview3.setGeometry(QtCore.QRect(640, 430, 611, 241))
        self.Overview3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Overview3.setObjectName("Overview3")

        # Left side Pushbutton #1 -> Overview Button
        self.MainButton = QtWidgets.QPushButton(MainForm)
        self.MainButton.setGeometry(QtCore.QRect(6, 10, 51, 51))
        self.MainButton.setStyleSheet("QPushButton{\n"
                                       "background-color: rgba(255, 255, 255, 0);\n"
                                       "border-image:url(UI/imgsource/clipboard1.png);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgba(255, 255, 255, 0);\n"
                                       "border-image:url(UI/imgsource/clipboard2.png);\n"
                                       "}")
        self.MainButton.setObjectName("MainButton")

        # Left side Pushbutton #2 -> LightControl Button
        self.LightControlButton = QtWidgets.QPushButton(MainForm)
        self.LightControlButton.setGeometry(QtCore.QRect(6, 80, 51, 51))
        self.LightControlButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/bulb1.png);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/bulb2.png);\n"
                                      "}")
        self.LightControlButton.setObjectName("LightControlButton")

        # Left side Pushbutton #3 -> LightManagement Button
        self.LightButton = QtWidgets.QPushButton(MainForm)
        self.LightButton.setGeometry(QtCore.QRect(6, 150, 51, 51))
        self.LightButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/folder1.png);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/folder2.png);\n"
                                      "}")
        self.LightButton.setObjectName("LightButton")


        # Left side Pushbutton #4 -> Account Control Button
        self.AccountButton = QtWidgets.QPushButton(MainForm)
        self.AccountButton.setGeometry(QtCore.QRect(6, 220, 51, 51))
        self.AccountButton.setStyleSheet("QPushButton{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/setting1.png);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/setting2.png);\n"
                                      "}")
        self.AccountButton.setObjectName("AccountButton")

        # Left side Pushbutton #5 -> Account Control Button
        self.LogOutButton = QtWidgets.QPushButton(MainForm)
        self.LogOutButton.setGeometry(QtCore.QRect(6, 290, 51, 51))
        self.LogOutButton.setStyleSheet("QPushButton{\n"
                                         "background-color: rgba(255, 255, 255, 0);\n"
                                         "border-image:url(UI/imgsource/exit1.png);\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(255, 255, 255, 0);\n"
                                         "border-image:url(UI/imgsource/exit2.png);\n"
                                         "}")
        self.LogOutButton.setObjectName("LogOutButton")

        # Sync Button
        self.SyncButton = QtWidgets.QPushButton(MainForm)
        self.SyncButton.setGeometry(QtCore.QRect(1220, 77, 41, 41))
        self.SyncButton.setStyleSheet("QPushButton{\n"
                                        "background-color: rgba(255, 255, 255, 0);\n"
                                        "border-image:url(UI/imgsource/sync1.png);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgba(255, 255, 255, 0);\n"
                                        "border-image:url(UI/imgsource/sync2.png);\n"
                                        "}")
        self.SyncButton.setObjectName("LogOutButton")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "LightManager"))
        MainForm.setWindowIcon(QIcon("UI/imgsource/lightbulb.png"))
        self.LightManager.setText(_translate("MainForm", "Light Manager"))
        self.System_Overview.setText(_translate("MainForm", "시스템 현황"))
