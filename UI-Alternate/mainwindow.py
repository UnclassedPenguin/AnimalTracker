# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setMinimumSize(QtCore.QSize(100, 0))
        self.quitButton.setMaximumSize(QtCore.QSize(2344234, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 15, 5, 1, 1)
        self.bodyconButton4 = QtWidgets.QRadioButton(self.centralwidget)
        self.bodyconButton4.setObjectName("bodyconButton4")
        self.bodyconGroup = QtWidgets.QButtonGroup(MainWindow)
        self.bodyconGroup.setObjectName("bodyconGroup")
        self.bodyconGroup.addButton(self.bodyconButton4)
        self.gridLayout.addWidget(self.bodyconButton4, 9, 4, 1, 1)
        self.nameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEntry.setMaximumSize(QtCore.QSize(2344234, 16777215))
        self.nameEntry.setObjectName("nameEntry")
        self.gridLayout.addWidget(self.nameEntry, 6, 1, 1, 1)
        self.hoofconButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.hoofconButton2.setObjectName("hoofconButton2")
        self.hoofconGroup = QtWidgets.QButtonGroup(MainWindow)
        self.hoofconGroup.setObjectName("hoofconGroup")
        self.hoofconGroup.addButton(self.hoofconButton2)
        self.gridLayout.addWidget(self.hoofconButton2, 9, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)
        self.dateLabel = QtWidgets.QLabel(self.centralwidget)
        self.dateLabel.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.dateLabel.setFont(font)
        self.dateLabel.setText("")
        self.dateLabel.setObjectName("dateLabel")
        self.gridLayout.addWidget(self.dateLabel, 1, 0, 1, 2)
        self.bodyconButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.bodyconButton2.setObjectName("bodyconButton2")
        self.bodyconGroup.addButton(self.bodyconButton2)
        self.gridLayout.addWidget(self.bodyconButton2, 11, 4, 1, 1)
        self.idEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.idEntry.setMaximumSize(QtCore.QSize(2344234, 16777215))
        self.idEntry.setObjectName("idEntry")
        self.gridLayout.addWidget(self.idEntry, 4, 1, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 6, 2, 1, 1)
        self.optionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.optionsButton.setMinimumSize(QtCore.QSize(100, 0))
        self.optionsButton.setMaximumSize(QtCore.QSize(2344234, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.optionsButton.setFont(font)
        self.optionsButton.setObjectName("optionsButton")
        self.gridLayout.addWidget(self.optionsButton, 14, 5, 1, 1)
        self.bdayEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.bdayEntry.setMinimumSize(QtCore.QSize(125, 0))
        self.bdayEntry.setMaximumSize(QtCore.QSize(2344234, 16777215))
        self.bdayEntry.setObjectName("bdayEntry")
        self.gridLayout.addWidget(self.bdayEntry, 6, 4, 1, 1)
        self.advsearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.advsearchButton.setMinimumSize(QtCore.QSize(100, 0))
        self.advsearchButton.setMaximumSize(QtCore.QSize(2344234, 16777215))
        self.advsearchButton.setSizeIncrement(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.advsearchButton.setFont(font)
        self.advsearchButton.setObjectName("advsearchButton")
        self.gridLayout.addWidget(self.advsearchButton, 13, 5, 1, 1)
        self.weightEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.weightEntry.setMinimumSize(QtCore.QSize(125, 0))
        self.weightEntry.setMaximumSize(QtCore.QSize(2344234, 16777215))
        self.weightEntry.setObjectName("weightEntry")
        self.gridLayout.addWidget(self.weightEntry, 6, 3, 1, 1)
        self.genderButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.genderButton1.setObjectName("genderButton1")
        self.genderGroup = QtWidgets.QButtonGroup(MainWindow)
        self.genderGroup.setObjectName("genderGroup")
        self.genderGroup.addButton(self.genderButton1)
        self.gridLayout.addWidget(self.genderButton1, 14, 3, 1, 1)
        self.notesEntry = QtWidgets.QTextEdit(self.centralwidget)
        self.notesEntry.setMinimumSize(QtCore.QSize(300, 0))
        self.notesEntry.setMaximumSize(QtCore.QSize(2344234, 16777215))
        self.notesEntry.setObjectName("notesEntry")
        self.gridLayout.addWidget(self.notesEntry, 8, 0, 9, 3)
        self.genderButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.genderButton2.setObjectName("genderButton2")
        self.genderGroup.addButton(self.genderButton2)
        self.gridLayout.addWidget(self.genderButton2, 13, 3, 1, 1)
        self.bodyconButton3 = QtWidgets.QRadioButton(self.centralwidget)
        self.bodyconButton3.setObjectName("bodyconButton3")
        self.bodyconGroup.addButton(self.bodyconButton3)
        self.gridLayout.addWidget(self.bodyconButton3, 10, 4, 1, 1)
        self.bodyconButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.bodyconButton1.setObjectName("bodyconButton1")
        self.bodyconGroup.addButton(self.bodyconButton1)
        self.gridLayout.addWidget(self.bodyconButton1, 12, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QComboBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout.addWidget(self.groupBox, 2, 1, 1, 1)
        self.addgroupButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.addgroupButton.setFont(font)
        self.addgroupButton.setObjectName("addgroupButton")
        self.gridLayout.addWidget(self.addgroupButton, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.rfidEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.rfidEntry.setMaximumSize(QtCore.QSize(2344234, 16777215))
        self.rfidEntry.setObjectName("rfidEntry")
        self.gridLayout.addWidget(self.rfidEntry, 3, 1, 1, 1)
        self.bodyconButton5 = QtWidgets.QRadioButton(self.centralwidget)
        self.bodyconButton5.setChecked(True)
        self.bodyconButton5.setObjectName("bodyconButton5")
        self.bodyconGroup.addButton(self.bodyconButton5)
        self.gridLayout.addWidget(self.bodyconButton5, 8, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.fatherEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.fatherEntry.setMinimumSize(QtCore.QSize(125, 0))
        self.fatherEntry.setMaximumSize(QtCore.QSize(2344234, 16777215))
        self.fatherEntry.setObjectName("fatherEntry")
        self.gridLayout.addWidget(self.fatherEntry, 3, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 4, 1, 1)
        self.motherEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.motherEntry.setMinimumSize(QtCore.QSize(125, 0))
        self.motherEntry.setMaximumSize(QtCore.QSize(2344234, 16777215))
        self.motherEntry.setObjectName("motherEntry")
        self.gridLayout.addWidget(self.motherEntry, 3, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 4, 1, 1)
        self.genderButton3 = QtWidgets.QRadioButton(self.centralwidget)
        self.genderButton3.setChecked(True)
        self.genderButton3.setObjectName("genderButton3")
        self.genderGroup.addButton(self.genderButton3)
        self.gridLayout.addWidget(self.genderButton3, 12, 3, 1, 1)
        self.hoofconButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.hoofconButton1.setObjectName("hoofconButton1")
        self.hoofconGroup.addButton(self.hoofconButton1)
        self.gridLayout.addWidget(self.hoofconButton1, 10, 3, 1, 1)
        self.hoofconButton3 = QtWidgets.QRadioButton(self.centralwidget)
        self.hoofconButton3.setChecked(True)
        self.hoofconButton3.setObjectName("hoofconButton3")
        self.hoofconGroup.addButton(self.hoofconButton3)
        self.gridLayout.addWidget(self.hoofconButton3, 8, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 3, 1, 1)
        self.soldButton = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.soldButton.setFont(font)
        self.soldButton.setToolTipDuration(-3)
        self.soldButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.soldButton.setObjectName("soldButton")
        self.gridLayout.addWidget(self.soldButton, 14, 4, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setMinimumSize(QtCore.QSize(100, 0))
        self.clearButton.setMaximumSize(QtCore.QSize(2344234, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 12, 5, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setMinimumSize(QtCore.QSize(100, 0))
        self.saveButton.setMaximumSize(QtCore.QSize(2344234, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 11, 5, 1, 1)
        self.displayallButton = QtWidgets.QPushButton(self.centralwidget)
        self.displayallButton.setMinimumSize(QtCore.QSize(100, 0))
        self.displayallButton.setMaximumSize(QtCore.QSize(2344234, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.displayallButton.setFont(font)
        self.displayallButton.setObjectName("displayallButton")
        self.gridLayout.addWidget(self.displayallButton, 10, 5, 1, 1)
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setMinimumSize(QtCore.QSize(100, 0))
        self.testButton.setMaximumSize(QtCore.QSize(2344234, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.testButton.setFont(font)
        self.testButton.setObjectName("testButton")
        self.gridLayout.addWidget(self.testButton, 9, 5, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Animal Tracker"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
        self.bodyconButton4.setText(_translate("MainWindow", "4"))
        self.hoofconButton2.setText(_translate("MainWindow", "OK"))
        self.label_9.setText(_translate("MainWindow", "Father"))
        self.bodyconButton2.setText(_translate("MainWindow", "2"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.optionsButton.setText(_translate("MainWindow", "Options"))
        self.advsearchButton.setText(_translate("MainWindow", "Adv. Search"))
        self.genderButton1.setText(_translate("MainWindow", "Weather"))
        self.genderButton2.setText(_translate("MainWindow", "Male"))
        self.bodyconButton3.setText(_translate("MainWindow", "3"))
        self.bodyconButton1.setText(_translate("MainWindow", "1 (Bad)"))
        self.label.setText(_translate("MainWindow", "Group"))
        self.addgroupButton.setText(_translate("MainWindow", "Add Group"))
        self.label_2.setText(_translate("MainWindow", "RFID:"))
        self.bodyconButton5.setText(_translate("MainWindow", "5 (Good)"))
        self.label_6.setText(_translate("MainWindow", "Notes"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_3.setText(_translate("MainWindow", "ID:"))
        self.label_13.setText(_translate("MainWindow", "Body Condition"))
        self.label_10.setText(_translate("MainWindow", "Weight"))
        self.label_8.setText(_translate("MainWindow", "Mother"))
        self.label_11.setText(_translate("MainWindow", "Birthday"))
        self.genderButton3.setText(_translate("MainWindow", "Female"))
        self.hoofconButton1.setText(_translate("MainWindow", "Bad"))
        self.hoofconButton3.setText(_translate("MainWindow", "Good"))
        self.label_14.setText(_translate("MainWindow", "Hoof Condition"))
        self.label_12.setText(_translate("MainWindow", "Gender"))
        self.soldButton.setText(_translate("MainWindow", "Sold"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.displayallButton.setText(_translate("MainWindow", "Display All"))
        self.testButton.setText(_translate("MainWindow", "Test"))

