# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Tf_Definition/tfdefinition.ui'
#
# Created: Thu Sep 21 12:36:52 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TfDefinition(object):
    def setupUi(self, TfDefinition):
        TfDefinition.setObjectName("TfDefinition")
        TfDefinition.resize(689, 682)
        TfDefinition.setMaximumSize(QtCore.QSize(689, 682))
        self.centralWidget = QtWidgets.QWidget(TfDefinition)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Blocks_Temperature = QtWidgets.QWidget()
        self.Blocks_Temperature.setObjectName("Blocks_Temperature")
        self.gridLayout_53 = QtWidgets.QGridLayout(self.Blocks_Temperature)
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.frame_12 = QtWidgets.QFrame(self.Blocks_Temperature)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_12)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/hand-pump.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_28.setIcon(icon)
        self.pushButton_28.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_28.setFlat(True)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_6.addWidget(self.pushButton_28, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_12)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/valve.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_6.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_12)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/floor.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_29.setIcon(icon2)
        self.pushButton_29.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_29.setFlat(True)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_6.addWidget(self.pushButton_29, 0, 2, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_31.setIcon(icon1)
        self.pushButton_31.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_31.setFlat(True)
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_6.addWidget(self.pushButton_31, 2, 1, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_12)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/gamepad.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_30.setIcon(icon3)
        self.pushButton_30.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_30.setFlat(True)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_6.addWidget(self.pushButton_30, 1, 2, 1, 1)
        self.gridLayout_53.addWidget(self.frame_12, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.Blocks_Temperature)
        self.Blocks_Level = QtWidgets.QWidget()
        self.Blocks_Level.setObjectName("Blocks_Level")
        self.gridLayout_50 = QtWidgets.QGridLayout(self.Blocks_Level)
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.frame_85 = QtWidgets.QFrame(self.Blocks_Level)
        self.frame_85.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_85.setObjectName("frame_85")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.frame_85)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.pushButton_228 = QtWidgets.QPushButton(self.frame_85)
        self.pushButton_228.setIcon(icon3)
        self.pushButton_228.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_228.setFlat(True)
        self.pushButton_228.setObjectName("pushButton_228")
        self.gridLayout_21.addWidget(self.pushButton_228, 2, 2, 1, 1)
        self.pushButton_224 = QtWidgets.QPushButton(self.frame_85)
        self.pushButton_224.setIcon(icon2)
        self.pushButton_224.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_224.setFlat(True)
        self.pushButton_224.setObjectName("pushButton_224")
        self.gridLayout_21.addWidget(self.pushButton_224, 1, 2, 1, 1)
        self.pushButton_225 = QtWidgets.QPushButton(self.frame_85)
        self.pushButton_225.setIcon(icon)
        self.pushButton_225.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_225.setFlat(True)
        self.pushButton_225.setObjectName("pushButton_225")
        self.gridLayout_21.addWidget(self.pushButton_225, 2, 1, 1, 1)
        self.pushButton_226 = QtWidgets.QPushButton(self.frame_85)
        self.pushButton_226.setIcon(icon1)
        self.pushButton_226.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_226.setFlat(True)
        self.pushButton_226.setObjectName("pushButton_226")
        self.gridLayout_21.addWidget(self.pushButton_226, 1, 1, 1, 1)
        self.pushButton_227 = QtWidgets.QPushButton(self.frame_85)
        self.pushButton_227.setIcon(icon1)
        self.pushButton_227.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_227.setFlat(True)
        self.pushButton_227.setObjectName("pushButton_227")
        self.gridLayout_21.addWidget(self.pushButton_227, 3, 1, 1, 1)
        self.gridLayout_50.addWidget(self.frame_85, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Blocks_Level)
        self.Blocks_Flow = QtWidgets.QWidget()
        self.Blocks_Flow.setObjectName("Blocks_Flow")
        self.gridLayout_52 = QtWidgets.QGridLayout(self.Blocks_Flow)
        self.gridLayout_52.setObjectName("gridLayout_52")
        self.frame_88 = QtWidgets.QFrame(self.Blocks_Flow)
        self.frame_88.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_88.setObjectName("frame_88")
        self.gridLayout_51 = QtWidgets.QGridLayout(self.frame_88)
        self.gridLayout_51.setObjectName("gridLayout_51")
        self.pushButton_235 = QtWidgets.QPushButton(self.frame_88)
        self.pushButton_235.setIcon(icon2)
        self.pushButton_235.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_235.setFlat(True)
        self.pushButton_235.setObjectName("pushButton_235")
        self.gridLayout_51.addWidget(self.pushButton_235, 0, 2, 1, 1)
        self.pushButton_236 = QtWidgets.QPushButton(self.frame_88)
        self.pushButton_236.setIcon(icon)
        self.pushButton_236.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_236.setFlat(True)
        self.pushButton_236.setObjectName("pushButton_236")
        self.gridLayout_51.addWidget(self.pushButton_236, 1, 1, 1, 1)
        self.pushButton_237 = QtWidgets.QPushButton(self.frame_88)
        self.pushButton_237.setIcon(icon1)
        self.pushButton_237.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_237.setFlat(True)
        self.pushButton_237.setObjectName("pushButton_237")
        self.gridLayout_51.addWidget(self.pushButton_237, 0, 1, 1, 1)
        self.pushButton_238 = QtWidgets.QPushButton(self.frame_88)
        self.pushButton_238.setIcon(icon1)
        self.pushButton_238.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_238.setFlat(True)
        self.pushButton_238.setObjectName("pushButton_238")
        self.gridLayout_51.addWidget(self.pushButton_238, 2, 1, 1, 1)
        self.pushButton_239 = QtWidgets.QPushButton(self.frame_88)
        self.pushButton_239.setIcon(icon3)
        self.pushButton_239.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_239.setFlat(True)
        self.pushButton_239.setObjectName("pushButton_239")
        self.gridLayout_51.addWidget(self.pushButton_239, 1, 2, 1, 1)
        self.gridLayout_52.addWidget(self.frame_88, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Blocks_Flow)
        self.Blocks_Pressure = QtWidgets.QWidget()
        self.Blocks_Pressure.setObjectName("Blocks_Pressure")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.Blocks_Pressure)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.frame_40 = QtWidgets.QFrame(self.Blocks_Pressure)
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_40)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_94 = QtWidgets.QPushButton(self.frame_40)
        self.pushButton_94.setIcon(icon2)
        self.pushButton_94.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_94.setFlat(True)
        self.pushButton_94.setObjectName("pushButton_94")
        self.gridLayout_7.addWidget(self.pushButton_94, 0, 2, 1, 1)
        self.pushButton_95 = QtWidgets.QPushButton(self.frame_40)
        self.pushButton_95.setIcon(icon)
        self.pushButton_95.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_95.setFlat(True)
        self.pushButton_95.setObjectName("pushButton_95")
        self.gridLayout_7.addWidget(self.pushButton_95, 1, 1, 1, 1)
        self.pushButton_96 = QtWidgets.QPushButton(self.frame_40)
        self.pushButton_96.setIcon(icon1)
        self.pushButton_96.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_96.setFlat(True)
        self.pushButton_96.setObjectName("pushButton_96")
        self.gridLayout_7.addWidget(self.pushButton_96, 0, 1, 1, 1)
        self.pushButton_97 = QtWidgets.QPushButton(self.frame_40)
        self.pushButton_97.setIcon(icon1)
        self.pushButton_97.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_97.setFlat(True)
        self.pushButton_97.setObjectName("pushButton_97")
        self.gridLayout_7.addWidget(self.pushButton_97, 2, 1, 1, 1)
        self.pushButton_98 = QtWidgets.QPushButton(self.frame_40)
        self.pushButton_98.setIcon(icon3)
        self.pushButton_98.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_98.setFlat(True)
        self.pushButton_98.setObjectName("pushButton_98")
        self.gridLayout_7.addWidget(self.pushButton_98, 1, 2, 1, 1)
        self.gridLayout_20.addWidget(self.frame_40, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.Blocks_Pressure)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.centralWidget)
        self.frame_11.setMaximumSize(QtCore.QSize(100, 552))
        self.frame_11.setStyleSheet("")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_23.setEnabled(False)
        self.pushButton_23.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/tools-and-utensils.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_23.setIcon(icon4)
        self.pushButton_23.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_23.setFlat(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.verticalLayout_12.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_24.setEnabled(False)
        self.pushButton_24.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/transfer_function.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon5)
        self.pushButton_24.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_24.setFlat(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_12.addWidget(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_25.setEnabled(False)
        self.pushButton_25.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/graphs.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_25.setIcon(icon6)
        self.pushButton_25.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_25.setFlat(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout_12.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_26.setEnabled(False)
        self.pushButton_26.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon7)
        self.pushButton_26.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_26.setFlat(True)
        self.pushButton_26.setObjectName("pushButton_26")
        self.verticalLayout_12.addWidget(self.pushButton_26)
        self.pushButton_173 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_173.setToolTipDuration(-2)
        self.pushButton_173.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/blocks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_173.setIcon(icon8)
        self.pushButton_173.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_173.setFlat(True)
        self.pushButton_173.setObjectName("pushButton_173")
        self.verticalLayout_12.addWidget(self.pushButton_173)
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_27.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/reply.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_27.setIcon(icon9)
        self.pushButton_27.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_27.setFlat(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_12.addWidget(self.pushButton_27)
        self.gridLayout.addWidget(self.frame_11, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_13 = QtWidgets.QFrame(self.centralWidget)
        self.frame_13.setMaximumSize(QtCore.QSize(660, 100))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.tfMainFigure = QtWidgets.QLabel(self.frame_13)
        self.tfMainFigure.setMaximumSize(QtCore.QSize(48, 48))
        self.tfMainFigure.setText("")
        self.tfMainFigure.setPixmap(QtGui.QPixmap(":/icons/hot-thermometer.svg"))
        self.tfMainFigure.setScaledContents(True)
        self.tfMainFigure.setObjectName("tfMainFigure")
        self.horizontalLayout_13.addWidget(self.tfMainFigure)
        self.title = QtWidgets.QLabel(self.frame_13)
        self.title.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Latin Modern Sans Demi Cond")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.horizontalLayout_13.addWidget(self.title)
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)
        TfDefinition.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(TfDefinition)
        self.statusBar.setEnabled(True)
        self.statusBar.setObjectName("statusBar")
        TfDefinition.setStatusBar(self.statusBar)

        self.retranslateUi(TfDefinition)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(TfDefinition)

    def retranslateUi(self, TfDefinition):
        _translate = QtCore.QCoreApplication.translate
        TfDefinition.setWindowTitle(_translate("TfDefinition", "TfDefinition"))
        self.pushButton_28.setText(_translate("TfDefinition", "           Bomba P101"))
        self.pushButton_6.setText(_translate("TfDefinition", "        Valvula 104"))
        self.pushButton_29.setText(_translate("TfDefinition", "  AQUECEDOR E104"))
        self.pushButton_31.setText(_translate("TfDefinition", "         Valvula 105"))
        self.pushButton_30.setText(_translate("TfDefinition", "      TIC 105"))
        self.pushButton_228.setText(_translate("TfDefinition", "      TIC"))
        self.pushButton_224.setText(_translate("TfDefinition", "  AQUECEDOR E104"))
        self.pushButton_225.setText(_translate("TfDefinition", "           Bomba P101"))
        self.pushButton_226.setText(_translate("TfDefinition", "        Valvula 104"))
        self.pushButton_227.setText(_translate("TfDefinition", "         Valvula 105"))
        self.pushButton_235.setText(_translate("TfDefinition", "  AQUECEDOR E104"))
        self.pushButton_236.setText(_translate("TfDefinition", "           Bomba P101"))
        self.pushButton_237.setText(_translate("TfDefinition", "        Valvula 104"))
        self.pushButton_238.setText(_translate("TfDefinition", "         Valvula 105"))
        self.pushButton_239.setText(_translate("TfDefinition", "      TIC"))
        self.pushButton_94.setText(_translate("TfDefinition", "  AQUECEDOR E104"))
        self.pushButton_95.setText(_translate("TfDefinition", "           Bomba P101"))
        self.pushButton_96.setText(_translate("TfDefinition", "        Valvula 104"))
        self.pushButton_97.setText(_translate("TfDefinition", "         Valvula 105"))
        self.pushButton_98.setText(_translate("TfDefinition", "      TIC"))
        self.pushButton_173.setToolTip(_translate("TfDefinition", "Diagrama de Blocos"))
        self.pushButton_27.setToolTip(_translate("TfDefinition", "Retornar"))
        self.title.setText(_translate("TfDefinition", "DEFINIÇAO DAS FUNÇÕES DE TRANSFERENCIA\n"
" DOS ELEMENTOS DA MALHA DE TEMPERATURA"))

import filter_rc
