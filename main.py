from UIhandler import UIHandler
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
ui_handler = UIHandler()
ui_handler.show_login_page()
sys.exit(app.exec_())