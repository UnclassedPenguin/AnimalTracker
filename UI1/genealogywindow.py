# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genealogywindow3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(288, 255)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.halfmothercbButton = QtWidgets.QRadioButton(self.centralwidget)
        self.halfmothercbButton.setObjectName("halfmothercbButton")
        self.gridLayout.addWidget(self.halfmothercbButton, 5, 3, 1, 2)
        self.halffathercbButton = QtWidgets.QRadioButton(self.centralwidget)
        self.halffathercbButton.setObjectName("halffathercbButton")
        self.gridLayout.addWidget(self.halffathercbButton, 6, 3, 2, 2)
        self.nohalfcbButton = QtWidgets.QRadioButton(self.centralwidget)
        self.nohalfcbButton.setChecked(True)
        self.nohalfcbButton.setObjectName("nohalfcbButton")
        self.gridLayout.addWidget(self.nohalfcbButton, 4, 3, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 2, 3, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 3, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 8, 4, 1, 1)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.closeButton.setFont(font)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 9, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 10, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Animal Tracker - Genealogy"))
        self.label.setText(_translate("MainWindow", "Name: "))
        self.halfmothercbButton.setText(_translate("MainWindow", "Half Siblings with mother"))
        self.halffathercbButton.setText(_translate("MainWindow", "Half siblings with father"))
        self.nohalfcbButton.setText(_translate("MainWindow", "No half siblings"))
        self.label_3.setText(_translate("MainWindow", "Half Siblings: "))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.label_2.setText(_translate("MainWindow", "Genealogy  "))
