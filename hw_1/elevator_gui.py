# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elevator_gui_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from elevator_algo import Controller, Elevator
from threading import Thread

class Ui_Elevator_schedule(object):
    def setupUi(self, Elevator_schedule):
        Elevator_schedule.setObjectName("Elevator_schedule")
        Elevator_schedule.resize(1032, 950)
        Elevator_schedule.setMouseTracking(True)
        self.gridLayoutWidget = QtWidgets.QWidget(Elevator_schedule)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(540, 70, 344, 841))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.elevator1 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.elevator1.setMinimum(1)
        self.elevator1.setMaximum(20)
        self.elevator1.setSingleStep(1)
        self.elevator1.setPageStep(1)
        self.elevator1.setProperty("value", 1)
        self.elevator1.setSliderPosition(1)
        self.elevator1.setTracking(True)
        self.elevator1.setOrientation(QtCore.Qt.Vertical)
        self.elevator1.setObjectName("elevator1")
        self.gridLayout_2.addWidget(self.elevator1, 0, 4, 1, 1)
        self.elevator2 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.elevator2.setMinimum(1)
        self.elevator2.setMaximum(20)
        self.elevator2.setPageStep(1)
        self.elevator2.setOrientation(QtCore.Qt.Vertical)
        self.elevator2.setObjectName("elevator2")
        self.gridLayout_2.addWidget(self.elevator2, 0, 5, 1, 1)
        self.elevator3 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.elevator3.setMinimum(1)
        self.elevator3.setMaximum(20)
        self.elevator3.setPageStep(1)
        self.elevator3.setOrientation(QtCore.Qt.Vertical)
        self.elevator3.setObjectName("elevator3")
        self.gridLayout_2.addWidget(self.elevator3, 0, 6, 1, 1)
        self.buttons = QtWidgets.QVBoxLayout()
        self.buttons.setObjectName("buttons")
        self.b_20 = QtWidgets.QHBoxLayout()
        self.b_20.setObjectName("b_20")
        self.down_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_20.setCheckable(True)
        self.down_20.setObjectName("down_20")
        self.b_20.addWidget(self.down_20)
        self.up_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_20.setCheckable(True)
        self.up_20.setAutoDefault(False)
        self.up_20.setDefault(False)
        self.up_20.setFlat(False)
        self.up_20.setObjectName("up_20")
        self.b_20.addWidget(self.up_20)
        self.buttons.addLayout(self.b_20)
        self.b_19 = QtWidgets.QHBoxLayout()
        self.b_19.setObjectName("b_19")
        self.down_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_19.setCheckable(True)
        self.down_19.setObjectName("down_19")
        self.b_19.addWidget(self.down_19)
        self.up_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_19.setCheckable(True)
        self.up_19.setAutoDefault(False)
        self.up_19.setDefault(False)
        self.up_19.setFlat(False)
        self.up_19.setObjectName("up_19")
        self.b_19.addWidget(self.up_19)
        self.buttons.addLayout(self.b_19)
        self.b_18 = QtWidgets.QHBoxLayout()
        self.b_18.setObjectName("b_18")
        self.down_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_18.setCheckable(True)
        self.down_18.setObjectName("down_18")
        self.b_18.addWidget(self.down_18)
        self.up_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_18.setCheckable(True)
        self.up_18.setAutoDefault(False)
        self.up_18.setDefault(False)
        self.up_18.setFlat(False)
        self.up_18.setObjectName("up_18")
        self.b_18.addWidget(self.up_18)
        self.buttons.addLayout(self.b_18)
        self.b_17 = QtWidgets.QHBoxLayout()
        self.b_17.setObjectName("b_17")
        self.down_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_17.setCheckable(True)
        self.down_17.setObjectName("down_17")
        self.b_17.addWidget(self.down_17)
        self.up_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_17.setCheckable(True)
        self.up_17.setAutoDefault(False)
        self.up_17.setDefault(False)
        self.up_17.setFlat(False)
        self.up_17.setObjectName("up_17")
        self.b_17.addWidget(self.up_17)
        self.buttons.addLayout(self.b_17)
        self.b_16 = QtWidgets.QHBoxLayout()
        self.b_16.setObjectName("b_16")
        self.down_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_16.setCheckable(True)
        self.down_16.setObjectName("down_16")
        self.b_16.addWidget(self.down_16)
        self.up_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_16.setCheckable(True)
        self.up_16.setAutoDefault(False)
        self.up_16.setDefault(False)
        self.up_16.setFlat(False)
        self.up_16.setObjectName("up_16")
        self.b_16.addWidget(self.up_16)
        self.buttons.addLayout(self.b_16)
        self.b_15 = QtWidgets.QHBoxLayout()
        self.b_15.setObjectName("b_15")
        self.down_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_15.setCheckable(True)
        self.down_15.setObjectName("down_15")
        self.b_15.addWidget(self.down_15)
        self.up_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_15.setCheckable(True)
        self.up_15.setAutoDefault(False)
        self.up_15.setDefault(False)
        self.up_15.setFlat(False)
        self.up_15.setObjectName("up_15")
        self.b_15.addWidget(self.up_15)
        self.buttons.addLayout(self.b_15)
        self.b_14 = QtWidgets.QHBoxLayout()
        self.b_14.setObjectName("b_14")
        self.down_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_14.setCheckable(True)
        self.down_14.setObjectName("down_14")
        self.b_14.addWidget(self.down_14)
        self.up_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_14.setCheckable(True)
        self.up_14.setAutoDefault(False)
        self.up_14.setDefault(False)
        self.up_14.setFlat(False)
        self.up_14.setObjectName("up_14")
        self.b_14.addWidget(self.up_14)
        self.buttons.addLayout(self.b_14)
        self.b_13 = QtWidgets.QHBoxLayout()
        self.b_13.setObjectName("b_13")
        self.down_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_13.setCheckable(True)
        self.down_13.setObjectName("down_13")
        self.b_13.addWidget(self.down_13)
        self.up_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_13.setCheckable(True)
        self.up_13.setAutoDefault(False)
        self.up_13.setDefault(False)
        self.up_13.setFlat(False)
        self.up_13.setObjectName("up_13")
        self.b_13.addWidget(self.up_13)
        self.buttons.addLayout(self.b_13)
        self.b_12 = QtWidgets.QHBoxLayout()
        self.b_12.setObjectName("b_12")
        self.down_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_12.setCheckable(True)
        self.down_12.setObjectName("down_12")
        self.b_12.addWidget(self.down_12)
        self.up_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_12.setCheckable(True)
        self.up_12.setAutoDefault(False)
        self.up_12.setDefault(False)
        self.up_12.setFlat(False)
        self.up_12.setObjectName("up_12")
        self.b_12.addWidget(self.up_12)
        self.buttons.addLayout(self.b_12)
        self.b_11 = QtWidgets.QHBoxLayout()
        self.b_11.setObjectName("b_11")
        self.down_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_11.setCheckable(True)
        self.down_11.setObjectName("down_11")
        self.b_11.addWidget(self.down_11)
        self.up_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_11.setCheckable(True)
        self.up_11.setAutoDefault(False)
        self.up_11.setDefault(False)
        self.up_11.setFlat(False)
        self.up_11.setObjectName("up_11")
        self.b_11.addWidget(self.up_11)
        self.buttons.addLayout(self.b_11)
        self.b_10 = QtWidgets.QHBoxLayout()
        self.b_10.setObjectName("b_10")
        self.down_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_10.setCheckable(True)
        self.down_10.setObjectName("down_10")
        self.b_10.addWidget(self.down_10)
        self.up_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_10.setCheckable(True)
        self.up_10.setAutoDefault(False)
        self.up_10.setDefault(False)
        self.up_10.setFlat(False)
        self.up_10.setObjectName("up_10")
        self.b_10.addWidget(self.up_10)
        self.buttons.addLayout(self.b_10)
        self.b_9 = QtWidgets.QHBoxLayout()
        self.b_9.setObjectName("b_9")
        self.down_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_9.setCheckable(True)
        self.down_9.setObjectName("down_9")
        self.b_9.addWidget(self.down_9)
        self.up_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_9.setCheckable(True)
        self.up_9.setAutoDefault(False)
        self.up_9.setDefault(False)
        self.up_9.setFlat(False)
        self.up_9.setObjectName("up_9")
        self.b_9.addWidget(self.up_9)
        self.buttons.addLayout(self.b_9)
        self.b_8 = QtWidgets.QHBoxLayout()
        self.b_8.setObjectName("b_8")
        self.down_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_8.setCheckable(True)
        self.down_8.setObjectName("down_8")
        self.b_8.addWidget(self.down_8)
        self.up_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_8.setCheckable(True)
        self.up_8.setAutoDefault(False)
        self.up_8.setDefault(False)
        self.up_8.setFlat(False)
        self.up_8.setObjectName("up_8")
        self.b_8.addWidget(self.up_8)
        self.buttons.addLayout(self.b_8)
        self.b_7 = QtWidgets.QHBoxLayout()
        self.b_7.setObjectName("b_7")
        self.down_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_7.setCheckable(True)
        self.down_7.setObjectName("down_7")
        self.b_7.addWidget(self.down_7)
        self.up_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_7.setCheckable(True)
        self.up_7.setAutoDefault(False)
        self.up_7.setDefault(False)
        self.up_7.setFlat(False)
        self.up_7.setObjectName("up_7")
        self.b_7.addWidget(self.up_7)
        self.buttons.addLayout(self.b_7)
        self.b_6 = QtWidgets.QHBoxLayout()
        self.b_6.setObjectName("b_6")
        self.down_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_6.setCheckable(True)
        self.down_6.setObjectName("down_6")
        self.b_6.addWidget(self.down_6)
        self.up_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_6.setCheckable(True)
        self.up_6.setAutoDefault(False)
        self.up_6.setDefault(False)
        self.up_6.setFlat(False)
        self.up_6.setObjectName("up_6")
        self.b_6.addWidget(self.up_6)
        self.buttons.addLayout(self.b_6)
        self.b_5 = QtWidgets.QHBoxLayout()
        self.b_5.setObjectName("b_5")
        self.down_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_5.setCheckable(True)
        self.down_5.setObjectName("down_5")
        self.b_5.addWidget(self.down_5)
        self.up_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_5.setCheckable(True)
        self.up_5.setAutoDefault(False)
        self.up_5.setDefault(False)
        self.up_5.setFlat(False)
        self.up_5.setObjectName("up_5")
        self.b_5.addWidget(self.up_5)
        self.buttons.addLayout(self.b_5)
        self.b_4 = QtWidgets.QHBoxLayout()
        self.b_4.setObjectName("b_4")
        self.down_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_4.setCheckable(True)
        self.down_4.setObjectName("down_4")
        self.b_4.addWidget(self.down_4)
        self.up_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_4.setCheckable(True)
        self.up_4.setAutoDefault(False)
        self.up_4.setDefault(False)
        self.up_4.setFlat(False)
        self.up_4.setObjectName("up_4")
        self.b_4.addWidget(self.up_4)
        self.buttons.addLayout(self.b_4)
        self.b_3 = QtWidgets.QHBoxLayout()
        self.b_3.setObjectName("b_3")
        self.down_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_3.setCheckable(True)
        self.down_3.setObjectName("down_3")
        self.b_3.addWidget(self.down_3)
        self.up_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_3.setCheckable(True)
        self.up_3.setAutoDefault(False)
        self.up_3.setDefault(False)
        self.up_3.setFlat(False)
        self.up_3.setObjectName("up_3")
        self.b_3.addWidget(self.up_3)
        self.buttons.addLayout(self.b_3)
        self.b_2 = QtWidgets.QHBoxLayout()
        self.b_2.setObjectName("b_2")
        self.down_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_2.setCheckable(True)
        self.down_2.setObjectName("down_2")
        self.b_2.addWidget(self.down_2)
        self.up_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_2.setCheckable(True)
        self.up_2.setAutoDefault(False)
        self.up_2.setDefault(False)
        self.up_2.setFlat(False)
        self.up_2.setObjectName("up_2")
        self.b_2.addWidget(self.up_2)
        self.buttons.addLayout(self.b_2)
        self.b_1 = QtWidgets.QHBoxLayout()
        self.b_1.setObjectName("b_1")
        self.down_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.down_1.setCheckable(True)
        self.down_1.setObjectName("down_1")
        self.b_1.addWidget(self.down_1)
        self.up_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.up_1.setCheckable(True)
        self.up_1.setAutoDefault(False)
        self.up_1.setDefault(False)
        self.up_1.setFlat(False)
        self.up_1.setObjectName("up_1")
        self.b_1.addWidget(self.up_1)
        self.buttons.addLayout(self.b_1)
        self.gridLayout_2.addLayout(self.buttons, 0, 2, 1, 1)
        self.elevator4 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.elevator4.setMinimum(1)
        self.elevator4.setMaximum(20)
        self.elevator4.setPageStep(1)
        self.elevator4.setOrientation(QtCore.Qt.Vertical)
        self.elevator4.setObjectName("elevator4")
        self.gridLayout_2.addWidget(self.elevator4, 0, 7, 1, 1)
        self.elevator5 = QtWidgets.QSlider(self.gridLayoutWidget)
        self.elevator5.setMinimum(1)
        self.elevator5.setMaximum(20)
        self.elevator5.setPageStep(1)
        self.elevator5.setOrientation(QtCore.Qt.Vertical)
        self.elevator5.setObjectName("elevator5")
        self.gridLayout_2.addWidget(self.elevator5, 0, 8, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Elevator_schedule)
        self.tabWidget.setGeometry(QtCore.QRect(110, 220, 341, 511))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 4, 331, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.verticalLayoutWidget)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.verticalLayout.addWidget(self.lcdNumber_1)
        self.es_10 = QtWidgets.QHBoxLayout()
        self.es_10.setObjectName("es_10")
        self.ef_20 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_20.setCheckable(True)
        self.ef_20.setObjectName("ef_20")
        self.es_10.addWidget(self.ef_20)
        self.ef_19 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_19.setCheckable(True)
        self.ef_19.setObjectName("ef_19")
        self.es_10.addWidget(self.ef_19)
        self.verticalLayout.addLayout(self.es_10)
        self.es_9 = QtWidgets.QHBoxLayout()
        self.es_9.setObjectName("es_9")
        self.ef_18 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_18.setCheckable(True)
        self.ef_18.setObjectName("ef_18")
        self.es_9.addWidget(self.ef_18)
        self.ef_17 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_17.setCheckable(True)
        self.ef_17.setObjectName("ef_17")
        self.es_9.addWidget(self.ef_17)
        self.verticalLayout.addLayout(self.es_9)
        self.es_8 = QtWidgets.QHBoxLayout()
        self.es_8.setObjectName("es_8")
        self.ef_16 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_16.setCheckable(True)
        self.ef_16.setObjectName("ef_16")
        self.es_8.addWidget(self.ef_16)
        self.ef_15 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_15.setCheckable(True)
        self.ef_15.setObjectName("ef_15")
        self.es_8.addWidget(self.ef_15)
        self.verticalLayout.addLayout(self.es_8)
        self.es_7 = QtWidgets.QHBoxLayout()
        self.es_7.setObjectName("es_7")
        self.ef_14 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_14.setCheckable(True)
        self.ef_14.setObjectName("ef_14")
        self.es_7.addWidget(self.ef_14)
        self.ef_13 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_13.setCheckable(True)
        self.ef_13.setObjectName("ef_13")
        self.es_7.addWidget(self.ef_13)
        self.verticalLayout.addLayout(self.es_7)
        self.es_6 = QtWidgets.QHBoxLayout()
        self.es_6.setObjectName("es_6")
        self.ef_12 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_12.setCheckable(True)
        self.ef_12.setObjectName("ef_12")
        self.es_6.addWidget(self.ef_12)
        self.ef_11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_11.setCheckable(True)
        self.ef_11.setObjectName("ef_11")
        self.es_6.addWidget(self.ef_11)
        self.verticalLayout.addLayout(self.es_6)
        self.es_5 = QtWidgets.QHBoxLayout()
        self.es_5.setObjectName("es_5")
        self.ef_10 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_10.setCheckable(True)
        self.ef_10.setObjectName("ef_10")
        self.es_5.addWidget(self.ef_10)
        self.ef_9 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_9.setCheckable(True)
        self.ef_9.setObjectName("ef_9")
        self.es_5.addWidget(self.ef_9)
        self.verticalLayout.addLayout(self.es_5)
        self.es_4 = QtWidgets.QHBoxLayout()
        self.es_4.setObjectName("es_4")
        self.ef_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_8.setCheckable(True)
        self.ef_8.setObjectName("ef_8")
        self.es_4.addWidget(self.ef_8)
        self.ef_7 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_7.setCheckable(True)
        self.ef_7.setObjectName("ef_7")
        self.es_4.addWidget(self.ef_7)
        self.verticalLayout.addLayout(self.es_4)
        self.es_3 = QtWidgets.QHBoxLayout()
        self.es_3.setObjectName("es_3")
        self.ef_6 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_6.setCheckable(True)
        self.ef_6.setObjectName("ef_6")
        self.es_3.addWidget(self.ef_6)
        self.ef_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_5.setCheckable(True)
        self.ef_5.setObjectName("ef_5")
        self.es_3.addWidget(self.ef_5)
        self.verticalLayout.addLayout(self.es_3)
        self.es_2 = QtWidgets.QHBoxLayout()
        self.es_2.setObjectName("es_2")
        self.ef_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_4.setCheckable(True)
        self.ef_4.setObjectName("ef_4")
        self.es_2.addWidget(self.ef_4)
        self.ef_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_3.setCheckable(True)
        self.ef_3.setObjectName("ef_3")
        self.es_2.addWidget(self.ef_3)
        self.verticalLayout.addLayout(self.es_2)
        self.es_1 = QtWidgets.QHBoxLayout()
        self.es_1.setObjectName("es_1")
        self.ef_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_2.setCheckable(True)
        self.ef_2.setObjectName("ef_2")
        self.es_1.addWidget(self.ef_2)
        self.ef_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ef_1.setCheckable(True)
        self.ef_1.setObjectName("ef_1")
        self.es_1.addWidget(self.ef_1)
        self.verticalLayout.addLayout(self.es_1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 331, 481))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_2.addWidget(self.lcdNumber_2)
        self.es2_10 = QtWidgets.QHBoxLayout()
        self.es2_10.setObjectName("es2_10")
        self.ef2_20 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_20.setCheckable(True)
        self.ef2_20.setObjectName("ef2_20")
        self.es2_10.addWidget(self.ef2_20)
        self.ef2_19 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_19.setCheckable(True)
        self.ef2_19.setObjectName("ef2_19")
        self.es2_10.addWidget(self.ef2_19)
        self.verticalLayout_2.addLayout(self.es2_10)
        self.es2_9 = QtWidgets.QHBoxLayout()
        self.es2_9.setObjectName("es2_9")
        self.ef2_18 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_18.setCheckable(True)
        self.ef2_18.setObjectName("ef2_18")
        self.es2_9.addWidget(self.ef2_18)
        self.ef2_17 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_17.setCheckable(True)
        self.ef2_17.setObjectName("ef2_17")
        self.es2_9.addWidget(self.ef2_17)
        self.verticalLayout_2.addLayout(self.es2_9)
        self.es2_8 = QtWidgets.QHBoxLayout()
        self.es2_8.setObjectName("es2_8")
        self.ef2_16 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_16.setCheckable(True)
        self.ef2_16.setObjectName("ef2_16")
        self.es2_8.addWidget(self.ef2_16)
        self.ef2_15 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_15.setCheckable(True)
        self.ef2_15.setObjectName("ef2_15")
        self.es2_8.addWidget(self.ef2_15)
        self.verticalLayout_2.addLayout(self.es2_8)
        self.es2_7 = QtWidgets.QHBoxLayout()
        self.es2_7.setObjectName("es2_7")
        self.ef2_14 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_14.setCheckable(True)
        self.ef2_14.setObjectName("ef2_14")
        self.es2_7.addWidget(self.ef2_14)
        self.ef2_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_13.setCheckable(True)
        self.ef2_13.setObjectName("ef2_13")
        self.es2_7.addWidget(self.ef2_13)
        self.verticalLayout_2.addLayout(self.es2_7)
        self.es2_6 = QtWidgets.QHBoxLayout()
        self.es2_6.setObjectName("es2_6")
        self.ef2_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_12.setCheckable(True)
        self.ef2_12.setObjectName("ef2_12")
        self.es2_6.addWidget(self.ef2_12)
        self.ef2_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_11.setCheckable(True)
        self.ef2_11.setObjectName("ef2_11")
        self.es2_6.addWidget(self.ef2_11)
        self.verticalLayout_2.addLayout(self.es2_6)
        self.es2_5 = QtWidgets.QHBoxLayout()
        self.es2_5.setObjectName("es2_5")
        self.ef2_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_10.setCheckable(True)
        self.ef2_10.setObjectName("ef2_10")
        self.es2_5.addWidget(self.ef2_10)
        self.ef2_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_9.setCheckable(True)
        self.ef2_9.setObjectName("ef2_9")
        self.es2_5.addWidget(self.ef2_9)
        self.verticalLayout_2.addLayout(self.es2_5)
        self.es2_4 = QtWidgets.QHBoxLayout()
        self.es2_4.setObjectName("es2_4")
        self.ef2_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_8.setCheckable(True)
        self.ef2_8.setObjectName("ef2_8")
        self.es2_4.addWidget(self.ef2_8)
        self.ef2_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_7.setCheckable(True)
        self.ef2_7.setObjectName("ef2_7")
        self.es2_4.addWidget(self.ef2_7)
        self.verticalLayout_2.addLayout(self.es2_4)
        self.es2_3 = QtWidgets.QHBoxLayout()
        self.es2_3.setObjectName("es2_3")
        self.ef2_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_6.setCheckable(True)
        self.ef2_6.setObjectName("ef2_6")
        self.es2_3.addWidget(self.ef2_6)
        self.ef2_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_5.setCheckable(True)
        self.ef2_5.setObjectName("ef2_5")
        self.es2_3.addWidget(self.ef2_5)
        self.verticalLayout_2.addLayout(self.es2_3)
        self.es2_2 = QtWidgets.QHBoxLayout()
        self.es2_2.setObjectName("es2_2")
        self.ef2_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_4.setCheckable(True)
        self.ef2_4.setObjectName("ef2_4")
        self.es2_2.addWidget(self.ef2_4)
        self.ef2_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_3.setCheckable(True)
        self.ef2_3.setObjectName("ef2_3")
        self.es2_2.addWidget(self.ef2_3)
        self.verticalLayout_2.addLayout(self.es2_2)
        self.es2_1 = QtWidgets.QHBoxLayout()
        self.es2_1.setObjectName("es2_1")
        self.ef2_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_2.setCheckable(True)
        self.ef2_2.setObjectName("ef2_2")
        self.es2_1.addWidget(self.ef2_2)
        self.ef2_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ef2_1.setCheckable(True)
        self.ef2_1.setObjectName("ef2_1")
        self.es2_1.addWidget(self.ef2_1)
        self.verticalLayout_2.addLayout(self.es2_1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 10, 331, 471))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_3)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout_3.addWidget(self.lcdNumber_3)
        self.es3_10 = QtWidgets.QHBoxLayout()
        self.es3_10.setObjectName("es3_10")
        self.ef3_20 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_20.setCheckable(True)
        self.ef3_20.setObjectName("ef3_20")
        self.es3_10.addWidget(self.ef3_20)
        self.ef3_19 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_19.setCheckable(True)
        self.ef3_19.setObjectName("ef3_19")
        self.es3_10.addWidget(self.ef3_19)
        self.verticalLayout_3.addLayout(self.es3_10)
        self.es3_9 = QtWidgets.QHBoxLayout()
        self.es3_9.setObjectName("es3_9")
        self.ef3_18 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_18.setCheckable(True)
        self.ef3_18.setObjectName("ef3_18")
        self.es3_9.addWidget(self.ef3_18)
        self.ef3_17 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_17.setCheckable(True)
        self.ef3_17.setObjectName("ef3_17")
        self.es3_9.addWidget(self.ef3_17)
        self.verticalLayout_3.addLayout(self.es3_9)
        self.es3_8 = QtWidgets.QHBoxLayout()
        self.es3_8.setObjectName("es3_8")
        self.ef3_16 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_16.setCheckable(True)
        self.ef3_16.setObjectName("ef3_16")
        self.es3_8.addWidget(self.ef3_16)
        self.ef3_15 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_15.setCheckable(True)
        self.ef3_15.setObjectName("ef3_15")
        self.es3_8.addWidget(self.ef3_15)
        self.verticalLayout_3.addLayout(self.es3_8)
        self.es3_7 = QtWidgets.QHBoxLayout()
        self.es3_7.setObjectName("es3_7")
        self.ef3_14 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_14.setCheckable(True)
        self.ef3_14.setObjectName("ef3_14")
        self.es3_7.addWidget(self.ef3_14)
        self.ef3_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_13.setCheckable(True)
        self.ef3_13.setObjectName("ef3_13")
        self.es3_7.addWidget(self.ef3_13)
        self.verticalLayout_3.addLayout(self.es3_7)
        self.es3_6 = QtWidgets.QHBoxLayout()
        self.es3_6.setObjectName("es3_6")
        self.ef3_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_12.setCheckable(True)
        self.ef3_12.setObjectName("ef3_12")
        self.es3_6.addWidget(self.ef3_12)
        self.ef3_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_11.setCheckable(True)
        self.ef3_11.setObjectName("ef3_11")
        self.es3_6.addWidget(self.ef3_11)
        self.verticalLayout_3.addLayout(self.es3_6)
        self.es3_5 = QtWidgets.QHBoxLayout()
        self.es3_5.setObjectName("es3_5")
        self.ef3_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_10.setCheckable(True)
        self.ef3_10.setObjectName("ef3_10")
        self.es3_5.addWidget(self.ef3_10)
        self.ef3_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_9.setCheckable(True)
        self.ef3_9.setObjectName("ef3_9")
        self.es3_5.addWidget(self.ef3_9)
        self.verticalLayout_3.addLayout(self.es3_5)
        self.es3_4 = QtWidgets.QHBoxLayout()
        self.es3_4.setObjectName("es3_4")
        self.ef3_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_8.setCheckable(True)
        self.ef3_8.setObjectName("ef3_8")
        self.es3_4.addWidget(self.ef3_8)
        self.ef3_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_7.setCheckable(True)
        self.ef3_7.setObjectName("ef3_7")
        self.es3_4.addWidget(self.ef3_7)
        self.verticalLayout_3.addLayout(self.es3_4)
        self.es3_3 = QtWidgets.QHBoxLayout()
        self.es3_3.setObjectName("es3_3")
        self.ef3_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_6.setCheckable(True)
        self.ef3_6.setObjectName("ef3_6")
        self.es3_3.addWidget(self.ef3_6)
        self.ef3_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_5.setCheckable(True)
        self.ef3_5.setObjectName("ef3_5")
        self.es3_3.addWidget(self.ef3_5)
        self.verticalLayout_3.addLayout(self.es3_3)
        self.es3_2 = QtWidgets.QHBoxLayout()
        self.es3_2.setObjectName("es3_2")
        self.ef3_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_4.setCheckable(True)
        self.ef3_4.setObjectName("ef3_4")
        self.es3_2.addWidget(self.ef3_4)
        self.ef3_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_3.setCheckable(True)
        self.ef3_3.setObjectName("ef3_3")
        self.es3_2.addWidget(self.ef3_3)
        self.verticalLayout_3.addLayout(self.es3_2)
        self.es3_1 = QtWidgets.QHBoxLayout()
        self.es3_1.setObjectName("es3_1")
        self.ef3_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_2.setCheckable(True)
        self.ef3_2.setObjectName("ef3_2")
        self.es3_1.addWidget(self.ef3_2)
        self.ef3_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ef3_1.setCheckable(True)
        self.ef3_1.setObjectName("ef3_1")
        self.es3_1.addWidget(self.ef3_1)
        self.verticalLayout_3.addLayout(self.es3_1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 331, 471))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_4)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.verticalLayout_4.addWidget(self.lcdNumber_4)
        self.es4_10 = QtWidgets.QHBoxLayout()
        self.es4_10.setObjectName("es4_10")
        self.ef4_20 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_20.setCheckable(True)
        self.ef4_20.setObjectName("ef4_20")
        self.es4_10.addWidget(self.ef4_20)
        self.ef4_19 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_19.setCheckable(True)
        self.ef4_19.setObjectName("ef4_19")
        self.es4_10.addWidget(self.ef4_19)
        self.verticalLayout_4.addLayout(self.es4_10)
        self.es4_9 = QtWidgets.QHBoxLayout()
        self.es4_9.setObjectName("es4_9")
        self.ef4_18 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_18.setCheckable(True)
        self.ef4_18.setObjectName("ef4_18")
        self.es4_9.addWidget(self.ef4_18)
        self.ef4_17 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_17.setCheckable(True)
        self.ef4_17.setObjectName("ef4_17")
        self.es4_9.addWidget(self.ef4_17)
        self.verticalLayout_4.addLayout(self.es4_9)
        self.es4_8 = QtWidgets.QHBoxLayout()
        self.es4_8.setObjectName("es4_8")
        self.ef4_16 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_16.setCheckable(True)
        self.ef4_16.setObjectName("ef4_16")
        self.es4_8.addWidget(self.ef4_16)
        self.ef4_15 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_15.setCheckable(True)
        self.ef4_15.setObjectName("ef4_15")
        self.es4_8.addWidget(self.ef4_15)
        self.verticalLayout_4.addLayout(self.es4_8)
        self.es4_7 = QtWidgets.QHBoxLayout()
        self.es4_7.setObjectName("es4_7")
        self.ef4_14 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_14.setCheckable(True)
        self.ef4_14.setObjectName("ef4_14")
        self.es4_7.addWidget(self.ef4_14)
        self.ef4_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_13.setCheckable(True)
        self.ef4_13.setObjectName("ef4_13")
        self.es4_7.addWidget(self.ef4_13)
        self.verticalLayout_4.addLayout(self.es4_7)
        self.es4_6 = QtWidgets.QHBoxLayout()
        self.es4_6.setObjectName("es4_6")
        self.ef4_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_12.setCheckable(True)
        self.ef4_12.setObjectName("ef4_12")
        self.es4_6.addWidget(self.ef4_12)
        self.ef4_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_11.setCheckable(True)
        self.ef4_11.setObjectName("ef4_11")
        self.es4_6.addWidget(self.ef4_11)
        self.verticalLayout_4.addLayout(self.es4_6)
        self.es4_5 = QtWidgets.QHBoxLayout()
        self.es4_5.setObjectName("es4_5")
        self.ef4_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_10.setCheckable(True)
        self.ef4_10.setObjectName("ef4_10")
        self.es4_5.addWidget(self.ef4_10)
        self.ef4_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_9.setCheckable(True)
        self.ef4_9.setObjectName("ef4_9")
        self.es4_5.addWidget(self.ef4_9)
        self.verticalLayout_4.addLayout(self.es4_5)
        self.es4_4 = QtWidgets.QHBoxLayout()
        self.es4_4.setObjectName("es4_4")
        self.ef4_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_8.setCheckable(True)
        self.ef4_8.setObjectName("ef4_8")
        self.es4_4.addWidget(self.ef4_8)
        self.ef4_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_7.setCheckable(True)
        self.ef4_7.setObjectName("ef4_7")
        self.es4_4.addWidget(self.ef4_7)
        self.verticalLayout_4.addLayout(self.es4_4)
        self.es4_3 = QtWidgets.QHBoxLayout()
        self.es4_3.setObjectName("es4_3")
        self.ef4_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_6.setCheckable(True)
        self.ef4_6.setObjectName("ef4_6")
        self.es4_3.addWidget(self.ef4_6)
        self.ef4_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_5.setCheckable(True)
        self.ef4_5.setObjectName("ef4_5")
        self.es4_3.addWidget(self.ef4_5)
        self.verticalLayout_4.addLayout(self.es4_3)
        self.es4_2 = QtWidgets.QHBoxLayout()
        self.es4_2.setObjectName("es4_2")
        self.ef4_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_4.setCheckable(True)
        self.ef4_4.setObjectName("ef4_4")
        self.es4_2.addWidget(self.ef4_4)
        self.ef4_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_3.setCheckable(True)
        self.ef4_3.setObjectName("ef4_3")
        self.es4_2.addWidget(self.ef4_3)
        self.verticalLayout_4.addLayout(self.es4_2)
        self.es4_1 = QtWidgets.QHBoxLayout()
        self.es4_1.setObjectName("es4_1")
        self.ef4_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_2.setCheckable(True)
        self.ef4_2.setObjectName("ef4_2")
        self.es4_1.addWidget(self.ef4_2)
        self.ef4_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.ef4_1.setCheckable(True)
        self.ef4_1.setObjectName("ef4_1")
        self.es4_1.addWidget(self.ef4_1)
        self.verticalLayout_4.addLayout(self.es4_1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.tab_5)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 331, 471))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.verticalLayoutWidget_5)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.verticalLayout_5.addWidget(self.lcdNumber_5)
        self.es5_10 = QtWidgets.QHBoxLayout()
        self.es5_10.setObjectName("es5_10")
        self.ef5_20 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_20.setCheckable(True)
        self.ef5_20.setObjectName("ef5_20")
        self.es5_10.addWidget(self.ef5_20)
        self.ef5_19 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_19.setCheckable(True)
        self.ef5_19.setObjectName("ef5_19")
        self.es5_10.addWidget(self.ef5_19)
        self.verticalLayout_5.addLayout(self.es5_10)
        self.es5_9 = QtWidgets.QHBoxLayout()
        self.es5_9.setObjectName("es5_9")
        self.ef5_18 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_18.setCheckable(True)
        self.ef5_18.setObjectName("ef5_18")
        self.es5_9.addWidget(self.ef5_18)
        self.ef5_17 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_17.setCheckable(True)
        self.ef5_17.setObjectName("ef5_17")
        self.es5_9.addWidget(self.ef5_17)
        self.verticalLayout_5.addLayout(self.es5_9)
        self.es5_8 = QtWidgets.QHBoxLayout()
        self.es5_8.setObjectName("es5_8")
        self.ef5_16 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_16.setCheckable(True)
        self.ef5_16.setObjectName("ef5_16")
        self.es5_8.addWidget(self.ef5_16)
        self.ef5_15 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_15.setCheckable(True)
        self.ef5_15.setObjectName("ef5_15")
        self.es5_8.addWidget(self.ef5_15)
        self.verticalLayout_5.addLayout(self.es5_8)
        self.es5_7 = QtWidgets.QHBoxLayout()
        self.es5_7.setObjectName("es5_7")
        self.ef5_14 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_14.setCheckable(True)
        self.ef5_14.setObjectName("ef5_14")
        self.es5_7.addWidget(self.ef5_14)
        self.ef5_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_13.setCheckable(True)
        self.ef5_13.setObjectName("ef5_13")
        self.es5_7.addWidget(self.ef5_13)
        self.verticalLayout_5.addLayout(self.es5_7)
        self.es5_6 = QtWidgets.QHBoxLayout()
        self.es5_6.setObjectName("es5_6")
        self.ef5_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_12.setCheckable(True)
        self.ef5_12.setObjectName("ef5_12")
        self.es5_6.addWidget(self.ef5_12)
        self.ef5_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_11.setCheckable(True)
        self.ef5_11.setObjectName("ef5_11")
        self.es5_6.addWidget(self.ef5_11)
        self.verticalLayout_5.addLayout(self.es5_6)
        self.es5_5 = QtWidgets.QHBoxLayout()
        self.es5_5.setObjectName("es5_5")
        self.ef5_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_10.setCheckable(True)
        self.ef5_10.setObjectName("ef5_10")
        self.es5_5.addWidget(self.ef5_10)
        self.ef5_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_9.setCheckable(True)
        self.ef5_9.setObjectName("ef5_9")
        self.es5_5.addWidget(self.ef5_9)
        self.verticalLayout_5.addLayout(self.es5_5)
        self.es5_4 = QtWidgets.QHBoxLayout()
        self.es5_4.setObjectName("es5_4")
        self.ef5_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_8.setCheckable(True)
        self.ef5_8.setObjectName("ef5_8")
        self.es5_4.addWidget(self.ef5_8)
        self.ef5_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_7.setCheckable(True)
        self.ef5_7.setObjectName("ef5_7")
        self.es5_4.addWidget(self.ef5_7)
        self.verticalLayout_5.addLayout(self.es5_4)
        self.es5_3 = QtWidgets.QHBoxLayout()
        self.es5_3.setObjectName("es5_3")
        self.ef5_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_6.setCheckable(True)
        self.ef5_6.setObjectName("ef5_6")
        self.es5_3.addWidget(self.ef5_6)
        self.ef5_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_5.setCheckable(True)
        self.ef5_5.setObjectName("ef5_5")
        self.es5_3.addWidget(self.ef5_5)
        self.verticalLayout_5.addLayout(self.es5_3)
        self.es5_2 = QtWidgets.QHBoxLayout()
        self.es5_2.setObjectName("es5_2")
        self.ef5_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_4.setCheckable(True)
        self.ef5_4.setObjectName("ef5_4")
        self.es5_2.addWidget(self.ef5_4)
        self.ef5_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_3.setCheckable(True)
        self.ef5_3.setObjectName("ef5_3")
        self.es5_2.addWidget(self.ef5_3)
        self.verticalLayout_5.addLayout(self.es5_2)
        self.es5_1 = QtWidgets.QHBoxLayout()
        self.es5_1.setObjectName("es5_1")
        self.ef5_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_2.setCheckable(True)
        self.ef5_2.setObjectName("ef5_2")
        self.es5_1.addWidget(self.ef5_2)
        self.ef5_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.ef5_1.setCheckable(True)
        self.ef5_1.setObjectName("ef5_1")
        self.es5_1.addWidget(self.ef5_1)
        self.verticalLayout_5.addLayout(self.es5_1)
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Elevator_schedule)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Elevator_schedule)

        self.down_20.clicked.connect(self.band_down20)
        self.down_19.clicked.connect(self.band_down19)
        self.down_18.clicked.connect(self.band_down18)
        self.down_17.clicked.connect(self.band_down17)
        self.down_16.clicked.connect(self.band_down16)
        self.down_15.clicked.connect(self.band_down15)
        self.down_14.clicked.connect(self.band_down14)
        self.down_13.clicked.connect(self.band_down13)
        self.down_12.clicked.connect(self.band_down12)
        self.down_11.clicked.connect(self.band_down11)
        self.down_10.clicked.connect(self.band_down10)
        self.down_9.clicked.connect(self.band_down9)
        self.down_8.clicked.connect(self.band_down8)
        self.down_7.clicked.connect(self.band_down7)
        self.down_6.clicked.connect(self.band_down6)
        self.down_5.clicked.connect(self.band_down5)
        self.down_4.clicked.connect(self.band_down4)
        self.down_3.clicked.connect(self.band_down3)
        self.down_2.clicked.connect(self.band_down2)
        self.up_1.clicked.connect(self.band_up1)
        self.up_2.clicked.connect(self.band_up2)
        self.up_3.clicked.connect(self.band_up3)
        self.up_4.clicked.connect(self.band_up4)
        self.up_5.clicked.connect(self.band_up5)
        self.up_6.clicked.connect(self.band_up6)
        self.up_7.clicked.connect(self.band_up7)
        self.up_8.clicked.connect(self.band_up8)
        self.up_9.clicked.connect(self.band_up9)
        self.up_10.clicked.connect(self.band_up10)
        self.up_11.clicked.connect(self.band_up11)
        self.up_12.clicked.connect(self.band_up12)
        self.up_13.clicked.connect(self.band_up13)
        self.up_14.clicked.connect(self.band_up14)
        self.up_15.clicked.connect(self.band_up15)
        self.up_16.clicked.connect(self.band_up16)
        self.up_17.clicked.connect(self.band_up17)
        self.up_18.clicked.connect(self.band_up18)
        self.up_19.clicked.connect(self.band_up19)
        self.ef_1.clicked.connect(self.band_ef_1)
        self.ef_2.clicked.connect(self.band_ef_2)
        self.ef_3.clicked.connect(self.band_ef_3)
        self.ef_4.clicked.connect(self.band_ef_4)
        self.ef_5.clicked.connect(self.band_ef_5)
        self.ef_6.clicked.connect(self.band_ef_6)
        self.ef_7.clicked.connect(self.band_ef_7)
        self.ef_8.clicked.connect(self.band_ef_8)
        self.ef_9.clicked.connect(self.band_ef_9)
        self.ef_10.clicked.connect(self.band_ef_10)
        self.ef_11.clicked.connect(self.band_ef_11)
        self.ef_12.clicked.connect(self.band_ef_12)
        self.ef_13.clicked.connect(self.band_ef_13)
        self.ef_14.clicked.connect(self.band_ef_14)
        self.ef_15.clicked.connect(self.band_ef_15)
        self.ef_16.clicked.connect(self.band_ef_16)
        self.ef_17.clicked.connect(self.band_ef_17)
        self.ef_18.clicked.connect(self.band_ef_18)
        self.ef_19.clicked.connect(self.band_ef_19)
        self.ef_20.clicked.connect(self.band_ef_20)
        self.ef2_1.clicked.connect(self.band_ef2_1)
        self.ef2_2.clicked.connect(self.band_ef2_2)
        self.ef2_3.clicked.connect(self.band_ef2_3)
        self.ef2_4.clicked.connect(self.band_ef2_4)
        self.ef2_5.clicked.connect(self.band_ef2_5)
        self.ef2_6.clicked.connect(self.band_ef2_6)
        self.ef2_7.clicked.connect(self.band_ef2_7)
        self.ef2_8.clicked.connect(self.band_ef2_8)
        self.ef2_9.clicked.connect(self.band_ef2_9)
        self.ef2_10.clicked.connect(self.band_ef2_10)
        self.ef2_11.clicked.connect(self.band_ef2_11)
        self.ef2_12.clicked.connect(self.band_ef2_12)
        self.ef2_13.clicked.connect(self.band_ef2_13)
        self.ef2_14.clicked.connect(self.band_ef2_14)
        self.ef2_15.clicked.connect(self.band_ef2_15)
        self.ef2_16.clicked.connect(self.band_ef2_16)
        self.ef2_17.clicked.connect(self.band_ef2_17)
        self.ef2_18.clicked.connect(self.band_ef2_18)
        self.ef2_19.clicked.connect(self.band_ef2_19)
        self.ef2_20.clicked.connect(self.band_ef2_20)
        self.ef3_1.clicked.connect(self.band_ef3_1)
        self.ef3_2.clicked.connect(self.band_ef3_2)
        self.ef3_3.clicked.connect(self.band_ef3_3)
        self.ef3_4.clicked.connect(self.band_ef3_4)
        self.ef3_5.clicked.connect(self.band_ef3_5)
        self.ef3_6.clicked.connect(self.band_ef3_6)
        self.ef3_7.clicked.connect(self.band_ef3_7)
        self.ef3_8.clicked.connect(self.band_ef3_8)
        self.ef3_9.clicked.connect(self.band_ef3_9)
        self.ef3_10.clicked.connect(self.band_ef3_10)
        self.ef3_11.clicked.connect(self.band_ef3_11)
        self.ef3_12.clicked.connect(self.band_ef3_12)
        self.ef3_13.clicked.connect(self.band_ef3_13)
        self.ef3_14.clicked.connect(self.band_ef3_14)
        self.ef3_15.clicked.connect(self.band_ef3_15)
        self.ef3_16.clicked.connect(self.band_ef3_16)
        self.ef3_17.clicked.connect(self.band_ef3_17)
        self.ef3_18.clicked.connect(self.band_ef3_18)
        self.ef3_19.clicked.connect(self.band_ef3_19)
        self.ef3_20.clicked.connect(self.band_ef3_20)
        self.ef4_1.clicked.connect(self.band_ef4_1)
        self.ef4_2.clicked.connect(self.band_ef4_2)
        self.ef4_3.clicked.connect(self.band_ef4_3)
        self.ef4_4.clicked.connect(self.band_ef4_4)
        self.ef4_5.clicked.connect(self.band_ef4_5)
        self.ef4_6.clicked.connect(self.band_ef4_6)
        self.ef4_7.clicked.connect(self.band_ef4_7)
        self.ef4_8.clicked.connect(self.band_ef4_8)
        self.ef4_9.clicked.connect(self.band_ef4_9)
        self.ef4_10.clicked.connect(self.band_ef4_10)
        self.ef4_11.clicked.connect(self.band_ef4_11)
        self.ef4_12.clicked.connect(self.band_ef4_12)
        self.ef4_13.clicked.connect(self.band_ef4_13)
        self.ef4_14.clicked.connect(self.band_ef4_14)
        self.ef4_15.clicked.connect(self.band_ef4_15)
        self.ef4_16.clicked.connect(self.band_ef4_16)
        self.ef4_17.clicked.connect(self.band_ef4_17)
        self.ef4_18.clicked.connect(self.band_ef4_18)
        self.ef4_19.clicked.connect(self.band_ef4_19)
        self.ef4_20.clicked.connect(self.band_ef4_20)
        self.ef5_1.clicked.connect(self.band_ef5_1)
        self.ef5_2.clicked.connect(self.band_ef5_2)
        self.ef5_3.clicked.connect(self.band_ef5_3)
        self.ef5_4.clicked.connect(self.band_ef5_4)
        self.ef5_5.clicked.connect(self.band_ef5_5)
        self.ef5_6.clicked.connect(self.band_ef5_6)
        self.ef5_7.clicked.connect(self.band_ef5_7)
        self.ef5_8.clicked.connect(self.band_ef5_8)
        self.ef5_9.clicked.connect(self.band_ef5_9)
        self.ef5_10.clicked.connect(self.band_ef5_10)
        self.ef5_11.clicked.connect(self.band_ef5_11)
        self.ef5_12.clicked.connect(self.band_ef5_12)
        self.ef5_13.clicked.connect(self.band_ef5_13)
        self.ef5_14.clicked.connect(self.band_ef5_14)
        self.ef5_15.clicked.connect(self.band_ef5_15)
        self.ef5_16.clicked.connect(self.band_ef5_16)
        self.ef5_17.clicked.connect(self.band_ef5_17)
        self.ef5_18.clicked.connect(self.band_ef5_18)
        self.ef5_19.clicked.connect(self.band_ef5_19)
        self.ef5_20.clicked.connect(self.band_ef5_20)
    def retranslateUi(self, Elevator_schedule):
        _translate = QtCore.QCoreApplication.translate
        Elevator_schedule.setWindowTitle(_translate("Elevator_schedule", "Form"))
        self.down_20.setText(_translate("Elevator_schedule", "⇩"))
        self.up_20.setText(_translate("Elevator_schedule", "⇧"))
        self.down_19.setText(_translate("Elevator_schedule", "⇩"))
        self.up_19.setText(_translate("Elevator_schedule", "⇧"))
        self.down_18.setText(_translate("Elevator_schedule", "⇩"))
        self.up_18.setText(_translate("Elevator_schedule", "⇧"))
        self.down_17.setText(_translate("Elevator_schedule", "⇩"))
        self.up_17.setText(_translate("Elevator_schedule", "⇧"))
        self.down_16.setText(_translate("Elevator_schedule", "⇩"))
        self.up_16.setText(_translate("Elevator_schedule", "⇧"))
        self.down_15.setText(_translate("Elevator_schedule", "⇩"))
        self.up_15.setText(_translate("Elevator_schedule", "⇧"))
        self.down_14.setText(_translate("Elevator_schedule", "⇩"))
        self.up_14.setText(_translate("Elevator_schedule", "⇧"))
        self.down_13.setText(_translate("Elevator_schedule", "⇩"))
        self.up_13.setText(_translate("Elevator_schedule", "⇧"))
        self.down_12.setText(_translate("Elevator_schedule", "⇩"))
        self.up_12.setText(_translate("Elevator_schedule", "⇧"))
        self.down_11.setText(_translate("Elevator_schedule", "⇩"))
        self.up_11.setText(_translate("Elevator_schedule", "⇧"))
        self.down_10.setText(_translate("Elevator_schedule", "⇩"))
        self.up_10.setText(_translate("Elevator_schedule", "⇧"))
        self.down_9.setText(_translate("Elevator_schedule", "⇩"))
        self.up_9.setText(_translate("Elevator_schedule", "⇧"))
        self.down_8.setText(_translate("Elevator_schedule", "⇩"))
        self.up_8.setText(_translate("Elevator_schedule", "⇧"))
        self.down_7.setText(_translate("Elevator_schedule", "⇩"))
        self.up_7.setText(_translate("Elevator_schedule", "⇧"))
        self.down_6.setText(_translate("Elevator_schedule", "⇩"))
        self.up_6.setText(_translate("Elevator_schedule", "⇧"))
        self.down_5.setText(_translate("Elevator_schedule", "⇩"))
        self.up_5.setText(_translate("Elevator_schedule", "⇧"))
        self.down_4.setText(_translate("Elevator_schedule", "⇩"))
        self.up_4.setText(_translate("Elevator_schedule", "⇧"))
        self.down_3.setText(_translate("Elevator_schedule", "⇩"))
        self.up_3.setText(_translate("Elevator_schedule", "⇧"))
        self.down_2.setText(_translate("Elevator_schedule", "⇩"))
        self.up_2.setText(_translate("Elevator_schedule", "⇧"))
        self.down_1.setText(_translate("Elevator_schedule", "⇩"))
        self.up_1.setText(_translate("Elevator_schedule", "⇧"))
        self.ef_20.setText(_translate("Elevator_schedule", "20"))
        self.ef_19.setText(_translate("Elevator_schedule", "19"))
        self.ef_18.setText(_translate("Elevator_schedule", "18"))
        self.ef_17.setText(_translate("Elevator_schedule", "17"))
        self.ef_16.setText(_translate("Elevator_schedule", "16"))
        self.ef_15.setText(_translate("Elevator_schedule", "15"))
        self.ef_14.setText(_translate("Elevator_schedule", "14"))
        self.ef_13.setText(_translate("Elevator_schedule", "13"))
        self.ef_12.setText(_translate("Elevator_schedule", "12"))
        self.ef_11.setText(_translate("Elevator_schedule", "11"))
        self.ef_10.setText(_translate("Elevator_schedule", "10"))
        self.ef_9.setText(_translate("Elevator_schedule", "9"))
        self.ef_8.setText(_translate("Elevator_schedule", "8"))
        self.ef_7.setText(_translate("Elevator_schedule", "7"))
        self.ef_6.setText(_translate("Elevator_schedule", "6"))
        self.ef_5.setText(_translate("Elevator_schedule", "5"))
        self.ef_4.setText(_translate("Elevator_schedule", "4"))
        self.ef_3.setText(_translate("Elevator_schedule", "3"))
        self.ef_2.setText(_translate("Elevator_schedule", "2"))
        self.ef_1.setText(_translate("Elevator_schedule", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Elevator_schedule", "电梯1"))
        self.ef2_20.setText(_translate("Elevator_schedule", "20"))
        self.ef2_19.setText(_translate("Elevator_schedule", "19"))
        self.ef2_18.setText(_translate("Elevator_schedule", "18"))
        self.ef2_17.setText(_translate("Elevator_schedule", "17"))
        self.ef2_16.setText(_translate("Elevator_schedule", "16"))
        self.ef2_15.setText(_translate("Elevator_schedule", "15"))
        self.ef2_14.setText(_translate("Elevator_schedule", "14"))
        self.ef2_13.setText(_translate("Elevator_schedule", "13"))
        self.ef2_12.setText(_translate("Elevator_schedule", "12"))
        self.ef2_11.setText(_translate("Elevator_schedule", "11"))
        self.ef2_10.setText(_translate("Elevator_schedule", "10"))
        self.ef2_9.setText(_translate("Elevator_schedule", "9"))
        self.ef2_8.setText(_translate("Elevator_schedule", "8"))
        self.ef2_7.setText(_translate("Elevator_schedule", "7"))
        self.ef2_6.setText(_translate("Elevator_schedule", "6"))
        self.ef2_5.setText(_translate("Elevator_schedule", "5"))
        self.ef2_4.setText(_translate("Elevator_schedule", "4"))
        self.ef2_3.setText(_translate("Elevator_schedule", "3"))
        self.ef2_2.setText(_translate("Elevator_schedule", "2"))
        self.ef2_1.setText(_translate("Elevator_schedule", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Elevator_schedule", "电梯2"))
        self.ef3_20.setText(_translate("Elevator_schedule", "20"))
        self.ef3_19.setText(_translate("Elevator_schedule", "19"))
        self.ef3_18.setText(_translate("Elevator_schedule", "18"))
        self.ef3_17.setText(_translate("Elevator_schedule", "17"))
        self.ef3_16.setText(_translate("Elevator_schedule", "16"))
        self.ef3_15.setText(_translate("Elevator_schedule", "15"))
        self.ef3_14.setText(_translate("Elevator_schedule", "14"))
        self.ef3_13.setText(_translate("Elevator_schedule", "13"))
        self.ef3_12.setText(_translate("Elevator_schedule", "12"))
        self.ef3_11.setText(_translate("Elevator_schedule", "11"))
        self.ef3_10.setText(_translate("Elevator_schedule", "10"))
        self.ef3_9.setText(_translate("Elevator_schedule", "9"))
        self.ef3_8.setText(_translate("Elevator_schedule", "8"))
        self.ef3_7.setText(_translate("Elevator_schedule", "7"))
        self.ef3_6.setText(_translate("Elevator_schedule", "6"))
        self.ef3_5.setText(_translate("Elevator_schedule", "5"))
        self.ef3_4.setText(_translate("Elevator_schedule", "4"))
        self.ef3_3.setText(_translate("Elevator_schedule", "3"))
        self.ef3_2.setText(_translate("Elevator_schedule", "2"))
        self.ef3_1.setText(_translate("Elevator_schedule", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Elevator_schedule", "电梯3"))
        self.ef4_20.setText(_translate("Elevator_schedule", "20"))
        self.ef4_19.setText(_translate("Elevator_schedule", "19"))
        self.ef4_18.setText(_translate("Elevator_schedule", "18"))
        self.ef4_17.setText(_translate("Elevator_schedule", "17"))
        self.ef4_16.setText(_translate("Elevator_schedule", "16"))
        self.ef4_15.setText(_translate("Elevator_schedule", "15"))
        self.ef4_14.setText(_translate("Elevator_schedule", "14"))
        self.ef4_13.setText(_translate("Elevator_schedule", "13"))
        self.ef4_12.setText(_translate("Elevator_schedule", "12"))
        self.ef4_11.setText(_translate("Elevator_schedule", "11"))
        self.ef4_10.setText(_translate("Elevator_schedule", "10"))
        self.ef4_9.setText(_translate("Elevator_schedule", "9"))
        self.ef4_8.setText(_translate("Elevator_schedule", "8"))
        self.ef4_7.setText(_translate("Elevator_schedule", "7"))
        self.ef4_6.setText(_translate("Elevator_schedule", "6"))
        self.ef4_5.setText(_translate("Elevator_schedule", "5"))
        self.ef4_4.setText(_translate("Elevator_schedule", "4"))
        self.ef4_3.setText(_translate("Elevator_schedule", "3"))
        self.ef4_2.setText(_translate("Elevator_schedule", "2"))
        self.ef4_1.setText(_translate("Elevator_schedule", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Elevator_schedule", "电梯4"))
        self.ef5_20.setText(_translate("Elevator_schedule", "20"))
        self.ef5_19.setText(_translate("Elevator_schedule", "19"))
        self.ef5_18.setText(_translate("Elevator_schedule", "18"))
        self.ef5_17.setText(_translate("Elevator_schedule", "17"))
        self.ef5_16.setText(_translate("Elevator_schedule", "16"))
        self.ef5_15.setText(_translate("Elevator_schedule", "15"))
        self.ef5_14.setText(_translate("Elevator_schedule", "14"))
        self.ef5_13.setText(_translate("Elevator_schedule", "13"))
        self.ef5_12.setText(_translate("Elevator_schedule", "12"))
        self.ef5_11.setText(_translate("Elevator_schedule", "11"))
        self.ef5_10.setText(_translate("Elevator_schedule", "10"))
        self.ef5_9.setText(_translate("Elevator_schedule", "9"))
        self.ef5_8.setText(_translate("Elevator_schedule", "8"))
        self.ef5_7.setText(_translate("Elevator_schedule", "7"))
        self.ef5_6.setText(_translate("Elevator_schedule", "6"))
        self.ef5_5.setText(_translate("Elevator_schedule", "5"))
        self.ef5_4.setText(_translate("Elevator_schedule", "4"))
        self.ef5_3.setText(_translate("Elevator_schedule", "3"))
        self.ef5_2.setText(_translate("Elevator_schedule", "2"))
        self.ef5_1.setText(_translate("Elevator_schedule", "1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Elevator_schedule", "电梯5"))
    def band_ef_1(self):
        controller.dispatch(0, 1, 1, 0)

    def band_ef_2(self):
        controller.dispatch(0, 1, 2, 0)

    def band_ef_3(self):
        controller.dispatch(0, 1, 3, 0)

    def band_ef_4(self):
        controller.dispatch(0, 1, 4, 0)

    def band_ef_5(self):
        controller.dispatch(0, 1, 5, 0)

    def band_ef_6(self):
        controller.dispatch(0, 1, 6, 0)

    def band_ef_7(self):
        controller.dispatch(0, 1, 7, 0)

    def band_ef_8(self):
        controller.dispatch(0, 1, 8, 0)

    def band_ef_9(self):
        controller.dispatch(0, 1, 9, 0)

    def band_ef_10(self):
        controller.dispatch(0, 1, 10, 0)

    def band_ef_11(self):
        controller.dispatch(0, 1, 11, 0)

    def band_ef_12(self):
        controller.dispatch(0, 1, 12, 0)

    def band_ef_13(self):
        controller.dispatch(0, 1, 13, 0)

    def band_ef_14(self):
        controller.dispatch(0, 1, 14, 0)

    def band_ef_15(self):
        controller.dispatch(0, 1, 15, 0)

    def band_ef_16(self):
        controller.dispatch(0, 1, 16, 0)

    def band_ef_17(self):
        controller.dispatch(0, 1, 17, 0)

    def band_ef_18(self):
        controller.dispatch(0, 1, 18, 0)

    def band_ef_19(self):
        controller.dispatch(0, 1, 19, 0)

    def band_ef_20(self):
        controller.dispatch(0, 1, 20, 0)

    def band_ef2_1(self):
        controller.dispatch(0, 2, 1, 0)

    def band_ef2_2(self):
        controller.dispatch(0, 2, 2, 0)

    def band_ef2_3(self):
        controller.dispatch(0, 2, 3, 0)

    def band_ef2_4(self):
        controller.dispatch(0, 2, 4, 0)

    def band_ef2_5(self):
        controller.dispatch(0, 2, 5, 0)

    def band_ef2_6(self):
        controller.dispatch(0, 2, 6, 0)

    def band_ef2_7(self):
        controller.dispatch(0, 2, 7, 0)

    def band_ef2_8(self):
        controller.dispatch(0, 2, 8, 0)

    def band_ef2_9(self):
        controller.dispatch(0, 2, 9, 0)

    def band_ef2_10(self):
        controller.dispatch(0, 2, 10, 0)

    def band_ef2_11(self):
        controller.dispatch(0, 2, 11, 0)

    def band_ef2_12(self):
        controller.dispatch(0, 2, 12, 0)

    def band_ef2_13(self):
        controller.dispatch(0, 2, 13, 0)

    def band_ef2_14(self):
        controller.dispatch(0, 2, 14, 0)

    def band_ef2_15(self):
        controller.dispatch(0, 2, 15, 0)

    def band_ef2_16(self):
        controller.dispatch(0, 2, 16, 0)

    def band_ef2_17(self):
        controller.dispatch(0, 2, 17, 0)

    def band_ef2_18(self):
        controller.dispatch(0, 2, 18, 0)

    def band_ef2_19(self):
        controller.dispatch(0, 2, 19, 0)

    def band_ef2_20(self):
        controller.dispatch(0, 2, 20, 0)

    def band_ef3_1(self):
        controller.dispatch(0, 3, 1, 0)

    def band_ef3_2(self):
        controller.dispatch(0, 3, 2, 0)

    def band_ef3_3(self):
        controller.dispatch(0, 3, 3, 0)

    def band_ef3_4(self):
        controller.dispatch(0, 3, 4, 0)

    def band_ef3_5(self):
        controller.dispatch(0, 3, 5, 0)

    def band_ef3_6(self):
        controller.dispatch(0, 3, 6, 0)

    def band_ef3_7(self):
        controller.dispatch(0, 3, 7, 0)

    def band_ef3_8(self):
        controller.dispatch(0, 3, 8, 0)

    def band_ef3_9(self):
        controller.dispatch(0, 3, 9, 0)

    def band_ef3_10(self):
        controller.dispatch(0, 3, 10, 0)

    def band_ef3_11(self):
        controller.dispatch(0, 3, 11, 0)

    def band_ef3_12(self):
        controller.dispatch(0, 3, 12, 0)

    def band_ef3_13(self):
        controller.dispatch(0, 3, 13, 0)

    def band_ef3_14(self):
        controller.dispatch(0, 3, 14, 0)

    def band_ef3_15(self):
        controller.dispatch(0, 3, 15, 0)

    def band_ef3_16(self):
        controller.dispatch(0, 3, 16, 0)

    def band_ef3_17(self):
        controller.dispatch(0, 3, 17, 0)

    def band_ef3_18(self):
        controller.dispatch(0, 3, 18, 0)

    def band_ef3_19(self):
        controller.dispatch(0, 3, 19, 0)

    def band_ef3_20(self):
        controller.dispatch(0, 3, 20, 0)

    def band_ef4_1(self):
        controller.dispatch(0, 4, 1, 0)

    def band_ef4_2(self):
        controller.dispatch(0, 4, 2, 0)

    def band_ef4_3(self):
        controller.dispatch(0, 4, 3, 0)

    def band_ef4_4(self):
        controller.dispatch(0, 4, 4, 0)

    def band_ef4_5(self):
        controller.dispatch(0, 4, 5, 0)

    def band_ef4_6(self):
        controller.dispatch(0, 4, 6, 0)

    def band_ef4_7(self):
        controller.dispatch(0, 4, 7, 0)

    def band_ef4_8(self):
        controller.dispatch(0, 4, 8, 0)

    def band_ef4_9(self):
        controller.dispatch(0, 4, 9, 0)

    def band_ef4_10(self):
        controller.dispatch(0, 4, 10, 0)

    def band_ef4_11(self):
        controller.dispatch(0, 4, 11, 0)

    def band_ef4_12(self):
        controller.dispatch(0, 4, 12, 0)

    def band_ef4_13(self):
        controller.dispatch(0, 4, 13, 0)

    def band_ef4_14(self):
        controller.dispatch(0, 4, 14, 0)

    def band_ef4_15(self):
        controller.dispatch(0, 4, 15, 0)

    def band_ef4_16(self):
        controller.dispatch(0, 4, 16, 0)

    def band_ef4_17(self):
        controller.dispatch(0, 4, 17, 0)

    def band_ef4_18(self):
        controller.dispatch(0, 4, 18, 0)

    def band_ef4_19(self):
        controller.dispatch(0, 4, 19, 0)

    def band_ef4_20(self):
        controller.dispatch(0, 4, 20, 0)

    def band_ef5_1(self):
        controller.dispatch(0, 5, 1, 0)

    def band_ef5_2(self):
        controller.dispatch(0, 5, 2, 0)

    def band_ef5_3(self):
        controller.dispatch(0, 5, 3, 0)

    def band_ef5_4(self):
        controller.dispatch(0, 5, 4, 0)

    def band_ef5_5(self):
        controller.dispatch(0, 5, 5, 0)

    def band_ef5_6(self):
        controller.dispatch(0, 5, 6, 0)

    def band_ef5_7(self):
        controller.dispatch(0, 5, 7, 0)

    def band_ef5_8(self):
        controller.dispatch(0, 5, 8, 0)

    def band_ef5_9(self):
        controller.dispatch(0, 5, 9, 0)

    def band_ef5_10(self):
        controller.dispatch(0, 5, 10, 0)

    def band_ef5_11(self):
        controller.dispatch(0, 5, 11, 0)

    def band_ef5_12(self):
        controller.dispatch(0, 5, 12, 0)

    def band_ef5_13(self):
        controller.dispatch(0, 5, 13, 0)

    def band_ef5_14(self):
        controller.dispatch(0, 5, 14, 0)

    def band_ef5_15(self):
        controller.dispatch(0, 5, 15, 0)

    def band_ef5_16(self):
        controller.dispatch(0, 5, 16, 0)

    def band_ef5_17(self):
        controller.dispatch(0, 5, 17, 0)

    def band_ef5_18(self):
        controller.dispatch(0, 5, 18, 0)

    def band_ef5_19(self):
        controller.dispatch(0, 5, 19, 0)

    def band_ef5_20(self):
        controller.dispatch(0, 5, 20, 0)

    def band_down20(self):
        controller.dispatch(1, 0, 20, -1)

    def band_down19(self):
        controller.dispatch(1, 0, 19, -1)

    def band_down18(self):
        controller.dispatch(1, 0, 18, -1)

    def band_down17(self):
        controller.dispatch(1, 0, 17, -1)

    def band_down16(self):
        controller.dispatch(1, 0, 16, -1)

    def band_down15(self):
        controller.dispatch(1, 0, 15, -1)

    def band_down14(self):
        controller.dispatch(1, 0, 14, -1)

    def band_down13(self):
        controller.dispatch(1, 0, 13, -1)

    def band_down12(self):
        controller.dispatch(1, 0, 12, -1)

    def band_down11(self):
        controller.dispatch(1, 0, 11, -1)

    def band_down10(self):
        controller.dispatch(1, 0, 10, -1)

    def band_down9(self):
        controller.dispatch(1, 0, 9, -1)

    def band_down8(self):
        controller.dispatch(1, 0, 8, -1)

    def band_down7(self):
        controller.dispatch(1, 0, 7, -1)

    def band_down6(self):
        controller.dispatch(1, 0, 6, -1)

    def band_down5(self):
        controller.dispatch(1, 0, 5, -1)

    def band_down4(self):
        controller.dispatch(1, 0, 4, -1)

    def band_down3(self):
        controller.dispatch(1, 0, 3, -1)

    def band_down2(self):
        controller.dispatch(1, 0, 2, -1)

    def band_up1(self):
        controller.dispatch(1, 0, 1, 1)

    def band_up2(self):
        controller.dispatch(1, 0, 2, 1)

    def band_up3(self):
        controller.dispatch(1, 0, 3, 1)

    def band_up4(self):
        controller.dispatch(1, 0, 4, 1)

    def band_up5(self):
        controller.dispatch(1, 0, 5, 1)

    def band_up6(self):
        controller.dispatch(1, 0, 6, 1)

    def band_up7(self):
        controller.dispatch(1, 0, 7, 1)

    def band_up8(self):
        controller.dispatch(1, 0, 8, 1)

    def band_up9(self):
        controller.dispatch(1, 0, 9, 1)

    def band_up10(self):
        controller.dispatch(1, 0, 10, 1)

    def band_up11(self):
        controller.dispatch(1, 0, 11, 1)

    def band_up12(self):
        controller.dispatch(1, 0, 12, 1)

    def band_up13(self):
        controller.dispatch(1, 0, 13, 1)

    def band_up14(self):
        controller.dispatch(1, 0, 14, 1)

    def band_up15(self):
        controller.dispatch(1, 0, 15, 1)

    def band_up16(self):
        controller.dispatch(1, 0, 16, 1)

    def band_up17(self):
        controller.dispatch(1, 0, 17, 1)

    def band_up18(self):
        controller.dispatch(1, 0, 18, 1)

    def band_up19(self):
        controller.dispatch(1, 0, 19, 1)
    def status_monitor(self):
        while True:
            # elevator1 internal display
            self.lcdNumber_1.display(controller.elevator1.current_floor)
            if controller.elevator1.internal_request[0] == 1:
                self.ef_1.setChecked(True)
            else:
                self.ef_1.setChecked(False)
            if controller.elevator1.internal_request[1] == 1:
                self.ef_2.setChecked(True)
            else:
                self.ef_2.setChecked(False)
            if controller.elevator1.internal_request[2] == 1:
                self.ef_3.setChecked(True)
            else:
                self.ef_3.setChecked(False)
            if controller.elevator1.internal_request[3] == 1:
                self.ef_4.setChecked(True)
            else:
                self.ef_4.setChecked(False)
            if controller.elevator1.internal_request[4] == 1:
                self.ef_5.setChecked(True)
            else:
                self.ef_5.setChecked(False)
            if controller.elevator1.internal_request[5] == 1:
                self.ef_6.setChecked(True)
            else:
                self.ef_6.setChecked(False)
            if controller.elevator1.internal_request[6] == 1:
                self.ef_7.setChecked(True)
            else:
                self.ef_7.setChecked(False)
            if controller.elevator1.internal_request[7] == 1:
                self.ef_8.setChecked(True)
            else:
                self.ef_8.setChecked(False)
            if controller.elevator1.internal_request[8] == 1:
                self.ef_9.setChecked(True)
            else:
                self.ef_9.setChecked(False)
            if controller.elevator1.internal_request[9] == 1:
                self.ef_10.setChecked(True)
            else:
                self.ef_10.setChecked(False)
            if controller.elevator1.internal_request[10] == 1:
                self.ef_11.setChecked(True)
            else:
                self.ef_11.setChecked(False)
            if controller.elevator1.internal_request[11] == 1:
                self.ef_12.setChecked(True)
            else:
                self.ef_12.setChecked(False)
            if controller.elevator1.internal_request[12] == 1:
                self.ef_13.setChecked(True)
            else:
                self.ef_13.setChecked(False)
            if controller.elevator1.internal_request[13] == 1:
                self.ef_14.setChecked(True)
            else:
                self.ef_14.setChecked(False)
            if controller.elevator1.internal_request[14] == 1:
                self.ef_15.setChecked(True)
            else:
                self.ef_15.setChecked(False)
            if controller.elevator1.internal_request[15] == 1:
                self.ef_16.setChecked(True)
            else:
                self.ef_16.setChecked(False)
            if controller.elevator1.internal_request[16] == 1:
                self.ef_17.setChecked(True)
            else:
                self.ef_17.setChecked(False)
            if controller.elevator1.internal_request[17] == 1:
                self.ef_18.setChecked(True)
            else:
                self.ef_18.setChecked(False)
            if controller.elevator1.internal_request[18] == 1:
                self.ef_19.setChecked(True)
            else:
                self.ef_19.setChecked(False)
            if controller.elevator1.internal_request[19] == 1:
                self.ef_20.setChecked(True)
            else:
                self.ef_20.setChecked(False)
            self.elevator1.setValue(int(controller.elevator1.current_floor))
            # elevator2 internal display
            self.lcdNumber_2.display(controller.elevator2.current_floor)
            if controller.elevator2.internal_request[0] == 1:
                self.ef2_1.setChecked(True)
            else:
                self.ef2_1.setChecked(False)
            if controller.elevator2.internal_request[1] == 1:
                self.ef2_2.setChecked(True)
            else:
                self.ef2_2.setChecked(False)
            if controller.elevator2.internal_request[2] == 1:
                self.ef2_3.setChecked(True)
            else:
                self.ef2_3.setChecked(False)
            if controller.elevator2.internal_request[3] == 1:
                self.ef2_4.setChecked(True)
            else:
                self.ef2_4.setChecked(False)
            if controller.elevator2.internal_request[4] == 1:
                self.ef2_5.setChecked(True)
            else:
                self.ef2_5.setChecked(False)
            if controller.elevator2.internal_request[5] == 1:
                self.ef2_6.setChecked(True)
            else:
                self.ef2_6.setChecked(False)
            if controller.elevator2.internal_request[6] == 1:
                self.ef2_7.setChecked(True)
            else:
                self.ef2_7.setChecked(False)
            if controller.elevator2.internal_request[7] == 1:
                self.ef2_8.setChecked(True)
            else:
                self.ef2_8.setChecked(False)
            if controller.elevator2.internal_request[8] == 1:
                self.ef2_9.setChecked(True)
            else:
                self.ef2_9.setChecked(False)
            if controller.elevator2.internal_request[9] == 1:
                self.ef2_10.setChecked(True)
            else:
                self.ef2_10.setChecked(False)
            if controller.elevator2.internal_request[10] == 1:
                self.ef2_11.setChecked(True)
            else:
                self.ef2_11.setChecked(False)
            if controller.elevator2.internal_request[11] == 1:
                self.ef2_12.setChecked(True)
            else:
                self.ef2_12.setChecked(False)
            if controller.elevator2.internal_request[12] == 1:
                self.ef2_13.setChecked(True)
            else:
                self.ef2_13.setChecked(False)
            if controller.elevator2.internal_request[13] == 1:
                self.ef2_14.setChecked(True)
            else:
                self.ef2_14.setChecked(False)
            if controller.elevator2.internal_request[14] == 1:
                self.ef2_15.setChecked(True)
            else:
                self.ef2_15.setChecked(False)
            if controller.elevator2.internal_request[15] == 1:
                self.ef2_16.setChecked(True)
            else:
                self.ef2_16.setChecked(False)
            if controller.elevator2.internal_request[16] == 1:
                self.ef2_17.setChecked(True)
            else:
                self.ef2_17.setChecked(False)
            if controller.elevator2.internal_request[17] == 1:
                self.ef2_18.setChecked(True)
            else:
                self.ef2_18.setChecked(False)
            if controller.elevator2.internal_request[18] == 1:
                self.ef2_19.setChecked(True)
            else:
                self.ef2_19.setChecked(False)
            if controller.elevator2.internal_request[19] == 1:
                self.ef2_20.setChecked(True)
            else:
                self.ef2_20.setChecked(False)
            self.elevator2.setValue(int(controller.elevator2.current_floor))
            # elevator3 internal display
            self.lcdNumber_3.display(controller.elevator3.current_floor)
            if controller.elevator3.internal_request[0] == 1:
                self.ef3_1.setChecked(True)
            else:
                self.ef3_1.setChecked(False)
            if controller.elevator3.internal_request[1] == 1:
                self.ef3_2.setChecked(True)
            else:
                self.ef3_2.setChecked(False)
            if controller.elevator3.internal_request[2] == 1:
                self.ef3_3.setChecked(True)
            else:
                self.ef3_3.setChecked(False)
            if controller.elevator3.internal_request[3] == 1:
                self.ef3_4.setChecked(True)
            else:
                self.ef3_4.setChecked(False)
            if controller.elevator3.internal_request[4] == 1:
                self.ef3_5.setChecked(True)
            else:
                self.ef3_5.setChecked(False)
            if controller.elevator3.internal_request[5] == 1:
                self.ef3_6.setChecked(True)
            else:
                self.ef3_6.setChecked(False)
            if controller.elevator3.internal_request[6] == 1:
                self.ef3_7.setChecked(True)
            else:
                self.ef3_7.setChecked(False)
            if controller.elevator3.internal_request[7] == 1:
                self.ef3_8.setChecked(True)
            else:
                self.ef3_8.setChecked(False)
            if controller.elevator3.internal_request[8] == 1:
                self.ef3_9.setChecked(True)
            else:
                self.ef3_9.setChecked(False)
            if controller.elevator3.internal_request[9] == 1:
                self.ef3_10.setChecked(True)
            else:
                self.ef3_10.setChecked(False)
            if controller.elevator3.internal_request[10] == 1:
                self.ef3_11.setChecked(True)
            else:
                self.ef3_11.setChecked(False)
            if controller.elevator3.internal_request[11] == 1:
                self.ef3_12.setChecked(True)
            else:
                self.ef3_12.setChecked(False)
            if controller.elevator3.internal_request[12] == 1:
                self.ef3_13.setChecked(True)
            else:
                self.ef3_13.setChecked(False)
            if controller.elevator3.internal_request[13] == 1:
                self.ef3_14.setChecked(True)
            else:
                self.ef3_14.setChecked(False)
            if controller.elevator3.internal_request[14] == 1:
                self.ef3_15.setChecked(True)
            else:
                self.ef3_15.setChecked(False)
            if controller.elevator3.internal_request[15] == 1:
                self.ef3_16.setChecked(True)
            else:
                self.ef3_16.setChecked(False)
            if controller.elevator3.internal_request[16] == 1:
                self.ef3_17.setChecked(True)
            else:
                self.ef3_17.setChecked(False)
            if controller.elevator3.internal_request[17] == 1:
                self.ef3_18.setChecked(True)
            else:
                self.ef3_18.setChecked(False)
            if controller.elevator3.internal_request[18] == 1:
                self.ef3_19.setChecked(True)
            else:
                self.ef3_19.setChecked(False)
            if controller.elevator3.internal_request[19] == 1:
                self.ef3_20.setChecked(True)
            else:
                self.ef3_20.setChecked(False)
            self.elevator3.setValue(int(controller.elevator3.current_floor))
            # elevator4 internal display
            self.lcdNumber_4.display(controller.elevator4.current_floor)
            if controller.elevator4.internal_request[0] == 1:
                self.ef4_1.setChecked(True)
            else:
                self.ef4_1.setChecked(False)
            if controller.elevator4.internal_request[1] == 1:
                self.ef4_2.setChecked(True)
            else:
                self.ef4_2.setChecked(False)
            if controller.elevator4.internal_request[2] == 1:
                self.ef4_3.setChecked(True)
            else:
                self.ef4_3.setChecked(False)
            if controller.elevator4.internal_request[3] == 1:
                self.ef4_4.setChecked(True)
            else:
                self.ef4_4.setChecked(False)
            if controller.elevator4.internal_request[4] == 1:
                self.ef4_5.setChecked(True)
            else:
                self.ef4_5.setChecked(False)
            if controller.elevator4.internal_request[5] == 1:
                self.ef4_6.setChecked(True)
            else:
                self.ef4_6.setChecked(False)
            if controller.elevator4.internal_request[6] == 1:
                self.ef4_7.setChecked(True)
            else:
                self.ef4_7.setChecked(False)
            if controller.elevator4.internal_request[7] == 1:
                self.ef4_8.setChecked(True)
            else:
                self.ef4_8.setChecked(False)
            if controller.elevator4.internal_request[8] == 1:
                self.ef4_9.setChecked(True)
            else:
                self.ef4_9.setChecked(False)
            if controller.elevator4.internal_request[9] == 1:
                self.ef4_10.setChecked(True)
            else:
                self.ef4_10.setChecked(False)
            if controller.elevator4.internal_request[10] == 1:
                self.ef4_11.setChecked(True)
            else:
                self.ef4_11.setChecked(False)
            if controller.elevator4.internal_request[11] == 1:
                self.ef4_12.setChecked(True)
            else:
                self.ef4_12.setChecked(False)
            if controller.elevator4.internal_request[12] == 1:
                self.ef4_13.setChecked(True)
            else:
                self.ef4_13.setChecked(False)
            if controller.elevator4.internal_request[13] == 1:
                self.ef4_14.setChecked(True)
            else:
                self.ef4_14.setChecked(False)
            if controller.elevator4.internal_request[14] == 1:
                self.ef4_15.setChecked(True)
            else:
                self.ef4_15.setChecked(False)
            if controller.elevator4.internal_request[15] == 1:
                self.ef4_16.setChecked(True)
            else:
                self.ef4_16.setChecked(False)
            if controller.elevator4.internal_request[16] == 1:
                self.ef4_17.setChecked(True)
            else:
                self.ef4_17.setChecked(False)
            if controller.elevator4.internal_request[17] == 1:
                self.ef4_18.setChecked(True)
            else:
                self.ef4_18.setChecked(False)
            if controller.elevator4.internal_request[18] == 1:
                self.ef4_19.setChecked(True)
            else:
                self.ef4_19.setChecked(False)
            if controller.elevator4.internal_request[19] == 1:
                self.ef4_20.setChecked(True)
            else:
                self.ef4_20.setChecked(False)
            self.elevator4.setValue(int(controller.elevator4.current_floor))
            # elevator5 internal display
            self.lcdNumber_5.display(controller.elevator5.current_floor)
            if controller.elevator5.internal_request[0] == 1:
                self.ef5_1.setChecked(True)
            else:
                self.ef5_1.setChecked(False)
            if controller.elevator5.internal_request[1] == 1:
                self.ef5_2.setChecked(True)
            else:
                self.ef5_2.setChecked(False)
            if controller.elevator5.internal_request[2] == 1:
                self.ef5_3.setChecked(True)
            else:
                self.ef5_3.setChecked(False)
            if controller.elevator5.internal_request[3] == 1:
                self.ef5_4.setChecked(True)
            else:
                self.ef5_4.setChecked(False)
            if controller.elevator5.internal_request[4] == 1:
                self.ef5_5.setChecked(True)
            else:
                self.ef5_5.setChecked(False)
            if controller.elevator5.internal_request[5] == 1:
                self.ef5_6.setChecked(True)
            else:
                self.ef5_6.setChecked(False)
            if controller.elevator5.internal_request[6] == 1:
                self.ef5_7.setChecked(True)
            else:
                self.ef5_7.setChecked(False)
            if controller.elevator5.internal_request[7] == 1:
                self.ef5_8.setChecked(True)
            else:
                self.ef5_8.setChecked(False)
            if controller.elevator5.internal_request[8] == 1:
                self.ef5_9.setChecked(True)
            else:
                self.ef5_9.setChecked(False)
            if controller.elevator5.internal_request[9] == 1:
                self.ef5_10.setChecked(True)
            else:
                self.ef5_10.setChecked(False)
            if controller.elevator5.internal_request[10] == 1:
                self.ef5_11.setChecked(True)
            else:
                self.ef5_11.setChecked(False)
            if controller.elevator5.internal_request[11] == 1:
                self.ef5_12.setChecked(True)
            else:
                self.ef5_12.setChecked(False)
            if controller.elevator5.internal_request[12] == 1:
                self.ef5_13.setChecked(True)
            else:
                self.ef5_13.setChecked(False)
            if controller.elevator5.internal_request[13] == 1:
                self.ef5_14.setChecked(True)
            else:
                self.ef5_14.setChecked(False)
            if controller.elevator5.internal_request[14] == 1:
                self.ef5_15.setChecked(True)
            else:
                self.ef5_15.setChecked(False)
            if controller.elevator5.internal_request[15] == 1:
                self.ef5_16.setChecked(True)
            else:
                self.ef5_16.setChecked(False)
            if controller.elevator5.internal_request[16] == 1:
                self.ef5_17.setChecked(True)
            else:
                self.ef5_17.setChecked(False)
            if controller.elevator5.internal_request[17] == 1:
                self.ef5_18.setChecked(True)
            else:
                self.ef5_18.setChecked(False)
            if controller.elevator5.internal_request[18] == 1:
                self.ef5_19.setChecked(True)
            else:
                self.ef5_19.setChecked(False)
            if controller.elevator5.internal_request[19] == 1:
                self.ef5_20.setChecked(True)
            else:
                self.ef5_20.setChecked(False)
            self.elevator5.setValue(int(controller.elevator5.current_floor))
            # Set the buttons
            if controller.elevator1.external_request[0] == 1 or controller.elevator2.external_request[0] == 1 \
                    or controller.elevator3.external_request[0] == 1 or controller.elevator4.external_request[0] == 1 \
                    or controller.elevator5.external_request[0] == 1:
                self.up_1.setChecked(True)
            else:
                self.up_1.setChecked(False)
            if controller.elevator1.external_request[1] == 1 or controller.elevator2.external_request[1] == 1 \
                    or controller.elevator3.external_request[1] == 1 or controller.elevator4.external_request[1] == 1 \
                    or controller.elevator5.external_request[1] == 1:
                self.up_2.setChecked(True)
            else:
                self.up_2.setChecked(False)
            if controller.elevator1.external_request[2] == 1 or controller.elevator2.external_request[2] == 1 \
                    or controller.elevator3.external_request[2] == 1 or controller.elevator4.external_request[2] == 1 \
                    or controller.elevator5.external_request[2] == 1:
                self.up_3.setChecked(True)
            else:
                self.up_3.setChecked(False)
            if controller.elevator1.external_request[3] == 1 or controller.elevator2.external_request[3] == 1 \
                    or controller.elevator3.external_request[3] == 1 or controller.elevator4.external_request[3] == 1 \
                    or controller.elevator5.external_request[3] == 1:
                self.up_4.setChecked(True)
            else:
                self.up_4.setChecked(False)
            if controller.elevator1.external_request[4] == 1 or controller.elevator2.external_request[4] == 1 \
                    or controller.elevator3.external_request[4] == 1 or controller.elevator4.external_request[4] == 1 \
                    or controller.elevator5.external_request[4] == 1:
                self.up_5.setChecked(True)
            else:
                self.up_5.setChecked(False)
            if controller.elevator1.external_request[5] == 1 or controller.elevator2.external_request[5] == 1 \
                    or controller.elevator3.external_request[5] == 1 or controller.elevator4.external_request[5] == 1 \
                    or controller.elevator5.external_request[5] == 1:
                self.up_6.setChecked(True)
            else:
                self.up_6.setChecked(False)
            if controller.elevator1.external_request[6] == 1 or controller.elevator2.external_request[6] == 1 \
                    or controller.elevator3.external_request[6] == 1 or controller.elevator4.external_request[6] == 1 \
                    or controller.elevator5.external_request[6] == 1:
                self.up_7.setChecked(True)
            else:
                self.up_7.setChecked(False)
            if controller.elevator1.external_request[7] == 1 or controller.elevator2.external_request[7] == 1 \
                    or controller.elevator3.external_request[7] == 1 or controller.elevator4.external_request[7] == 1 \
                    or controller.elevator5.external_request[7] == 1:
                self.up_8.setChecked(True)
            else:
                self.up_8.setChecked(False)
            if controller.elevator1.external_request[8] == 1 or controller.elevator2.external_request[8] == 1 \
                    or controller.elevator3.external_request[8] == 1 or controller.elevator4.external_request[8] == 1 \
                    or controller.elevator5.external_request[8] == 1:
                self.up_9.setChecked(True)
            else:
                self.up_9.setChecked(False)
            if controller.elevator1.external_request[9] == 1 or controller.elevator2.external_request[9] == 1 \
                    or controller.elevator3.external_request[9] == 1 or controller.elevator4.external_request[9] == 1 \
                    or controller.elevator5.external_request[9] == 1:
                self.up_10.setChecked(True)
            else:
                self.up_10.setChecked(False)
            if controller.elevator1.external_request[10] == 1 or controller.elevator2.external_request[10] == 1 \
                    or controller.elevator3.external_request[10] == 1 or controller.elevator4.external_request[10] == 1 \
                    or controller.elevator5.external_request[10] == 1:
                self.up_11.setChecked(True)
            else:
                self.up_11.setChecked(False)
            if controller.elevator1.external_request[11] == 1 or controller.elevator2.external_request[11] == 1 \
                    or controller.elevator3.external_request[11] == 1 or controller.elevator4.external_request[11] == 1 \
                    or controller.elevator5.external_request[11] == 1:
                self.up_12.setChecked(True)
            else:
                self.up_12.setChecked(False)
            if controller.elevator1.external_request[12] == 1 or controller.elevator2.external_request[12] == 1 \
                    or controller.elevator3.external_request[12] == 1 or controller.elevator4.external_request[12] == 1 \
                    or controller.elevator5.external_request[12] == 1:
                self.up_13.setChecked(True)
            else:
                self.up_13.setChecked(False)
            if controller.elevator1.external_request[13] == 1 or controller.elevator2.external_request[13] == 1 \
                    or controller.elevator3.external_request[13] == 1 or controller.elevator4.external_request[13] == 1 \
                    or controller.elevator5.external_request[13] == 1:
                self.up_14.setChecked(True)
            else:
                self.up_14.setChecked(False)
            if controller.elevator1.external_request[14] == 1 or controller.elevator2.external_request[14] == 1 \
                    or controller.elevator3.external_request[14] == 1 or controller.elevator4.external_request[14] == 1 \
                    or controller.elevator5.external_request[14] == 1:
                self.up_15.setChecked(True)
            else:
                self.up_15.setChecked(False)
            if controller.elevator1.external_request[15] == 1 or controller.elevator2.external_request[15] == 1 \
                    or controller.elevator3.external_request[15] == 1 or controller.elevator4.external_request[15] == 1 \
                    or controller.elevator5.external_request[15] == 1:
                self.up_16.setChecked(True)
            else:
                self.up_16.setChecked(False)
            if controller.elevator1.external_request[16] == 1 or controller.elevator2.external_request[16] == 1 \
                    or controller.elevator3.external_request[16] == 1 or controller.elevator4.external_request[16] == 1 \
                    or controller.elevator5.external_request[16] == 1:
                self.up_17.setChecked(True)
            else:
                self.up_17.setChecked(False)
            if controller.elevator1.external_request[17] == 1 or controller.elevator2.external_request[17] == 1 \
                    or controller.elevator3.external_request[17] == 1 or controller.elevator4.external_request[17] == 1 \
                    or controller.elevator5.external_request[17] == 1:
                self.up_18.setChecked(True)
            else:
                self.up_18.setChecked(False)
            if controller.elevator1.external_request[18] == 1 or controller.elevator2.external_request[18] == 1 \
                    or controller.elevator3.external_request[18] == 1 or controller.elevator4.external_request[18] == 1 \
                    or controller.elevator5.external_request[18] == 1:
                self.up_19.setChecked(True)
            else:
                self.up_19.setChecked(False)

            if controller.elevator1.external_request[19] == -1 or controller.elevator2.external_request[19] == -1 \
                    or controller.elevator3.external_request[19] == -1 or controller.elevator4.external_request[19] == -1 \
                    or controller.elevator5.external_request[19] == -1:
                self.down_20.setChecked(True)
            else:
                self.down_20.setChecked(False)
            if controller.elevator1.external_request[18] == -1 or controller.elevator2.external_request[18] == -1 \
                    or controller.elevator3.external_request[18] == -1 or controller.elevator4.external_request[18] == -1 \
                    or controller.elevator5.external_request[18] == -1:
                self.down_19.setChecked(True)
            else:
                self.down_19.setChecked(False)
            if controller.elevator1.external_request[17] == -1 or controller.elevator2.external_request[17] == -1 \
                    or controller.elevator3.external_request[17] == -1 or controller.elevator4.external_request[17] == -1 \
                    or controller.elevator5.external_request[17] == -1:
                self.down_18.setChecked(True)
            else:
                self.down_18.setChecked(False)
            if controller.elevator1.external_request[16] == -1 or controller.elevator2.external_request[16] == -1 \
                    or controller.elevator3.external_request[16] == -1 or controller.elevator4.external_request[16] == -1 \
                    or controller.elevator5.external_request[16] == -1:
                self.down_17.setChecked(True)
            else:
                self.down_17.setChecked(False)
            if controller.elevator1.external_request[15] == -1 or controller.elevator2.external_request[15] == -1 \
                    or controller.elevator3.external_request[15] == -1 or controller.elevator4.external_request[15] == -1 \
                    or controller.elevator5.external_request[15] == -1:
                self.down_16.setChecked(True)
            else:
                self.down_16.setChecked(False)
            if controller.elevator1.external_request[14] == -1 or controller.elevator2.external_request[14] == -1 \
                    or controller.elevator3.external_request[14] == -1 or controller.elevator4.external_request[14] == -1 \
                    or controller.elevator5.external_request[14] == -1:
                self.down_15.setChecked(True)
            else:
                self.down_15.setChecked(False)
            if controller.elevator1.external_request[13] == -1 or controller.elevator2.external_request[13] == -1 \
                    or controller.elevator3.external_request[13] == -1 or controller.elevator4.external_request[13] == -1 \
                    or controller.elevator5.external_request[13] == -1:
                self.down_14.setChecked(True)
            else:
                self.down_14.setChecked(False)
            if controller.elevator1.external_request[12] == -1 or controller.elevator2.external_request[12] == -1 \
                    or controller.elevator3.external_request[12] == -1 or controller.elevator4.external_request[12] == -1 \
                    or controller.elevator5.external_request[12] == -1:
                self.down_13.setChecked(True)
            else:
                self.down_13.setChecked(False)
            if controller.elevator1.external_request[11] == -1 or controller.elevator2.external_request[11] == -1 \
                    or controller.elevator3.external_request[11] == -1 or controller.elevator4.external_request[11] == -1 \
                    or controller.elevator5.external_request[11] == -1:
                self.down_12.setChecked(True)
            else:
                self.down_12.setChecked(False)
            if controller.elevator1.external_request[10] == -1 or controller.elevator2.external_request[10] == -1 \
                    or controller.elevator3.external_request[10] == -1 or controller.elevator4.external_request[10] == -1 \
                    or controller.elevator5.external_request[10] == -1:
                self.down_11.setChecked(True)
            else:
                self.down_11.setChecked(False)
            if controller.elevator1.external_request[9] == -1 or controller.elevator2.external_request[9] == -1 \
                or controller.elevator3.external_request[9] == -1 or controller.elevator4.external_request[9] == -1 \
                or controller.elevator5.external_request[9] == -1:
                self.down_10.setChecked(True)
            else:
                self.down_10.setChecked(False)
            if controller.elevator1.external_request[8] == -1 or controller.elevator2.external_request[8] == -1 \
                    or controller.elevator3.external_request[8] == -1 or controller.elevator4.external_request[8] == -1 \
                    or controller.elevator5.external_request[8] == -1:
                self.down_9.setChecked(True)
            else:
                self.down_9.setChecked(False)
            if controller.elevator1.external_request[7] == -1 or controller.elevator2.external_request[7] == -1 \
                    or controller.elevator3.external_request[7] == -1 or controller.elevator4.external_request[7] == -1 \
                    or controller.elevator5.external_request[7] == -1:
                self.down_8.setChecked(True)
            else:
                self.down_8.setChecked(False)
            if controller.elevator1.external_request[6] == -1 or controller.elevator2.external_request[6] == -1 \
                    or controller.elevator3.external_request[6] == -1 or controller.elevator4.external_request[6] == -1 \
                    or controller.elevator5.external_request[6] == -1:
                self.down_7.setChecked(True)
            else:
                self.down_7.setChecked(False)
            if controller.elevator1.external_request[5] == -1 or controller.elevator2.external_request[5] == -1 \
                    or controller.elevator3.external_request[5] == -1 or controller.elevator4.external_request[5] == -1 \
                    or controller.elevator5.external_request[5] == -1:
                self.down_6.setChecked(True)
            else:
                self.down_6.setChecked(False)
            if controller.elevator1.external_request[4] == -1 or controller.elevator2.external_request[4] == -1 \
                    or controller.elevator3.external_request[4] == -1 or controller.elevator4.external_request[4] == -1 \
                    or controller.elevator5.external_request[4] == -1:
                self.down_5.setChecked(True)
            else:
                self.down_5.setChecked(False)
            if controller.elevator1.external_request[3] == -1 or controller.elevator2.external_request[3] == -1 \
                    or controller.elevator3.external_request[3] == -1 or controller.elevator4.external_request[3] == -1 \
                    or controller.elevator5.external_request[3] == -1:
                self.down_4.setChecked(True)
            else:
                self.down_4.setChecked(False)
            if controller.elevator1.external_request[2] == -1 or controller.elevator2.external_request[2] == -1 \
                    or controller.elevator3.external_request[2] == -1 or controller.elevator4.external_request[2] == -1 \
                    or controller.elevator5.external_request[2] == -1:
                self.down_3.setChecked(True)
            else:
                self.down_3.setChecked(False)
            if controller.elevator1.external_request[1] == -1 or controller.elevator2.external_request[1] == -1 \
                    or controller.elevator3.external_request[1] == -1 or controller.elevator4.external_request[1] == -1 \
                    or controller.elevator5.external_request[1] == -1:
                self.down_2.setChecked(True)
            else:
                self.down_2.setChecked(False)

            time.sleep(0.5)
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Elevator_schedule()

    ui.setupUi(widget)
    widget.show()

    controller = Controller()
    t0 = Thread(target=ui.status_monitor, args=())
    t1 = Thread(target=controller.elevator1.run, args=())
    t2 = Thread(target=controller.elevator2.run, args=())
    t3 = Thread(target=controller.elevator3.run, args=())
    t4 = Thread(target=controller.elevator4.run, args=())
    t5 = Thread(target=controller.elevator5.run, args=())
    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    sys.exit(app.exec_())