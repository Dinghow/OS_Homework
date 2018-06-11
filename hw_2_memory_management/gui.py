# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import sys,time
from PyQt5 import QtCore, QtGui, QtWidgets
from page_replacement import Block,Simulator,generate_list
from threading import Thread


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(685, 553)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 601, 161))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.label_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_1.addWidget(self.label_1)
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_1.setDigitCount(3)
        self.lcdNumber_1.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.verticalLayout_1.addWidget(self.lcdNumber_1)
        self.horizontalLayout.addLayout(self.verticalLayout_1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_2.setDigitCount(3)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalLayout_2.addWidget(self.lcdNumber_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_3.setDigitCount(3)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.verticalLayout_3.addWidget(self.lcdNumber_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_4.setDigitCount(3)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.verticalLayout_4.addWidget(self.lcdNumber_4)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 230, 421, 301))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget_1 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_1.setObjectName("listWidget_1")
        self.verticalLayout.addWidget(self.listWidget_1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_5.addWidget(self.listWidget_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(470, 230, 171, 301))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_6.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_7)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_6.addWidget(self.radioButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_6.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_6.addWidget(self.pushButton_3)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 190, 601, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)

        # Band the buttons
        self.pushButton.clicked.connect(self.generate_list)
        self.pushButton_2.clicked.connect(self.single_step)
        self.pushButton_3.clicked.connect(self.to_end)
        self.radioButton.toggled.connect(self.set_alg_1)
        self.radioButton_2.toggled.connect(self.set_alg_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_1.setText(_translate("Form", "Block 1"))
        self.label_2.setText(_translate("Form", "Block 2"))
        self.label_3.setText(_translate("Form", "Block 3"))
        self.label_4.setText(_translate("Form", "Block 4"))
        self.label.setText(_translate("Form", "Access Sequence"))
        self.label_5.setText(_translate("Form", "Relevant Page "))
        self.radioButton.setText(_translate("Form", "FIFO"))
        self.radioButton_2.setText(_translate("Form", "LRU"))
        self.pushButton.setText(_translate("Form", "Generate List"))
        self.pushButton_2.setText(_translate("Form", "Single Step "))
        self.pushButton_3.setText(_translate("Form", "Execution to End"))
        self.label_6.setText(_translate("Form", "Number of page faults: 0"))
        self.label_7.setText(_translate("Form", "Rate of page faults: 0%"))

    def set_alg_1(self,value):
        if self.radioButton.isChecked():
            self.replacement_algo = 0

    def set_alg_2(self,value):
        if self.radioButton_2.isChecked():
            self.replacement_algo = 1

    def generate_list(self):
        self.step_counter = 0
        self.listWidget_1.setCurrentRow(self.step_counter)
        self.listWidget_2.setCurrentRow(self.step_counter)
        order = 4
        simulator.accessed_all = False
        simulator.missing_page_counter = 0
        for i in simulator.blocks:
            i.page = -1
            i.time = order
            i.accessed = False
            order -= 1

        self.refresh_display()
        instructions, pages = generate_list()
        self.listWidget_1.clear()
        self.listWidget_2.clear()
        for i in instructions:
            self.listWidget_1.addItem(str(i))
        for i in pages:
            self.listWidget_2.addItem(str(i))

    def single_step(self):
        self.listWidget_1.setCurrentRow(self.step_counter)
        self.listWidget_2.setCurrentRow(self.step_counter)
        new_page = self.listWidget_2.item(self.step_counter).text()
        self.step_counter += 1
        self.refresh_display()
        self.label_6.setText("Number of page faults: "+ str(simulator.missing_page_counter))
        self.label_7.setText("Rate of page faults: "+ str(round((100*simulator.missing_page_counter/self.step_counter),2))+ '%')

        simulator.access_new_page(int(new_page),self.replacement_algo)

    def run_to_end(self):
        while self.step_counter <= 317:
            self.single_step()
            time.sleep(0.1)

    def to_end(self):
        t0 = Thread(target=self.run_to_end,args=())
        t0.start()

    def refresh_display(self):
        self.lcdNumber_1.display(simulator.blocks[0].page)
        self.lcdNumber_2.display(simulator.blocks[1].page)
        self.lcdNumber_3.display(simulator.blocks[2].page)
        self.lcdNumber_4.display(simulator.blocks[3].page)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    simulator = Simulator()

    ui.setupUi(widget)
    widget.show()

    sys.exit(app.exec_())