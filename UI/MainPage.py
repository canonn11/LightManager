from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Main_Page(QWidget):
    show_logout_warning = QtCore.pyqtSignal()
    show_add_account_page = QtCore.pyqtSignal()
    show_auth_warning_account = QtCore.pyqtSignal()
    show_auth_warning_light = QtCore.pyqtSignal()
    show_auth_check = QtCore.pyqtSignal()
    show_account_delete_warning = QtCore.pyqtSignal()
    show_add_light_page = QtCore.pyqtSignal()
    add_update = QtCore.pyqtSignal()
    add_update_light = QtCore.pyqtSignal()
    account_number = 0
    light_number = 0

    def setupUi(self, MainForm):
        self.cursor.execute("select count(*) from id_table;")
        self.result = self.cursor.fetchone()
        self.account_number = self.result[0]

        self.cursor.execute("select count(*) from light_list;")
        self.result = self.cursor.fetchone()
        self.light_number = self.result[0]

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

        # Left side Pushbutton #2 -> Light Management Button
        self.LightButton = QtWidgets.QPushButton(MainForm)
        self.LightButton.setGeometry(QtCore.QRect(6, 80, 51, 51))
        self.LightButton.setStyleSheet("QPushButton{\n"
                                       "background-color: rgba(255, 255, 255, 0);\n"
                                       "border-image:url(UI/imgsource/bulb1.png);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgba(255, 255, 255, 0);\n"
                                       "border-image:url(UI/imgsource/bulb2.png);\n"
                                       "}")
        self.LightButton.setObjectName("LightButton")
        self.LightButton.clicked.connect(self.switch_layout_1)

        # Left side Pushbutton #3 -> LightControl Button
        self.LightControlButton = QtWidgets.QPushButton(MainForm)
        self.LightControlButton.setGeometry(QtCore.QRect(6, 150, 51, 51))
        self.LightControlButton.setStyleSheet("QPushButton{\n"
                                                      "background-color: rgba(255, 255, 255, 0);\n"
                                                      "border-image:url(UI/imgsource/folder1.png);\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "background-color: rgba(255, 255, 255, 0);\n"
                                                      "border-image:url(UI/imgsource/folder2.png);\n"
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

        # Left side Pushbutton #5 -> Logout Button
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
        self.system_overview_label.setGeometry(QtCore.QRect(20, 13, 181, 31))
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
        self.light_status_label.setGeometry(QtCore.QRect(20, 13, 181, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.light_status_label.setFont(font)
        self.light_status_label.setObjectName("light_status_label")

        # page #1 white background label
        self.page1_white_background = QtWidgets.QLabel(self.page_1)
        self.page1_white_background.setGeometry(QtCore.QRect(40, 140, 881, 471))
        self.page1_white_background.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-radius:12px;")
        self.page1_white_background.setObjectName("white_background")

        # page #1 light_list_label
        self.light_list_label = QtWidgets.QLabel(self.page_1)
        self.light_list_label.setGeometry(QtCore.QRect(40, 75, 241, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.light_list_label.setFont(font)
        self.light_list_label.setObjectName("light_list_label")

        # page #1 add_light_button
        self.add_light_button = QtWidgets.QPushButton(self.page_1)
        self.add_light_button.setGeometry(QtCore.QRect(970, 140, 171, 61))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.add_light_button.setFont(font)
        self.add_light_button.setStyleSheet("QPushButton{\n"
                                              "background-color: rgb(53, 174, 255);\n"
                                              "border-radius:12px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgb(153, 153, 153);\n"
                                              "border-radius:12px;\n"
                                              "}")
        self.add_light_button.setObjectName("add_light_button")
        self.add_light_button.clicked.connect(self.add_light_page)



        # page #1 delete_light_button
        self.delete_light_button = QtWidgets.QPushButton(self.page_1)
        self.delete_light_button.setGeometry(QtCore.QRect(970, 220, 171, 61))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.delete_light_button.setFont(font)
        self.delete_light_button.setStyleSheet("QPushButton{\n"
                                                 "background-color: rgb(255, 126, 128);\n"
                                                 "border-radius:12px;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "background-color: rgb(153, 153, 153);\n"
                                                 "border-radius:12px;\n"
                                                 "}")
        self.delete_light_button.setObjectName("delete_light_button")
        self.delete_light_button.clicked.connect(self.delete_light)

        # page #1 change_light_button
        self.change_light_button = QtWidgets.QPushButton(self.page_1)
        self.change_light_button.setGeometry(QtCore.QRect(970, 300, 171, 61))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.change_light_button.setFont(font)
        self.change_light_button.setStyleSheet("QPushButton{\n"
                                               "background-color: rgb(255, 237, 32);\n"
                                               "border-radius:12px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "background-color: rgb(153, 153, 153);\n"
                                               "border-radius:12px;\n"
                                               "}")
        self.change_light_button.setObjectName("change_light_button")

        # page #1 listwidget _ light
        self.listWidget_light = QtWidgets.QListWidget(self.page_1)
        self.listWidget_light.setGeometry(QtCore.QRect(50, 150, 861, 451))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_light.setFont(font)
        self.listWidget_light.setStyleSheet("border-radius:1px;")
        self.listWidget_light.setObjectName("listWidget_light")

        self.cursor.execute("select * from light_list;")
        self.result = self.cursor.fetchall()

        for i in range(0, self.light_number):
            item = self.listWidget_light.item(i)
            self.listWidget_light.addItem(QListWidgetItem(str(self.result[i][0])))

        #
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
        self.light_control_label.setGeometry(QtCore.QRect(20, 13, 181, 31))
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
        self.account_label.setGeometry(QtCore.QRect(20, 13, 180, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.account_label.setFont(font)
        self.account_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.account_label.setObjectName("account_label")

        # page #3 white background 1
        self.white_background_1 = QtWidgets.QLabel(self.page_3)
        self.white_background_1.setGeometry(QtCore.QRect(40, 160, 451, 451))
        self.white_background_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-radius:12px;")
        self.white_background_1.setObjectName("white_background_1")

        # page #3 white background 2
        self.white_background_2 = QtWidgets.QLabel(self.page_3)
        self.white_background_2.setGeometry(QtCore.QRect(540, 160, 451, 451))
        self.white_background_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-radius:12px;")
        self.white_background_2.setObjectName("white_background_2")

        # page #3 account listwidget
        self.listWidget_account = QtWidgets.QListWidget(self.page_3)
        self.listWidget_account.setGeometry(QtCore.QRect(545, 165, 441, 441))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_account.setFont(font)
        self.listWidget_account.setStyleSheet("border-radius:1px;")
        self.listWidget_account.setObjectName("listWidget_account")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        item.setFont(font)
        self.listWidget_account.itemSelectionChanged.connect(self.on_change_account)

        self.cursor.execute("select * from id_table;")
        self.result = self.cursor.fetchall()

        for i in range(0, self.account_number):
            item = self.listWidget_account.item(i)
            self.listWidget_account.addItem(QListWidgetItem(self.result[i][0]))

        # page #3 all acount text label
        self.all_account_label = QtWidgets.QLabel(self.page_3)
        self.all_account_label.setGeometry(QtCore.QRect(550, 90, 241, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.all_account_label.setFont(font)
        self.all_account_label.setObjectName("all_account_label")

        # page #3 account info text label
        self.account_info_label = QtWidgets.QLabel(self.page_3)
        self.account_info_label.setGeometry(QtCore.QRect(50, 90, 241, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.account_info_label.setFont(font)
        self.account_info_label.setObjectName("account_info_label")

        # page #3 add account button
        self.add_account_button = QtWidgets.QPushButton(self.page_3)
        self.add_account_button.setGeometry(QtCore.QRect(1030, 160, 131, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.add_account_button.setFont(font)
        self.add_account_button.setStyleSheet("QPushButton{\n"
                                                "background-color: rgb(53, 174, 255);\n"
                                                "border-radius:12px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "background-color: rgb(153, 153, 153);\n"
                                                "border-radius:12px;\n"
                                                "}")
        self.add_account_button.setObjectName("add_account_button")
        self.add_account_button.clicked.connect(self.add_account_page)

        # page #3 delete account button
        self.delete_account_button = QtWidgets.QPushButton(self.page_3)
        self.delete_account_button.setGeometry(QtCore.QRect(1030, 230, 131, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.delete_account_button.setFont(font)
        self.delete_account_button.setStyleSheet("QPushButton{\n"
                                              "background-color: rgb(255, 126, 128);\n"
                                              "border-radius:12px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgb(153, 153, 153);\n"
                                              "border-radius:12px;\n"
                                              "}")
        self.delete_account_button.setObjectName("delete_account_button")
        self.delete_account_button.clicked.connect(self.delete_account)

        # page #3 auth control button
        self.auth_control_button = QtWidgets.QPushButton(self.page_3)
        self.auth_control_button.setGeometry(QtCore.QRect(1030, 300, 131, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.auth_control_button.setFont(font)
        self.auth_control_button.setStyleSheet("QPushButton{\n"
                                                 "background-color: rgb(255, 237, 32);\n"
                                                 "border-radius:12px;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "background-color: rgb(153, 153, 153);\n"
                                                 "border-radius:12px;\n"
                                                 "}")
        self.auth_control_button.setObjectName("auth_control_button")
        self.auth_control_button.clicked.connect(self.auth_control)

        # page #3 id text label
        self.id_label = QtWidgets.QLabel(self.page_3)
        self.id_label.setGeometry(QtCore.QRect(70, 200, 131, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.id_label.setFont(font)
        self.id_label.setObjectName("id_label")


        # page #3 name text label
        self.name_label = QtWidgets.QLabel(self.page_3)
        self.name_label.setGeometry(QtCore.QRect(70, 300, 131, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")

        # page #3 location text label
        self.loc_label = QtWidgets.QLabel(self.page_3)
        self.loc_label.setGeometry(QtCore.QRect(70, 400, 131, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.loc_label.setFont(font)
        self.loc_label.setObjectName("loc_label")

        # page #3 auth text label
        self.auth_label = QtWidgets.QLabel(self.page_3)
        self.auth_label.setGeometry(QtCore.QRect(70, 500, 131, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.auth_label.setFont(font)
        self.auth_label.setObjectName("auth_label")

        # page #3 id result label
        self.id_result = QtWidgets.QLabel(self.page_3)
        self.id_result.setGeometry(QtCore.QRect(220, 200, 251, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.id_result.setFont(font)
        self.id_result.setObjectName("id_result")

        # page #3 name result label
        self.name_result = QtWidgets.QLabel(self.page_3)
        self.name_result.setGeometry(QtCore.QRect(220, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.name_result.setFont(font)
        self.name_result.setText("")
        self.name_result.setObjectName("name_result")

        # page #3 location result label
        self.loc_result = QtWidgets.QLabel(self.page_3)
        self.loc_result.setGeometry(QtCore.QRect(220, 400, 251, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.loc_result.setFont(font)
        self.loc_result.setText("")
        self.loc_result.setObjectName("loc_result")

        # page #3 auth result label
        self.auth_result = QtWidgets.QLabel(self.page_3)
        self.auth_result.setGeometry(QtCore.QRect(220, 500, 251, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.auth_result.setFont(font)
        self.auth_result.setText("")
        self.auth_result.setObjectName("auth_result")

        #
        self.stackedWidget.addWidget(self.page_3)

        self.retranslateUi(MainForm)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "LightManager"))
        MainForm.setWindowIcon(QIcon("UI/imgsource/lightbulb.png"))
        self.LightManager.setText(_translate("MainForm", "Light Manager"))
        self.system_overview_label.setText(_translate("MainForm", "시스템 현황"))
        self.light_status_label.setText(_translate("MainForm", "조명 관리"))
        self.light_control_label.setText(_translate("MainForm", "조명 제어"))
        self.account_label.setText(_translate("MainForm", "계정 관리"))
        self.light_list_label.setText(_translate("Form", "조명 목록"))
        self.add_light_button.setText(_translate("Form", "조명 추가"))
        self.delete_light_button.setText(_translate("Form", "조명 삭제"))
        self.change_light_button.setText(_translate("Form", "정보 변경"))
        __sortingEnabled = self.listWidget_light.isSortingEnabled()
        self.listWidget_light.setSortingEnabled(False)
        __sortingEnabled = self.listWidget_account.isSortingEnabled()
        self.listWidget_account.setSortingEnabled(False)
        self.listWidget_account.setSortingEnabled(__sortingEnabled)
        self.all_account_label.setText(_translate("MainForm", "전체 계정"))
        self.account_info_label.setText(_translate("MainForm", "계정 정보"))
        self.add_account_button.setText(_translate("MainForm", "계정 추가"))
        self.delete_account_button.setText(_translate("MainForm", "계정 삭제"))
        self.auth_control_button.setText(_translate("MainForm", "등급 제어"))
        self.id_label.setText(_translate("MainForm", "ID"))
        self.name_label.setText(_translate("MainForm", "이름"))
        self.loc_label.setText(_translate("MainForm", "위치"))
        self.auth_label.setText(_translate("MainForm", "권한"))

    def add_light_page(self):
        if(self.AUTH == 1):
            self.show_add_light_page.emit()
        else:
            self.show_auth_warning_light.emit()

    def add_account_page(self):
        if(self.AUTH == 1):
            self.show_add_account_page.emit()
        else:
            self.show_auth_warning_account.emit()

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

    def add_list_update_account(self):
        self.listWidget_account.addItem(QListWidgetItem(self.ID))
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(3)

    def add_list_update_light(self):
        self.listWidget_light.addItem(QListWidgetItem(str(self.lightID)))
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)

    def delete_light(self):
        value = self.listWidget_light.currentItem().text()
        row = self.listWidget_light.currentRow()
        if(row==-1):
            pass
        else:
            if(self.AUTH == 0):
                self.show_auth_warning_light.emit()
            else:
                query = "call delete_light("+str(value)+");"
                self.cursor.execute(query)
                self.listWidget_light.takeItem(row)


    def on_change_account(self):
        value = self.listWidget_account.currentItem().text()
        query = "select * from id_table where user_id ='"+value+"';"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.id_result.setText(result[0][0])
        self.name_result.setText(result[0][2])
        self.loc_result.setText(result[0][3])
        if(result[0][4] == 1):
            self.auth_result.setText("관리자")
        else:
            self.auth_result.setText("유저")

    def delete_account(self):
        value = self.listWidget_account.currentItem().text()
        row = self.listWidget_account.currentRow()
        if(row==-1):
            pass
        else:
            if(self.AUTH == 0):
                self.show_auth_warning_account.emit()
            elif(self.loginID == value):
                self.show_account_delete_warning.emit()
            else:
                query = "delete from id_table where user_id = '"+value+"';"
                self.cursor.execute(query)
                self.listWidget_account.takeItem(row)

    def auth_control(self):
        value = self.listWidget_account.currentItem().text()
        query = "select * from id_table where user_id ='"+value+"';"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        AUTHvalue = result[0][4]

        if(self.AUTH ==1) and (AUTHvalue<1):
            query = "update id_table set user_auth = 1 where user_id = '"+value+"';"
            self.cursor.execute(query)
            self.auth_result.setText("관리자")
        else:
            self.show_auth_check.emit()