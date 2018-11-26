# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genealogywindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
'''
Copyright © 2018 UnclassedPenguin
App: Animal Tracker
Author: UnclassedPenguin
Description: An app to keep track of your Animals
'''
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 318)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(175, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.frame)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_2.addWidget(self.nameEdit, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 1)
        self.nohalfcbButton = QtWidgets.QRadioButton(self.frame)
        self.nohalfcbButton.setChecked(True)
        self.nohalfcbButton.setObjectName("nohalfcbButton")
        self.gridLayout_2.addWidget(self.nohalfcbButton, 4, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 5, 0, 1, 1)
        self.halffathercbButton = QtWidgets.QRadioButton(self.frame)
        self.halffathercbButton.setObjectName("halffathercbButton")
        self.gridLayout_2.addWidget(self.halffathercbButton, 5, 1, 1, 3)
        self.halfmothercbButton = QtWidgets.QRadioButton(self.frame)
        self.halfmothercbButton.setObjectName("halfmothercbButton")
        self.gridLayout_2.addWidget(self.halfmothercbButton, 6, 1, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 7, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 8, 0, 1, 1)
        self.testButton = QtWidgets.QPushButton(self.frame)
        self.testButton.setObjectName("testButton")
        self.gridLayout_2.addWidget(self.testButton, 8, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 8, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 9, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(89, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 9, 1, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.frame)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 9, 2, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 9, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 9, 4, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Animal Tracker - Genealogy"))
        self.label_2.setText(_translate("MainWindow", "Genealogy  "))
        self.label.setText(_translate("MainWindow", "Name: "))
        self.label_3.setText(_translate("MainWindow", "Half Siblings: "))
        self.nohalfcbButton.setText(_translate("MainWindow", "No half siblings"))
        self.halffathercbButton.setText(_translate("MainWindow", "Half siblings with father"))
        self.halfmothercbButton.setText(_translate("MainWindow", "Half Siblings with mother"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.closeButton.setText(_translate("MainWindow", "Close"))

