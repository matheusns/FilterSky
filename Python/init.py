from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_filter_sky
import sys

class Application (QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_filter_sky()
        self.ui.setupUi(self)

    def systemPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    

    def flowMainPage(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    def levelMainPage(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def pressureMainPage(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        
    def temperatureMainPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    av = Application()
    av.show()
    sys.exit(app.exec_())