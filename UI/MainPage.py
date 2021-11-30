from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PySide2.QtCore import QTimer
import datetime

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
        self.systemtimer = QTimer()
        self.systemtimer.start(1000)
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
        self.refresh_button = QtWidgets.QPushButton(self.page_0)
        self.refresh_button.setGeometry(QtCore.QRect(1160, 10, 41, 41))
        self.refresh_button.setStyleSheet("QPushButton{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/sync1.png);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(255, 255, 255, 0);\n"
                                      "border-image:url(UI/imgsource/sync2.png);\n"
                                      "}")
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.clicked.connect(self.update_date_update)

        # page #0 white background
        self.page0_white_background_2 = QtWidgets.QLabel(self.page_0)
        self.page0_white_background_2.setGeometry(QtCore.QRect(630, 90, 551, 261))
        self.page0_white_background_2.setStyleSheet("background-color:rgb(255,255,255);\n"
                                                    "border-radius : 12px;")
        self.page0_white_background_2.setText("")
        self.page0_white_background_2.setObjectName("page0_white_background_2")

        # page #0 white background
        self.page0_white_background_3 = QtWidgets.QLabel(self.page_0)
        self.page0_white_background_3.setGeometry(QtCore.QRect(630, 370, 551, 261))
        self.page0_white_background_3.setStyleSheet("background-color:rgb(255,255,255);\n"
                                                    "border-radius : 12px;")
        self.page0_white_background_3.setText("")
        self.page0_white_background_3.setObjectName("page0_white_background_3")

        # page #0 white background
        self.page0_white_background_1 = QtWidgets.QLabel(self.page_0)
        self.page0_white_background_1.setGeometry(QtCore.QRect(20, 90, 571, 541))
        self.page0_white_background_1.setStyleSheet("background-color:rgb(255,255,255);\n"
                                                    "border-radius : 12px;")
        self.page0_white_background_1.setText("")
        self.page0_white_background_1.setObjectName("page0_white_background_1")

        # page #0 light status text label
        self.light_status_text = QtWidgets.QLabel(self.page_0)
        self.light_status_text.setGeometry(QtCore.QRect(650, 105, 121, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.light_status_text.setFont(font)
        self.light_status_text.setObjectName("light_status_text")

        # page #0 light on image
        self.light_status_on_img = QtWidgets.QLabel(self.page_0)
        self.light_status_on_img.setGeometry(QtCore.QRect(730, 160, 111, 111))
        self.light_status_on_img.setPixmap(QtGui.QPixmap("UI/imgsource/bulb-on.png"))
        self.light_status_on_img.setScaledContents(True)
        self.light_status_on_img.setObjectName("light_status_on_img")

        # page #0 light off image
        self.light_status_off_img = QtWidgets.QLabel(self.page_0)
        self.light_status_off_img.setGeometry(QtCore.QRect(970, 153, 111, 111))
        self.light_status_off_img.setPixmap(QtGui.QPixmap("UI/imgsource/bulb-off.png"))
        self.light_status_off_img.setScaledContents(True)
        self.light_status_off_img.setObjectName("light_status_off_img")

        # page #0 light on text label
        self.light_status_on = QtWidgets.QLabel(self.page_0)
        self.light_status_on.setGeometry(QtCore.QRect(740, 290, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.light_status_on.setFont(font)
        self.light_status_on.setObjectName("light_status_on")

        # page #0 light off text label
        self.light_status_off = QtWidgets.QLabel(self.page_0)
        self.light_status_off.setGeometry(QtCore.QRect(980, 290, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.light_status_off.setFont(font)
        self.light_status_off.setObjectName("light_status_off")

        # page #0 light status separator
        self.light_status_separator = QtWidgets.QLabel(self.page_0)
        self.light_status_separator.setGeometry(QtCore.QRect(900, 150, 2, 160))
        self.light_status_separator.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.light_status_separator.setText("")
        self.light_status_separator.setObjectName("light_status_separator")

        # page #0 light on result label
        self.light_status_on_result = QtWidgets.QLabel(self.page_0)
        self.light_status_on_result.setGeometry(QtCore.QRect(810, 290, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.light_status_on_result.setFont(font)
        self.light_status_on_result.setObjectName("light_status_on_result")

        self.cursor.execute("select count(*) from light_setting where light_onoff = 'on';")
        self.result = self.cursor.fetchall()
        self.light_status_on_result.setText(str(self.result[0][0]))

        # page #0 light off result label
        self.light_status_off_result = QtWidgets.QLabel(self.page_0)
        self.light_status_off_result.setGeometry(QtCore.QRect(1050, 290, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.light_status_off_result.setFont(font)
        self.light_status_off_result.setObjectName("light_status_off_result")

        self.cursor.execute("select count(*) from light_setting where light_onoff = 'off';")
        self.result = self.cursor.fetchall()
        self.light_status_off_result.setText(str(self.result[0][0]))

        # page #0 anomaly detection text label
        self.anomaly_detection_text = QtWidgets.QLabel(self.page_0)
        self.anomaly_detection_text.setGeometry(QtCore.QRect(650, 385, 121, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.anomaly_detection_text.setFont(font)
        self.anomaly_detection_text.setObjectName("anomaly_detection_text")

        # page #0 anomaly detection normal image label
        self.normal_img = QtWidgets.QLabel(self.page_0)
        self.normal_img.setGeometry(QtCore.QRect(680, 440, 99, 99))
        self.normal_img.setText("")
        self.normal_img.setPixmap(QtGui.QPixmap("UI/imgsource/bulb-normal.png"))
        self.normal_img.setScaledContents(True)
        self.normal_img.setObjectName("normal_img")

        # page #0 anomaly detection old image label
        self.old_img = QtWidgets.QLabel(self.page_0)
        self.old_img.setGeometry(QtCore.QRect(850, 440, 99, 99))
        self.old_img.setText("")
        self.old_img.setPixmap(QtGui.QPixmap("UI/imgsource/bulb-old.png"))
        self.old_img.setScaledContents(True)
        self.old_img.setObjectName("old_img")

        # page #0 anomaly detection change image label
        self.change_img = QtWidgets.QLabel(self.page_0)
        self.change_img.setGeometry(QtCore.QRect(1030, 440, 99, 99))
        self.change_img.setText("")
        self.change_img.setPixmap(QtGui.QPixmap("UI/imgsource/bulb-change.png"))
        self.change_img.setScaledContents(True)
        self.change_img.setObjectName("change_img")

        # page #0 anomaly detection normal text label
        self.anomaly_detection_normal = QtWidgets.QLabel(self.page_0)
        self.anomaly_detection_normal.setGeometry(QtCore.QRect(680, 560, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.anomaly_detection_normal.setFont(font)
        self.anomaly_detection_normal.setObjectName("anomaly_detection_normal")

        # page #0 anomaly detection old text label
        self.anomaly_detection_old = QtWidgets.QLabel(self.page_0)
        self.anomaly_detection_old.setGeometry(QtCore.QRect(850, 560, 81, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.anomaly_detection_old.setFont(font)
        self.anomaly_detection_old.setObjectName("anomaly_detection_old")

        # page #0 anomaly detection change text label
        self.anomaly_detection_change = QtWidgets.QLabel(self.page_0)
        self.anomaly_detection_change.setGeometry(QtCore.QRect(1020, 560, 101, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.anomaly_detection_change.setFont(font)
        self.anomaly_detection_change.setObjectName("anomaly_detection_change")

        # page #0 anomaly detection separator 1
        self.anomaly_detection_separator_1 = QtWidgets.QLabel(self.page_0)
        self.anomaly_detection_separator_1.setGeometry(QtCore.QRect(810, 430, 2, 160))
        self.anomaly_detection_separator_1.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.anomaly_detection_separator_1.setText("")
        self.anomaly_detection_separator_1.setObjectName("anomaly_detection_separator_1")

        # page #0 anomaly detection separator 2
        self.anomaly_detection_separator_2 = QtWidgets.QLabel(self.page_0)
        self.anomaly_detection_separator_2.setGeometry(QtCore.QRect(990, 430, 2, 160))
        self.anomaly_detection_separator_2.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.anomaly_detection_separator_2.setText("")
        self.anomaly_detection_separator_2.setObjectName("anomaly_detection_separator_2")

        # page #0 anomaly detecton normal result label
        self.anomaly_detection_normal_result = QtWidgets.QLabel(self.page_0)
        self.anomaly_detection_normal_result.setGeometry(QtCore.QRect(740, 560, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.anomaly_detection_normal_result.setFont(font)
        self.anomaly_detection_normal_result.setText("")
        self.anomaly_detection_normal_result.setObjectName("anomaly_detection_normal_result")

        self.cursor.execute("select count(*) from light_status where light_stat = 'normal';")
        self.result = self.cursor.fetchall()
        self.anomaly_detection_normal_result.setText(str(self.result[0][0]))

        # page #0 anomaly detection old result label
        self.anomaly_detection_old_result = QtWidgets.QLabel(self.page_0)
        self.anomaly_detection_old_result.setGeometry(QtCore.QRect(930, 560, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.anomaly_detection_old_result.setFont(font)
        self.anomaly_detection_old_result.setText("")
        self.anomaly_detection_old_result.setObjectName("anomaly_detection_old_result")

        self.cursor.execute("select count(*) from light_status where light_stat = 'old';")
        self.result = self.cursor.fetchall()
        self.anomaly_detection_old_result.setText(str(self.result[0][0]))

        # page #0 anomaly detection change result label
        self.anomaly_detection_change_result = QtWidgets.QLabel(self.page_0)
        self.anomaly_detection_change_result.setGeometry(QtCore.QRect(1130, 560, 71, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.anomaly_detection_change_result.setFont(font)
        self.anomaly_detection_change_result.setText("")
        self.anomaly_detection_change_result.setObjectName("anomaly_detection_change_result")

        self.cursor.execute("select count(*) from light_status where light_stat = 'change';")
        self.result = self.cursor.fetchall()
        self.anomaly_detection_change_result.setText(str(self.result[0][0]))

        # page #0 result text label
        self.result_text_label = QtWidgets.QLabel(self.page_0)
        self.result_text_label.setGeometry(QtCore.QRect(50, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.result_text_label.setFont(font)
        self.result_text_label.setStyleSheet("font-color:rgb(157, 157, 157);")
        self.result_text_label.setObjectName("result_text_label")

        # page #0 update time label
        self.update_time_label = QtWidgets.QLabel(self.page_0)
        self.update_time_label.setGeometry(QtCore.QRect(220, 110, 351, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.update_time_label.setFont(font)
        self.update_time_label.setStyleSheet("color:rgb(157, 157, 157);")
        self.update_time_label.setObjectName("update_time_label")

        self.current_time = datetime.datetime.now()
        self.update_time_label.setText("업데이트 : "+
            str(self.current_time.year) + "-" + str(self.current_time.month) + "-" + str(self.current_time.day) + "  " + str(
                self.current_time.hour) +
            ":" + str(self.current_time.minute) + ":" + str(self.current_time.second))

        # page #0 update time / result separator
        self.update_separator = QtWidgets.QLabel(self.page_0)
        self.update_separator.setGeometry(QtCore.QRect(170, 112, 2, 31))
        self.update_separator.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.update_separator.setObjectName("update_separator")

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
        self.page1_white_background.setGeometry(QtCore.QRect(540, 160, 451, 451))
        self.page1_white_background.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "border-radius:12px;")
        self.page1_white_background.setObjectName("white_background")

        # page #1 light_list_label
        self.light_list_label = QtWidgets.QLabel(self.page_1)
        self.light_list_label.setGeometry(QtCore.QRect(550, 90, 241, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.light_list_label.setFont(font)
        self.light_list_label.setObjectName("light_list_label")

        # page #1 add_light_button
        self.add_light_button = QtWidgets.QPushButton(self.page_1)
        self.add_light_button.setGeometry(QtCore.QRect(1030, 160, 131, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
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
        self.delete_light_button.setGeometry(QtCore.QRect(1030, 230, 131, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
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
        self.change_light_button.setGeometry(QtCore.QRect(1030, 300, 131, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
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
        self.listWidget_light.setGeometry(QtCore.QRect(545, 165, 441, 441))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_light.setFont(font)
        self.listWidget_light.setStyleSheet("border-radius:1px;")
        self.listWidget_light.setObjectName("listWidget_light")
        self.listWidget_light.itemSelectionChanged.connect(self.on_change_light)

        self.cursor.execute("select * from light_list;")
        self.result = self.cursor.fetchall()

        for i in range(0, self.light_number):
            item = self.listWidget_light.item(i)
            self.listWidget_light.addItem(QListWidgetItem(str(self.result[i][0])))

        # page #1 light information text label
        self.light_information_label = QtWidgets.QLabel(self.page_1)
        self.light_information_label.setGeometry(QtCore.QRect(50, 90, 241, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.light_information_label.setFont(font)
        self.light_information_label.setObjectName("light_information_label")

        # page #1 background label
        self.page1_white_background_2 = QtWidgets.QLabel(self.page_1)
        self.page1_white_background_2.setGeometry(QtCore.QRect(40, 160, 451, 451))
        self.page1_white_background_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                    "border-radius:12px;")
        self.page1_white_background_2.setText("")
        self.page1_white_background_2.setObjectName("page1_white_background_2")

        # page #1 light id text label
        self.light_id_label = QtWidgets.QLabel(self.page_1)
        self.light_id_label.setGeometry(QtCore.QRect(70, 200, 131, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.light_id_label.setFont(font)
        self.light_id_label.setObjectName("light_id_label")

        # page #1 light location text label
        self.light_loc_label = QtWidgets.QLabel(self.page_1)
        self.light_loc_label.setGeometry(QtCore.QRect(70, 300, 131, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.light_loc_label.setFont(font)
        self.light_loc_label.setObjectName("light_loc_label")

        # page #1 light lux text label
        self.light_lux_label = QtWidgets.QLabel(self.page_1)
        self.light_lux_label.setGeometry(QtCore.QRect(70, 400, 131, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.light_lux_label.setFont(font)
        self.light_lux_label.setObjectName("light_lux_label")

        # page #1 light status text label
        self.light_status_label_2 = QtWidgets.QLabel(self.page_1)
        self.light_status_label_2.setGeometry(QtCore.QRect(70, 500, 131, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.light_status_label_2.setFont(font)
        self.light_status_label_2.setObjectName("light_status_label_2")

        # page #1 light id result label
        self.light_id_result = QtWidgets.QLabel(self.page_1)
        self.light_id_result.setGeometry(QtCore.QRect(220, 200, 251, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.light_id_result.setFont(font)
        self.light_id_result.setText("")
        self.light_id_result.setObjectName("light_id_result")

        # page #1 light location result label
        self.light_loc_result = QtWidgets.QLabel(self.page_1)
        self.light_loc_result.setGeometry(QtCore.QRect(220, 300, 251, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.light_loc_result.setFont(font)
        self.light_loc_result.setText("")
        self.light_loc_result.setObjectName("light_loc_result")

        # page #1 light lux result label
        self.light_lux_result = QtWidgets.QLabel(self.page_1)
        self.light_lux_result.setGeometry(QtCore.QRect(220, 400, 251, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.light_lux_result.setFont(font)
        self.light_lux_result.setText("")
        self.light_lux_result.setObjectName("light_lux_result")

        # page #1 light status result label
        self.light_status_result = QtWidgets.QLabel(self.page_1)
        self.light_status_result.setGeometry(QtCore.QRect(220, 500, 251, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.light_status_result.setFont(font)
        self.light_status_result.setText("")
        self.light_status_result.setObjectName("light_status_result")

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

        # page #2 white background
        self.page2_white_background = QtWidgets.QLabel(self.page_2)
        self.page2_white_background.setGeometry(QtCore.QRect(30, 90, 911, 521))
        self.page2_white_background.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "border-radius:12px;")
        self.page2_white_background.setText("")
        self.page2_white_background.setObjectName("page2_white_background")

        # page #2 listwidget_light_control
        self.listWidget_light_control = QtWidgets.QListWidget(self.page_2)
        self.listWidget_light_control.setGeometry(QtCore.QRect(40, 100, 891, 501))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget_light_control.setFont(font)
        self.listWidget_light_control.setStyleSheet("border-radius:1px;")
        self.listWidget_light_control.setObjectName("listWidget_light_control")
        self.listWidget_light_control.setViewMode(QtWidgets.QListWidget.IconMode)
        self.listWidget_light_control.setIconSize(QtCore.QSize(128, 128))



        self.cursor.execute("select * from light_setting;")
        self.result = self.cursor.fetchall()
        for i in range(0, self.light_number):
            if(self.result[i][2]=='on'):
                self.icon = QtGui.QIcon("UI/imgsource/bulb-normal.png")
                self.listWidget_light_control.addItem(QListWidgetItem(self.icon,str(self.result[i][0])))
            elif(self.result[i][2]=='off'):
                self.icon = QtGui.QIcon("UI/imgsource/bulb-normal-off.png")
                self.listWidget_light_control.addItem(QListWidgetItem(self.icon, str(self.result[i][0])))

        # page #2 light_control_button
        self.light_control_button = QtWidgets.QPushButton(self.page_2)
        self.light_control_button.setGeometry(QtCore.QRect(1000, 100, 171, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.light_control_button.setFont(font)
        self.light_control_button.setStyleSheet("QPushButton{\n"
                                              "background-color: rgb(53, 174, 255);\n"
                                              "border-radius:12px;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "background-color: rgb(153, 153, 153);\n"
                                              "border-radius:12px;\n"
                                              "}")
        self.light_control_button.setObjectName("light_control_button")
        self.light_control_button.clicked.connect(self.light_control)

        # page #2 set_timer_button
        self.set_timer_button = QtWidgets.QPushButton(self.page_2)
        self.set_timer_button.setGeometry(QtCore.QRect(1000, 170, 171, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.set_timer_button.setFont(font)
        self.set_timer_button.setStyleSheet("QPushButton{\n"
                                               "background-color: rgb(255, 237, 32);\n"
                                               "border-radius:12px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "background-color: rgb(153, 153, 153);\n"
                                               "border-radius:12px;\n"
                                               "}")
        self.set_timer_button.setObjectName("set_timer_button")
        self.set_timer_button.clicked.connect(self.light_control_timer)

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
        font.setBold(True)
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
        font.setBold(True)
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
        font.setBold(True)
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

        self.systemtimer.timeout.connect(self.on_change_light)
        self.systemtimer.timeout.connect(self.light_control_update)
        self.systemtimer.timeout.connect(self.overview_update)


        self.retranslateUi(MainForm)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "LightManager"))
        MainForm.setWindowIcon(QIcon("UI/imgsource/lightbulb.png"))
        self.LightManager.setText(_translate("MainForm", "Light Manager"))
        self.system_overview_label.setText(_translate("MainForm", "시스템 현황"))
        self.light_status_text.setText(_translate("MainForm", "조명 상태"))
        self.light_status_on.setText(_translate("MainForm", "켜짐 : "))
        self.light_status_off.setText(_translate("MainForm", "꺼짐 : "))
        self.anomaly_detection_text.setText(_translate("MainForm", "이상 감지"))
        self.anomaly_detection_normal.setText(_translate("MainForm", "정상 : "))
        self.anomaly_detection_old.setText(_translate("MainForm", "노후화 :"))
        self.anomaly_detection_change.setText(_translate("MainForm", "교체 필요 :"))
        self.result_text_label.setText(_translate("MainForm", "진단 결과"))
        self.light_status_label.setText(_translate("MainForm", "조명 관리"))
        self.light_control_label.setText(_translate("MainForm", "조명 제어"))
        self.listWidget_light_control.setSortingEnabled(False)
        self.light_control_button.setText(_translate("MainForm", "조명 켜기/끄기"))
        self.set_timer_button.setText(_translate("MainForm", "타이머 설정"))
        self.account_label.setText(_translate("MainForm", "계정 관리"))
        self.light_list_label.setText(_translate("MainForm", "조명 목록"))
        self.add_light_button.setText(_translate("MainForm", "조명 추가"))
        self.delete_light_button.setText(_translate("MainForm", "조명 삭제"))
        self.change_light_button.setText(_translate("MainForm", "정보 변경"))
        __sortingEnabled = self.listWidget_light.isSortingEnabled()
        self.listWidget_light.setSortingEnabled(False)
        self.light_information_label.setText(_translate("MainForm", "조명 정보"))
        self.light_id_label.setText(_translate("MainForm", "ID"))
        self.light_loc_label.setText(_translate("MainForm", "위치"))
        self.light_lux_label.setText(_translate("MainForm", "조도"))
        self.light_status_label_2.setText(_translate("MainForm", "상태"))
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
        row = self.listWidget_light.currentRow()
        if(row==-1):
            pass
        else:
            value = self.listWidget_light.currentItem().text()
            if(self.AUTH == 0):
                self.show_auth_warning_light.emit()
            else:
                query = "call delete_light("+str(value)+");"
                self.cursor.execute(query)
                self.listWidget_light.takeItem(row)

    def on_change_light(self):
        row = self.listWidget_light.currentRow()
        if(row == -1):
            pass
        else:
            value = self.listWidget_light.currentItem().text()
            self.light_id_result.setText(value)
            query = "select light_loc from light_list where light_id = " + value + ";"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.light_loc_result.setText(result[0][0])
            query = "select light_lux from light_status where light_list_id = " + value + ";"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            self.light_lux_result.setText(str(result[0][0]))
            procedure = "call take_light_status(" + value + ");"
            self.cursor.execute(procedure)
            result = self.cursor.fetchall()
            if (result[0][0] == "change"):
                self.light_status_result.setText("교체 필요")
            elif (result[0][0] == 'old'):
                self.light_status_result.setText("노후화됨")
            else:
                self.light_status_result.setText("정상")

    def light_control_update(self):
        row = self.listWidget_light_control.currentRow()
        if(row == -1):
            pass
        else:
            count = self.listWidget_light_control.count()
            for i in range(0,count):
                value = self.listWidget_light_control.item(i).text()
                query = "select light_onoff from light_setting where light_setting_id = "+str(value)+";"
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                if(result[0][0]=='on'):
                    self.listWidget_light_control.item(i).setIcon(QIcon("UI/imgsource/bulb-normal.png"))
                elif(result[0][0] == 'off'):
                    self.listWidget_light_control.item(i).setIcon(QIcon("UI/imgsource/bulb-normal-off.png"))

    def overview_update(self):
        self.cursor.execute("select count(*) from light_setting where light_onoff = 'on';")
        self.result = self.cursor.fetchall()
        self.light_status_on_result.setText(str(self.result[0][0]))

        self.cursor.execute("select count(*) from light_setting where light_onoff = 'off';")
        self.result = self.cursor.fetchall()
        self.light_status_off_result.setText(str(self.result[0][0]))

        self.cursor.execute("select count(*) from light_status where light_stat = 'normal';")
        self.result = self.cursor.fetchall()
        self.anomaly_detection_normal_result.setText(str(self.result[0][0]))

        self.cursor.execute("select count(*) from light_status where light_stat = 'old';")
        self.result = self.cursor.fetchall()
        self.anomaly_detection_old_result.setText(str(self.result[0][0]))

        self.cursor.execute("select count(*) from light_status where light_stat = 'change';")
        self.result = self.cursor.fetchall()
        self.anomaly_detection_change_result.setText(str(self.result[0][0]))
        self.current_time = datetime.datetime.now()

    def update_date_update(self):
        self.update_time_label.setText("업데이트 : " +
                                       str(self.current_time.year) + "-" + str(self.current_time.month) + "-" + str(
            self.current_time.day) + "  " + str(
            self.current_time.hour) +
                                       ":" + str(self.current_time.minute) + ":" + str(self.current_time.second))
        self.overview_update()


    def light_control(self):
        row = self.listWidget_light_control.currentRow()
        if(row==-1):
            pass
        else:
            value = self.listWidget_light_control.currentItem().text()
            query = "select * from light_setting where light_setting_id = "+str(value)+";"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if(result[0][2] == 'on'):
                query = "update light_setting set light_onoff = 'off' where light_setting_id ="+str(value)+";"
                self.cursor.execute(query)
                self.listWidget_light_control.item(row).setIcon(QIcon("UI/imgsource/bulb-normal-off.png"))
            elif (result[0][2] == 'off'):
                query = "update light_setting set light_onoff = 'on' where light_setting_id =" + str(value) + ";"
                self.cursor.execute(query)
                self.listWidget_light_control.item(row).setIcon(QIcon("UI/imgsource/bulb-normal.png"))

    def light_control_timer(self):
        row = self.listWidget_light_control.currentRow()
        if (row == -1):
            pass
        else:
            text, ok = QInputDialog.getInt(self, 'Timer', '시간을 입력하세요 (단위 : 초)   ')

            if ok:
                time_value = text
                if(time_value < 0):
                    pass
                else:
                    value = self.listWidget_light_control.currentItem().text()
                    query = "select * from light_setting where light_setting_id = " + str(value) + ";"
                    self.cursor.execute(query)
                    result = self.cursor.fetchall()
                    query = "update light_setting set light_timer = " + str(time_value) + " where light_setting_id = " + str(
                        value) + ";"
                    self.cursor.execute(query)



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
        row = self.listWidget_account.currentRow()
        if(row==-1):
            pass
        else:
            value = self.listWidget_account.currentItem().text()
            if (self.AUTH == 0):
                self.show_auth_warning_account.emit()
            elif (self.loginID == value):
                self.show_account_delete_warning.emit()
            else:
                query = "delete from id_table where user_id = '" + value + "';"
                self.cursor.execute(query)
                self.listWidget_account.takeItem(row)

    def auth_control(self):
        row = self.listWidget_account.currentRow()
        if(row==-1):
            pass
        else:
            value = self.listWidget_account.currentItem().text()
            query = "select * from id_table where user_id ='" + value + "';"
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            AUTHvalue = result[0][4]

            if (self.AUTH == 1) and (AUTHvalue < 1):
                query = "update id_table set user_auth = 1 where user_id = '" + value + "';"
                self.cursor.execute(query)
                self.auth_result.setText("관리자")
            else:
                self.show_auth_check.emit()

