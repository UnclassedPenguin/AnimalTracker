# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genealogywindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(302, 270)
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(74, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 3, 0, 1, 1)
        self.halfmothercbButton = QtWidgets.QRadioButton(self.frame)
        self.halfmothercbButton.setObjectName("halfmothercbButton")
        self.gridLayout_2.addWidget(self.halfmothercbButton, 5, 1, 1, 3)
        self.nohalfcbButton = QtWidgets.QRadioButton(self.frame)
        self.nohalfcbButton.setChecked(True)
        self.nohalfcbButton.setObjectName("nohalfcbButton")
        self.gridLayout_2.addWidget(self.nohalfcbButton, 3, 1, 1, 2)
        self.halffathercbButton = QtWidgets.QRadioButton(self.frame)
        self.halffathercbButton.setObjectName("halffathercbButton")
        self.gridLayout_2.addWidget(self.halffathercbButton, 4, 1, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 8, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.frame)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_2.addWidget(self.nameEdit, 1, 2, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 4, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(6, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 6, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 2)
        self.closeButton = QtWidgets.QPushButton(self.frame)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout_2.addWidget(self.closeButton, 8, 3, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.frame)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout_2.addWidget(self.searchButton, 8, 2, 1, 1)
        self.testButton = QtWidgets.QPushButton(self.frame)
        self.testButton.setObjectName("testButton")
        self.gridLayout_2.addWidget(self.testButton, 6, 3, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Animal Tracker - Genealogy"))
        self.label.setText(_translate("MainWindow", "Name: "))
        self.halfmothercbButton.setText(_translate("MainWindow", "Half Siblings with mother"))
        self.nohalfcbButton.setText(_translate("MainWindow", "No half siblings"))
        self.halffathercbButton.setText(_translate("MainWindow", "Half siblings with father"))
        self.label_3.setText(_translate("MainWindow", "Half Siblings: "))
        self.label_2.setText(_translate("MainWindow", "Genealogy  "))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.testButton.setText(_translate("MainWindow", "Test"))

