# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../System_Definition/systemdefinition.ui'
#
# Created: Thu Sep 21 12:36:52 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SystemDefinition(object):
    def setupUi(self, SystemDefinition):
        SystemDefinition.setObjectName("SystemDefinition")
        SystemDefinition.resize(689, 682)
        SystemDefinition.setMaximumSize(QtCore.QSize(689, 682))
        self.centralWidget = QtWidgets.QWidget(SystemDefinition)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Temperature_Page = QtWidgets.QWidget()
        self.Temperature_Page.setObjectName("Temperature_Page")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.Temperature_Page)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textBrowser = QtWidgets.QTextBrowser(self.Temperature_Page)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_11.addWidget(self.textBrowser)
        self.frame_9 = QtWidgets.QFrame(self.Temperature_Page)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 291))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.label_16 = QtWidgets.QLabel(self.frame_9)
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/icons/malha_temperatura.jpg"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_11.addWidget(self.frame_9)
        self.gridLayout_22.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Temperature_Page)
        self.Level_Page = QtWidgets.QWidget()
        self.Level_Page.setObjectName("Level_Page")
        self.gridLayout_49 = QtWidgets.QGridLayout(self.Level_Page)
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.Level_Page)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.gridLayout_49.addWidget(self.textBrowser_8, 0, 0, 1, 1)
        self.frame_52 = QtWidgets.QFrame(self.Level_Page)
        self.frame_52.setMaximumSize(QtCore.QSize(16777215, 291))
        self.frame_52.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.frame_52)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem2)
        self.label_63 = QtWidgets.QLabel(self.frame_52)
        self.label_63.setText("")
        self.label_63.setPixmap(QtGui.QPixmap(":/icons/malha_nivel.png"))
        self.label_63.setScaledContents(True)
        self.label_63.setObjectName("label_63")
        self.horizontalLayout_38.addWidget(self.label_63)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem3)
        self.gridLayout_49.addWidget(self.frame_52, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.Level_Page)
        self.Flow_Page = QtWidgets.QWidget()
        self.Flow_Page.setObjectName("Flow_Page")
        self.gridLayout_48 = QtWidgets.QGridLayout(self.Flow_Page)
        self.gridLayout_48.setObjectName("gridLayout_48")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.Flow_Page)
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.gridLayout_48.addWidget(self.textBrowser_13, 0, 0, 1, 1)
        self.frame_83 = QtWidgets.QFrame(self.Flow_Page)
        self.frame_83.setMaximumSize(QtCore.QSize(16777215, 291))
        self.frame_83.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_83.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_83.setObjectName("frame_83")
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout(self.frame_83)
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_77.addItem(spacerItem4)
        self.label_125 = QtWidgets.QLabel(self.frame_83)
        self.label_125.setText("")
        self.label_125.setPixmap(QtGui.QPixmap(":/icons/malha_vazao.png"))
        self.label_125.setScaledContents(True)
        self.label_125.setObjectName("label_125")
        self.horizontalLayout_77.addWidget(self.label_125)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_77.addItem(spacerItem5)
        self.gridLayout_48.addWidget(self.frame_83, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.Flow_Page)
        self.Pressure_Page = QtWidgets.QWidget()
        self.Pressure_Page.setObjectName("Pressure_Page")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.Pressure_Page)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.frame_43 = QtWidgets.QFrame(self.Pressure_Page)
        self.frame_43.setMaximumSize(QtCore.QSize(16777215, 291))
        self.frame_43.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_43)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem6)
        self.label_60 = QtWidgets.QLabel(self.frame_43)
        self.label_60.setText("")
        self.label_60.setPixmap(QtGui.QPixmap(":/icons/malha_pressao.png"))
        self.label_60.setScaledContents(True)
        self.label_60.setObjectName("label_60")
        self.horizontalLayout_37.addWidget(self.label_60)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem7)
        self.gridLayout_23.addWidget(self.frame_43, 3, 0, 1, 1)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.Pressure_Page)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.gridLayout_23.addWidget(self.textBrowser_7, 1, 0, 2, 1)
        self.stackedWidget.addWidget(self.Pressure_Page)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.title = QtWidgets.QLabel(self.centralWidget)
        self.title.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans Demi Cond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setText("MALHA DE TEMPERATURA")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout_2.addWidget(self.title, 0, 0, 1, 3)
        self.frame_50 = QtWidgets.QFrame(self.centralWidget)
        self.frame_50.setMaximumSize(QtCore.QSize(100, 589))
        self.frame_50.setStyleSheet("")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_50)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filterButton = QtWidgets.QPushButton(self.frame_50)
        self.filterButton.setEnabled(True)
        self.filterButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/tools-and-utensils.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filterButton.setIcon(icon)
        self.filterButton.setIconSize(QtCore.QSize(48, 48))
        self.filterButton.setFlat(True)
        self.filterButton.setObjectName("filterButton")
        self.verticalLayout.addWidget(self.filterButton)
        self.tfButton = QtWidgets.QPushButton(self.frame_50)
        self.tfButton.setEnabled(True)
        self.tfButton.setToolTipDuration(-2)
        self.tfButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/transfer_function.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tfButton.setIcon(icon1)
        self.tfButton.setIconSize(QtCore.QSize(48, 48))
        self.tfButton.setFlat(True)
        self.tfButton.setObjectName("tfButton")
        self.verticalLayout.addWidget(self.tfButton)
        self.graphButton = QtWidgets.QPushButton(self.frame_50)
        self.graphButton.setEnabled(False)
        self.graphButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/graphs.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.graphButton.setIcon(icon2)
        self.graphButton.setIconSize(QtCore.QSize(48, 48))
        self.graphButton.setFlat(True)
        self.graphButton.setObjectName("graphButton")
        self.verticalLayout.addWidget(self.graphButton)
        self.settingsButton = QtWidgets.QPushButton(self.frame_50)
        self.settingsButton.setEnabled(True)
        self.settingsButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsButton.setIcon(icon3)
        self.settingsButton.setIconSize(QtCore.QSize(48, 48))
        self.settingsButton.setFlat(True)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout.addWidget(self.settingsButton)
        self.backButton = QtWidgets.QPushButton(self.frame_50)
        self.backButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/reply.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backButton.setIcon(icon4)
        self.backButton.setIconSize(QtCore.QSize(48, 48))
        self.backButton.setFlat(True)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.gridLayout_2.addWidget(self.frame_50, 1, 2, 1, 1)
        SystemDefinition.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(SystemDefinition)
        self.statusBar.setObjectName("statusBar")
        SystemDefinition.setStatusBar(self.statusBar)

        self.retranslateUi(SystemDefinition)
        self.stackedWidget.setCurrentIndex(0)
        self.backButton.clicked.connect(SystemDefinition.sfBackButton)
        self.settingsButton.clicked.connect(SystemDefinition.sfSettingsButton)
        self.graphButton.clicked.connect(SystemDefinition.sfGraphButton)
        self.filterButton.clicked.connect(SystemDefinition.sfFilterButton)
        self.tfButton.clicked.connect(SystemDefinition.sfTfButton)
        QtCore.QMetaObject.connectSlotsByName(SystemDefinition)

    def retranslateUi(self, SystemDefinition):
        _translate = QtCore.QCoreApplication.translate
        SystemDefinition.setWindowTitle(_translate("SystemDefinition", "FilterSky"))
        self.textBrowser.setHtml(_translate("SystemDefinition", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">O diagrama P&amp;ID a seguir ilustra os componentes encontrados na malha de temperatura da estação compacta da FESTO para experimentos em controle de processos. Na indústria, o controle da temperatura de determinados  recepientes e substâncias, é essencial durante o processo de fabricação e produção.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">A temperatura é uma grandeza de dinâmica lenta, ou seja, depende de uma quantidade de tempo maior, em relação a grandezas como vazão e nível, para mudar seu estado. A utlização de filtros digitais minimiza a ação de possíveis ruídos, provenientes da temperatura de outros ambientes, que possam alterar o valor do estado atual do sistema, podendo prejudicar o desempenho do processo em geral.  </span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> </span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("SystemDefinition", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">MALHA DE NÍVEL:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WKSKSLFJSKFSJFKSSSSSSSFKFJSKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKFJFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFSKFJSKFJSKFJSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSKSFJKSFJKSJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJKFJSKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK</p></body></html>"))
        self.textBrowser_13.setHtml(_translate("SystemDefinition", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">MALHA DE VAZÃO:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WKSKSLFJSKFSJFKSSSSSSSFKFJSKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKFJFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFSKFJSKFJSKFJSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSKSFJKSFJKSJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJKFJSKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK</p></body></html>"))
        self.textBrowser_7.setHtml(_translate("SystemDefinition", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">MALHA DE PRESSÃO:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WKSKSLFJSKFSJFKSSSSSSSFKFJSKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKFJFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFSKFJSKFJSKFJSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSKSFJKSFJKSJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJKFJSKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK</p></body></html>"))
        self.tfButton.setToolTip(_translate("SystemDefinition", "<html><head/><body><p>Função de Transferência</p></body></html>"))

import filter_rc
