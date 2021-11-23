from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Main_Page(QWidget):
    show_logout_warning = QtCore.pyqtSignal()

    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1280, 720)
        self.Background = QtWidgets.QLabel(MainForm)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.Background.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.Background.setText("")
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")

        # Blue Menubar
        self.Menubar = QtWidgets.QLabel(MainForm)
        self.Menubar.setGeometry(QtCore.QRect(0, 0, 64, 720))
        self.Menubar.setStyleSheet("background-color: rgb(11, 55, 255);")
        self.Menubar.setScaledContents(False)
        self.Menubar.setObjectName("Menubar")

        # White label background
        self.Top_Whitelabel = QtWidgets.QLabel(MainForm)
        self.Top_Whitelabel.setGeometry(QtCore.QRect(64, 0, 1216, 61))
        self.Top_Whitelabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Top_Whitelabel.setObjectName("Top_Whitelabel")

        # Lightmanager letter label
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
        self.MainButton.clicked.connect(self.switch_layout_0)

        # Left side Pushbutton #2 -> LightControl Button
        self.LightButton = QtWidgets.QPushButton(MainForm)
        self.LightButton.setGeometry(QtCore.QRect(6, 80, 51, 51))
        self.LightButton.setStyleSheet("QPushButton{\n"
                                       "background-color: rgba(255, 255, 255, 0);\n"
                                       "border-image:url(UI/imgsource/folder1.png);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgba(255, 255, 255, 0);\n"
                                       "border-image:url(UI/imgsource/folder2.png);\n"
                                       "}")
        self.LightButton.setObjectName("LightButton")
        self.LightButton.clicked.connect(self.switch_layout_1)

        # Left side Pushbutton #3 -> LightManagement Button
        self.LightControlButton = QtWidgets.QPushButton(MainForm)
        self.LightControlButton.setGeometry(QtCore.QRect(6, 150, 51, 51))
        self.LightControlButton.setStyleSheet("QPushButton{\n"
                                                      "background-color: rgba(255, 255, 255, 0);\n"
                                                      "border-image:url(UI/imgsource/bulb1.png);\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "background-color: rgba(255, 255, 255, 0);\n"
                                                      "border-image:url(UI/imgsource/bulb2.png);\n"
                                                      "}")
        self.LightControlButton.setObjectName("LightControlButton")
        self.LightControlButton.clicked.connect(self.switch_layout_2)

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
        self.AccountButton.clicked.connect(self.switch_layout_3)

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
        self.LogOutButton.clicked.connect(self.logout_main_page)

        #Stacked Widget
        self.stackedWidget = QtWidgets.QStackedWidget(MainForm)
        self.stackedWidget.setGeometry(QtCore.QRect(64, 65, 1216, 655))
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")

        # page #0
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")

        # page #0 background label
        self.page0_background = QtWidgets.QLabel(self.page_0)
        self.page0_background.setGeometry(QtCore.QRect(0, 0, 1216, 655))
        self.page0_background.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.page0_background.setObjectName("page0_background")

        # page #0 top white label
        self.page0_top_whitelabel = QtWidgets.QLabel(self.page_0)
        self.page0_top_whitelabel.setGeometry(QtCore.QRect(0, 0, 1216, 61))
        self.page0_top_whitelabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page0_top_whitelabel.setObjectName("page0_top_whitelabel")

        # page #0 top letter label
        self.system_overview_label = QtWidgets.QLabel(self.page_0)
        self.system_overview_label.setGeometry(QtCore.QRect(20, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.system_overview_label.setFont(font)
        self.system_overview_label.setObjectName("system_overview_label")

        # page #0 refresh button
        self.page0_refresh_button = QtWidgets.QPushButton(self.page_0)
        self.page0_refresh_button.setGeometry(QtCore.QRect(1160, 10, 41, 41))
        self.page0_refresh_button.setStyleSheet("QPushButton{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/sync1.png);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/sync2.png);\n"
                                      "}")
        self.page0_refresh_button.setObjectName("page0_refresh_button")
        #
        self.stackedWidget.addWidget(self.page_0)

        # page #1
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")

        # page #1 background label
        self.page1_background = QtWidgets.QLabel(self.page_1)
        self.page1_background.setGeometry(QtCore.QRect(0, 0, 1216, 655))
        self.page1_background.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.page1_background.setObjectName("page1_background")

        # page #1 top white label
        self.page1_top_whitelabel = QtWidgets.QLabel(self.page_1)
        self.page1_top_whitelabel.setGeometry(QtCore.QRect(0, 0, 1216, 61))
        self.page1_top_whitelabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page1_top_whitelabel.setObjectName("page1_top_whitelabel")

        # page #1 top letter label
        self.light_status_label = QtWidgets.QLabel(self.page_1)
        self.light_status_label.setGeometry(QtCore.QRect(20, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.light_status_label.setFont(font)
        self.light_status_label.setObjectName("light_status_label")


        self.stackedWidget.addWidget(self.page_1)

        # page #2
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")

        # page #2 background label
        self.page2_background = QtWidgets.QLabel(self.page_2)
        self.page2_background.setGeometry(QtCore.QRect(0, 0, 1216, 655))
        self.page2_background.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.page2_background.setMidLineWidth(-1)
        self.page2_background.setObjectName("page2_background")

        # page #2 top white label
        self.page2_top_whitelabel = QtWidgets.QLabel(self.page_2)
        self.page2_top_whitelabel.setGeometry(QtCore.QRect(0, 0, 1216, 61))
        self.page2_top_whitelabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page2_top_whitelabel.setObjectName("page2_top_whitelabel")

        # page #2 top letter label
        self.light_control_label = QtWidgets.QLabel(self.page_2)
        self.light_control_label.setGeometry(QtCore.QRect(20, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.light_control_label.setFont(font)
        self.light_control_label.setToolTipDuration(-1)
        self.light_control_label.setObjectName("light_control_label")

        #
        self.stackedWidget.addWidget(self.page_2)

        # page #3
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")

        # page #3 background label
        self.page3_background = QtWidgets.QLabel(self.page_3)
        self.page3_background.setGeometry(QtCore.QRect(0, 0, 1216, 655))
        self.page3_background.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.page3_background.setObjectName("page3_background")

        # page #3 top white label
        self.page3_top_whitelabel = QtWidgets.QLabel(self.page_3)
        self.page3_top_whitelabel.setGeometry(QtCore.QRect(0, 0, 1216, 61))
        self.page3_top_whitelabel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page3_top_whitelabel.setObjectName("page3_top_whitelabel")

        # page #3 top letter label
        self.account_label = QtWidgets.QLabel(self.page_3)
        self.account_label.setGeometry(QtCore.QRect(20, 10, 180, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.account_label.setFont(font)
        self.account_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.account_label.setObjectName("account_label")

        #
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(MainForm)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Form"))
        self.LightManager.setText(_translate("MainForm", "Light Manager"))
        self.system_overview_label.setText(_translate("MainForm", "시스템 현황"))
        self.light_status_label.setText(_translate("MainForm", "조명 상태"))
        self.light_control_label.setText(_translate("MainForm", "조명 제어"))
        self.account_label.setText(_translate("MainForm", "계정 관리"))

    def switch_layout_0(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_layout_1(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_layout_2(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_layout_3(self):
        self.stackedWidget.setCurrentIndex(3)

    def logout_main_page(self):
        self.show_logout_warning.emit()
