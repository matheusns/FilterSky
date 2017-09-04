from PyQt5 import QtCore, QtGui, QtWidgets
from systemdefinition import Ui_SystemDefinition
from tfdefinition import Ui_TfDefinition
from gui import Ui_filter_sky
from enum import Enum
import sys

class Application (QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_filter_sky()
        self.ui2 = Ui_SystemDefinition()
        self.ui3 = Ui_TfDefinition()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.Screens = Enum('Screens','Main')

    def systemPage(self):
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(2)
   
    def flowMainPage(self):
        self.ui2.setupUi(self)
        self.ui2.title.setText("MALHA DE VAZÃO")
        self.ui2.stackedWidget.setCurrentIndex(2)

    def levelMainPage(self):
        self.ui2.setupUi(self)
        self.ui2.title.setText("MALHA DE NÍVEL")
        self.ui2.stackedWidget.setCurrentIndex(1)

    def pressureMainPage(self):
        self.ui2.setupUi(self)
        self.ui2.title.setText("MALHA DE PRESSÃO")
        self.ui2.stackedWidget.setCurrentIndex(3)
        
    def temperatureMainPage(self):
        self.ui2.setupUi(self)
        self.ui2.title.setText("MALHA DE TEMPERATURA")
        self.ui2.stackedWidget.setCurrentIndex(0)
    
    def sfBackButton(self):
        self.systemPage()            

    def sfSettingsButton(self):
        print("Entrei Settings Button")

    def sfGraphButton(self):
        print("Entrei Graph Button")
        
    def sfTfButton(self):
        if(self.ui2.stackedWidget.currentIndex()==0):
            self.ui3.setupUi(self)
            self.ui3.title.setText("DEFINIÇAO DAS FUNÇÕES DE TRANSFERENCIA\n DOS ELEMENTOS DA MALHA DE TEMPERATURA")
            self.ui3.stackedWidget.setCurrentIndex(0)

        if(self.ui2.stackedWidget.currentIndex()==1):
            self.ui3.setupUi(self)
            self.ui3.title.setText("DEFINIÇAO DAS FUNÇÕES DE TRANSFERENCIA\n DOS ELEMENTOS DA MALHA DE TEMPERATURA")
            self.ui3.stackedWidget.setCurrentIndex(1)

        if(self.ui2.stackedWidget.currentIndex()==2):
            self.ui3.setupUi(self)
            self.ui3.title.setText("DEFINIÇAO DAS FUNÇÕES DE TRANSFERENCIA\n DOS ELEMENTOS DA MALHA DE TEMPERATURA")
            self.ui3.stackedWidget.setCurrentIndex(2)

        if(self.ui2.stackedWidget.currentIndex()==3):
            self.ui3.setupUi(self)
            self.ui3.title.setText("DEFINIÇAO DAS FUNÇÕES DE TRANSFERENCIA\n DOS ELEMENTOS DA MALHA DE PRESSÃO")
            self.ui3.stackedWidget.setCurrentIndex(3)
        
    
    def sfFilterButton(self):
        print("Entrei Filter Button")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    av = Application()
    av.show()
    sys.exit(app.exec_())