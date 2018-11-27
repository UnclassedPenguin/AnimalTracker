#!/usr/bin/python3

'''
Copyright © 2018 UnclassedPenguin
App: Animal Tracker
Author: UnclassedPenguin
Description: An app to keep track of your Animals
'''

import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
import sys
sys.path.append('./UI/')
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QMenuBar, \
    QWidget,QScrollArea, QTableWidget, QVBoxLayout,QTableWidgetItem, QAction
from PyQt5.QtGui import QScreen, QIcon, QPixmap
from datetime import datetime
import mainwindow, searchwindow, optionswindow, addgroupdialog, tablewindow, \
    savefilewindow, printwindow, genealogywindow
import pandas as pd
import sqlite3
import xlsxwriter
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
database = config['DEFAULT']['database']

class ATApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ATApp, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./Other/AnimalTrackerIcon.png'))

        date = datetime.now().strftime("%a %b %d, %Y")
        self.dialogs = []

        self.read_Config()
        self.create_Tables()
        self.dateLabel.setText(date)
        self.weightEntry.setText('0')
        self.addgroupButton.clicked.connect(self.get_Group)
        self.searchButton.clicked.connect(self.search_Button)

        self.displayallButton.clicked.connect(self.display_All)

        self.testButton.clicked.connect(self.read_Database)
        # self.testButton.clicked.connect(self.change_Dates)
        self.clearButton.clicked.connect(self.clear_Button)
        self.advsearchButton.clicked.connect(self.goto_SearchPage)
        self.optionsButton.clicked.connect(self.goto_OptionsPage)
        self.saveButton.clicked.connect(self.save_Button)
        self.quitButton.clicked.connect(self.close)

    def change_Dates(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('select date, numid from cleananimals;')
        datefetch = curs.fetchall()
        print(datefetch)
        for string in datefetch:
            print(string[0])
            value = string[1]
            date1 = string[0].split('/')
            print(date1)
            print(value)
            date2 = date1[2] + '-' + date1[1] + '-' + date1[0]
            print(date2)
            curs.execute('UPDATE cleananimals SET date = ? WHERE numid = ?', \
                         (date2, value,))
            conn.commit()
        conn.close()

    def change_Bdays(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('select bday, numid from cleananimals;')
        datefetch = curs.fetchall()
        print(datefetch)
        for string in datefetch:
            print(string[0])
            value = string[1]
            date1 = string[0].split('/')
            print(date1)
            print(value)
            date2 = '20' + date1[2] + '-' + date1[0] + '-' + date1[1]
            print(date2)
            curs.execute('UPDATE cleananimals SET bday = ? WHERE numid = ?', \
                         (date2, value,))
            conn.commit()
        conn.close()

    def read_Database(self):
        print("Heyo")
        # global database
        # conn = sqlite3.connect(database)
        # curs = conn.cursor()
        # #curs.execute('INSERT INTO config (configkey) \
        #     values("databasefile");')
        # # curs.execute('select configvalue from config \
            # where configkey = "databasefile"')
        # # self.dirtybasefile = curs.fetchall()
        # # self.tuplebasefile = self.dirtybasefile[0]
        # self.databasefile = self.tuplebasefile[0]
        # print(self.dirtybasefile)
        # print(type(self.dirtybasefile))
        # print(self.tuplebasefile)
        # print(type(self.tuplebasefile))
        # print(self.databasefile)
        # print(type(self.databasefile))
        # conn.close()
        # return self.databasefile

    def read_Config(self):
        global database
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('CREATE TABLE IF NOT EXISTS collection (species)')
        curs.execute('INSERT INTO collection (species) values("All");')
        curs.execute('SELECT * FROM collection')
        dirtylist = curs.fetchall()
        self.groups = []
        self.groups = list(sum(dirtylist, ()))
        print("Clean {}".format(self.groups))
        self.groupBox.clear()
        self.groupBox.addItems(self.groups)
        conn.close()
        return self.groups

    def msg(self, messagetype, messagetitle, infotext, messagetext):
        if messagetype == 'info':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            #msg.setBaseSize(QtCore.QSize(600, 120))
            msg.exec()
        if messagetype == 'crit':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            #msg.setBaseSize(QtCore.QSize(600, 120))
            msg.exec()
        if messagetype == "":
            msg = QtWidgets.QMessageBox()
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()

    def add_group(self, grouptoenter):
        global database
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        print("Newgroup: {}".format(grouptoenter))
        if len(grouptoenter) > 0:
            controlv = grouptoenter
            print("Updating Groups List...")
            curs.execute("INSERT INTO collection VALUES (?) ", (controlv,))
            conn.commit()
            self.msg('info', 'Info', '', 'Group Added')
        conn.close()
        self.read_Config()

    def get_Group(self):
        group = addgroupPage()
        if group.exec_():
            self.add_group(group.newgroupEntry.text())

    def goto_SearchPage(self):
        dialog = SearchPage(self)
        self.dialogs.append(dialog)
        dialog.show()

    def goto_OptionsPage(self):
        dialog = OptionsPage(self)
        self.dialogs.append(dialog)
        dialog.show()

    def goto_addgroupPage(self):
        dialog = addgroupPage(self)
        self.dialogs.append(dialog)
        dialog.show()

    def test_Button(self):
        name = self.nameEntry.text()
        notes = self.notesEntry.toPlainText()

        self.checkgender_Group()
        self.checkbodycon_Group()
        self.checkhoofcon_Group()
        self.checkis_Sold()

        print("Name: {}".format(name))
        print("Notes: {}".format(notes))

        list2 = ['hello', 'world']
        self.groupBox.clear()
        self.groupBox.addItems(list2)
        self.read_Config()

    def checkgender_Group(self):
        if self.genderButton3.isChecked():
            print("Gender is female")
            self.gendervalue = "female"
        if self.genderButton2.isChecked():
            print("Gender is male")
            self.gendervalue = "male"
        if self.genderButton1.isChecked():
            print("Gender is weather")
            self.gendervalue = "weather"
        return self.gendervalue

    def checkbodycon_Group(self):
        if self.bodyconButton5.isChecked():
            print("Body Con = 5")
            self.bodyconvalue = 5
        if self.bodyconButton4.isChecked():
            print("Body Con = 4")
            self.bodyconvalue = 4
        if self.bodyconButton3.isChecked():
            print("Body Con = 3")
            self.bodyconvalue = 3
        if self.bodyconButton2.isChecked():
            print("Body Con = 2")
            self.bodyconvalue = 2
        if self.bodyconButton1.isChecked():
            print("Body Con = 1")
            self.bodyconvalue = 1
        return self.bodyconvalue

    def checkhoofcon_Group(self):
        if self.hoofconButton3.isChecked():
            print("Hoof Con = 3")
            self.hoofconvalue = 'good'
        if self.hoofconButton2.isChecked():
            print("Hoof Con = 2")
            self.hoofconvalue = 'ok'
        if self.hoofconButton1.isChecked():
            print("Hoof Con = 1")
            self.hoofconvalue = 'bad'
        return self.hoofconvalue

    def checkis_Sold(self):
        if self.soldButton.isChecked():
            print("Animal is sold")
            self.soldvalue = 1
        else:
            print("Animal is not sold")
            self.soldvalue = 0
        return self.soldvalue

    def search_Button(self):
        global database
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        print("You searched! Maybe...")
        namefield = self.nameEntry.text()
        idfield = self.idEntry.text()
        rfidfield = self.rfidEntry.text()
        print(namefield)
        group = self.groupBox.currentText()
        if group != 'All':
            if len(namefield) > 0:
                curs.execute('''SELECT date, bday, groups, rfid, id, name,
                                mother, father, weight, notes, gender, hoofcon,
                                bodycon, sold FROM animals WHERE groups = ?
                                and name is ?''', (group, namefield,))
            elif len(idfield) > 0:
                curs.execute('''SELECT date, bday, groups, rfid, id, name,
                                mother, father, weight, notes, gender, hoofcon,
                                bodycon, sold FROM animals WHERE groups = ?
                                and id is ?''', (group, idfield,))
            elif len(rfidfield) > 0:
                curs.execute('''SELECT date, bday, groups, rfid, id, name,
                                mother, father, weight, notes, gender, hoofcon,
                                bodycon, sold FROM animals WHERE groups = ?
                                and rfid is ?''', (group, rfidfield,))
            templist = list(curs.fetchall())
            print("Templist: {}".format(templist))
            print("Length of templist: {}".format(len(templist)))
            if len(templist) > 0:
                templistlastitem = templist[-1]
                print("TempListlast item: {}".format(templistlastitem))

                self.bdayEntry.setText(templistlastitem[1])
                index = self.groupBox.findText(templistlastitem[2], \
                                               QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.groupBox.setCurrentIndex(index)

                self.rfidEntry.setText(templistlastitem[3])
                self.idEntry.setText(templistlastitem[4])
                self.nameEntry.setText(templistlastitem[5])
                self.motherEntry.setText(templistlastitem[6])
                self.fatherEntry.setText(templistlastitem[7])
                self.weightEntry.setText(str(templistlastitem[8]))
                self.notesEntry.setText(templistlastitem[9])
                if templistlastitem[10] == "female":
                    self.genderButton3.setChecked(True)
                elif templistlastitem[10] == "male":
                    self.genderButton2.setChecked(True)
                elif templistlastitem[10] == "weather":
                    self.genderButton1.setChecked(True)
                if templistlastitem[11] == 3 or templistlastitem[11] == 'good':
                    self.hoofconButton3.setChecked(True)
                elif templistlastitem[11] == 2 or templistlastitem[11] == 'ok':
                    self.hoofconButton2.setChecked(True)
                elif templistlastitem[11] == 1 or templistlastitem[11] == 'bad':
                    self.hoofconButton1.setChecked(True)
                if templistlastitem[12] == 5:
                    self.bodyconButton5.setChecked(True)
                elif templistlastitem[12] == 4:
                    self.bodyconButton4.setChecked(True)
                elif templistlastitem[12] == 3:
                    self.bodyconButton3.setChecked(True)
                elif templistlastitem[12] == 2:
                    self.bodyconButton2.setChecked(True)
                elif templistlastitem[12] == 1:
                    self.bodyconButton1.setChecked(True)
                if templistlastitem[13] == 1:
                    self.soldButton.setChecked(True)
                elif templistlastitem[13] == 0:
                    self.soldButton.setChecked(False)

            elif len(templist) == 0:
                print("Something Happened")

                self.msg('crit', 'Error', 'Search Error', \
                         'Empty or name not found')
                self.bdayEntry.setText('')
                self.rfidEntry.setText('')
                self.idEntry.setText('')
                self.nameEntry.setText('')
                self.motherEntry.setText('')
                self.fatherEntry.setText('')
                self.weightEntry.setText('')
                self.notesEntry.clear()
                self.hoofconButton3.setChecked(True)
                self.bodyconButton5.setChecked(True)
                self.genderButton3.setChecked(True)

        elif group == 'All':
            if len(namefield) > 0:
                curs.execute('''SELECT date, bday, groups, rfid, id, name,
                                mother, father, weight, notes, gender, hoofcon,
                                bodycon, sold FROM animals where name is ?''',\
                                (namefield,))
            elif len(idfield) > 0:
                curs.execute('''SELECT date, bday, groups, rfid, id, name,
                                mother, father, weight, notes, gender, hoofcon,
                                bodycon, sold FROM animals WHERE id is ?''',\
                                (idfield,))
            elif len(rfidfield) > 0:
                curs.execute('''SELECT date, bday, groups, rfid, id, name,
                                mother, father, weight, notes, gender, hoofcon,
                                bodycon, sold FROM animals WHERE rfid is ?''',\
                                (rfidfield,))
            templist = list(curs.fetchall())
            print("Templist: {}".format(templist))
            print("Length of templist: {}".format(len(templist)))
            if len(templist) > 0:
                templistlastitem = templist[-1]
                print("TempListlast item: {}".format(templistlastitem))

                self.bdayEntry.setText(templistlastitem[1])
                index = self.groupBox.findText(templistlastitem[2], \
                                               QtCore.Qt.MatchFixedString)
                if index >= 0:
                    self.groupBox.setCurrentIndex(index)

                self.rfidEntry.setText(templistlastitem[3])
                self.idEntry.setText(templistlastitem[4])
                self.nameEntry.setText(templistlastitem[5])
                self.motherEntry.setText(templistlastitem[6])
                self.fatherEntry.setText(templistlastitem[7])
                self.weightEntry.setText(str(templistlastitem[8]))
                self.notesEntry.setText(templistlastitem[9])
                if templistlastitem[10] == "female":
                    self.genderButton3.setChecked(True)
                elif templistlastitem[10] == "male":
                    self.genderButton2.setChecked(True)
                elif templistlastitem[10] == "weather":
                    self.genderButton1.setChecked(True)
                if templistlastitem[11] == 3 \
                   or templistlastitem[11] == 'good':
                    self.hoofconButton3.setChecked(True)
                elif templistlastitem[11] == 2 \
                     or templistlastitem[11] == 'ok':
                    self.hoofconButton2.setChecked(True)
                elif templistlastitem[11] == 1 \
                     or templistlastitem[11] == 'bad':
                    self.hoofconButton1.setChecked(True)
                if templistlastitem[12] == 5:
                    self.bodyconButton5.setChecked(True)
                elif templistlastitem[12] == 4:
                    self.bodyconButton4.setChecked(True)
                elif templistlastitem[12] == 3:
                    self.bodyconButton3.setChecked(True)
                elif templistlastitem[12] == 2:
                    self.bodyconButton2.setChecked(True)
                elif templistlastitem[12] == 1:
                    self.bodyconButton1.setChecked(True)
                if templistlastitem[13] == 1:
                    self.soldButton.setChecked(True)
                elif templistlastitem[13] == 0:
                    self.soldButton.setChecked(False)

            elif len(templist) == 0:
                print("Something Happened")

                self.msg('crit', 'Error', 'Search Error', \
                         'Empty or name not found')
                self.bdayEntry.setText('')
                self.rfidEntry.setText('')
                self.idEntry.setText('')
                self.nameEntry.setText('')
                self.motherEntry.setText('')
                self.fatherEntry.setText('')
                self.weightEntry.setText('')
                self.notesEntry.clear()
                self.hoofconButton3.setChecked(True)
                self.bodyconButton5.setChecked(True)
                self.genderButton3.setChecked(True)

        conn.close()

    def clear_Button(self):
        self.bdayEntry.setText('')
        self.rfidEntry.setText('')
        self.idEntry.setText('')
        self.nameEntry.setText('')
        self.motherEntry.setText('')
        self.fatherEntry.setText('')
        self.weightEntry.setText('0')
        self.notesEntry.clear()
        self.hoofconButton3.setChecked(True)
        self.bodyconButton5.setChecked(True)
        self.genderButton3.setChecked(True)
        self.soldButton.setChecked(False)

    def create_Tables(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('''CREATE TABLE IF NOT EXISTS animals
                   (numid integer PRIMARY KEY, date, bday, groups,
                    rfid, id, name, mother, father, weight, notes,
                    gender, hoofcon, bodycon, sold)''')
        curs.execute('''CREATE TABLE IF NOT EXISTS cleananimals
                   (numid integer PRIMARY KEY, date, bday, groups,
                    rfid, id, name, mother, father, weight, notes,
                    gender, hoofcon, bodycon, sold)''')
        curs.execute("CREATE UNIQUE INDEX if not exists" \
                     " numidx_cleananimals_name ON cleananimals (name);")
        conn.commit()
        conn.close()

    def display_All(self):
        conn = sqlite3.connect(database)
        curs = conn.cursor()

        templist = ['date', 'groups', 'rfid', 'id', 'name', \
                    'weight', 'mother', 'father', 'bday', \
                    'notes', 'gender', 'hoofcon', 'bodycon', 'sold']

        self.sql = "SELECT date, groups, rfid, id, name, " \
                   "weight, mother, father, bday, notes, gender," \
                   "hoofcon, bodycon, sold from cleananimals"
        x = pd.read_sql_query(self.sql, conn)
        y=x.sort_values(by=['groups', 'name'])
        self.window = DisplayPage()
        df = y
        self.window.table.setColumnCount(len(df.columns))
        self.window.table.setRowCount(len(df.index))
        self.window.table.setHorizontalHeaderLabels(templist)
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                self.window.table.setItem(i,j,QTableWidgetItem\
                                          (str(df.iloc[i, j])))
        self.window.table.setWordWrap(True)
        self.window.table.resizeRowsToContents()
        self.window.table.resizeColumnsToContents()
        self.window.show()
        conn.close()

    def save_Button(self):
        global database
        global counter
        if len(self.nameEntry.text()) == 0 and len(self.rfidEntry.text()) == 0:
            print("Doesn't work!")
            self.msg('crit', 'Error', 'Save Error', 'Please enter name and id')
        else:
            notes = self.notesEntry.toPlainText()
            date2 = datetime.now().strftime('%Y-%m-%d')
            conn = sqlite3.connect(database)
            curs = conn.cursor()

            print("Group: {}".format(str(self.groupBox.currentText())))
            print("RFID: {}".format(self.rfidEntry.text()))
            print("ID: {}".format(self.idEntry.text()))
            print("Name: {}".format(self.nameEntry.text()))
            print("Date: {}".format(date2))
            print("Gender: {}".format(self.checkgender_Group()))
            print("Weight: {}".format(self.weightEntry.text()))
            print("Mother: {}".format(self.motherEntry.text()))
            print("Father: {}".format(self.fatherEntry.text()))
            print("Hoof Cond: {}".format(self.checkhoofcon_Group()))
            print("Body Cond: {}".format(self.checkbodycon_Group()))
            print("Notes: {}".format(notes))

            # Was used to create database first time

            name = self.nameEntry.text()
            data_to_inject = (date2, self.bdayEntry.text(), \
                              str(self.groupBox.currentText()), \
                              self.rfidEntry.text(), self.idEntry.text(), \
                              self.nameEntry.text(), self.motherEntry.text(), \
                              self.fatherEntry.text(), \
                              int(self.weightEntry.text()), \
                              self.notesEntry.toPlainText(), \
                              self.checkgender_Group(), \
                              self.checkhoofcon_Group(), \
                              self.checkbodycon_Group(), self.checkis_Sold())
            curs.execute('''INSERT INTO animals(date, bday, groups, rfid, id,
                            name, mother, father, weight, notes, gender,
                            hoofcon, bodycon, sold)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', \
                            data_to_inject)

            name = self.nameEntry.text()
            data_to_inject = (date2, self.bdayEntry.text(), \
                              str(self.groupBox.currentText()), \
                              self.rfidEntry.text(), self.idEntry.text(), \
                              self.nameEntry.text(), self.motherEntry.text(), \
                              self.fatherEntry.text(), \
                              int(self.weightEntry.text()), \
                              self.notesEntry.toPlainText(), \
                              self.checkgender_Group(),
                              self.checkhoofcon_Group(), \
                              self.checkbodycon_Group(), self.checkis_Sold())
            curs.execute('''REPLACE INTO cleananimals (date, bday, groups,
                            rfid, id, name, mother, father, weight, notes,
                            gender, hoofcon, bodycon, sold)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', \
                            data_to_inject)

            conn.commit()
            conn.close()

        return True

class SearchPage(QtWidgets.QMainWindow, searchwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(SearchPage, self).__init__()
        self.setupUi(self)
        self.dialogs = []
        self.orderbygroups = ['None',
                 'Bday Asc.', 'Bday Des.',
                 'BodyCond Asc.', 'BodyCond Des.',
                 'Date Asc.', 'Date Des.',
                 'Father Asc.', 'Father Des.',
                 'Gender Asc.', 'Gender Des.',
                 'Group Asc.', 'Group Des.',
                 'HoofCond Asc.', 'HoofCond Des.',
                 'ID Asc.', 'ID Des.',
                 'Mother Asc.', 'Mother Des.',
                 'Name Asc.', 'Name Des.',
                 'Notes Asc.', 'Notes Des.',
                 'Sold Asc.', 'Sold Des.',
                 'Weight Asc.', 'Weight Des.',
                ]

        self.read_Config()
        list2 = ['Clean Data', 'Historical Data']
        self.tableBox.clear()
        self.tableBox.addItems(list2)
        self.toggleallButton.clicked.connect(self.toggle_All)
        self.search2Button.clicked.connect(self.search22_Button)
        self.save2Button.clicked.connect(self.getfile_Path)
        self.genealogyButton.clicked.connect(self.goto_Genealogypage)
        self.testButton.clicked.connect(self.test)
        self.quit2Button.clicked.connect(self.close)

    def test(self):
        self.msg('', 'Info', 'You pushed the test Button', '')

    def read_Config(self):
        global database
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('CREATE TABLE IF NOT EXISTS collection (species)')
        curs.execute('INSERT INTO collection (species) values("All");')
        curs.execute('SELECT * FROM collection')
        dirtylist = curs.fetchall()
        self.groups = []
        self.groups = list(sum(dirtylist, ()))
        self.group2Box.clear()
        self.group2Box.addItems(self.groups)
        self.orderbyBox.clear()
        self.orderbyBox.addItems(self.orderbygroups)
        self.orderby2Box.clear()
        self.orderby2Box.addItems(self.orderbygroups)
        conn.close()
        return self.groups

    def msg(self, messagetype, messagetitle, infotext, messagetext):
        if messagetype == 'info':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()
        if messagetype == 'crit':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()
        if messagetype == "":
            msg = QtWidgets.QMessageBox()
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()

    def toggle_All(self):
        x = self.get_Cbvalues()
        print(x)
        print("0: {}".format(x.count(0)))
        print("1: {}".format(x.count(1)))
        self.temp2list = [self.gendercbButton, self.datecbButton,
             self.groupcbButton, self.namecbButton,
             self.bdaycbButton, self.rfidcbButton,
             self.idcbButton, self.mothercbButton,
             self.fathercbButton, self.weightcbButton,
             self.hoofconcbButton, self.bodyconcbButton,
             self.notescbButton, self.soldcbButton
             ]
        if x.count(1) <= 14 and x.count(1) > 1:
            for s in self.temp2list:
                s.setChecked(False)
        if x.count(0) <= 14 and x.count(0) > 1:
            for s in self.temp2list:
                s.setChecked(True)

    def getfile_Path(self):
        filepath = savefilePage()
        if filepath.exec_():
            self.actually_Save(filepath.savepathEntry.text(), \
                               filepath.savenameEntry.text(), \
                               filepath.filetypeBox.currentText())

    def actually_Save(self, filepath, savename, filetype):
        if len(savename) > 0 and filetype == '.xlsx (Excel) File':
            try:
                if filepath[-1:] == '/':
                    completepath = filepath + savename + '.xlsx'
                elif filepath[-1:] != '/':
                    completepath = filepath + '/' + savename + '.xlsx'
                df = self.search2_Button()
                writer = pd.ExcelWriter(completepath, engine='xlsxwriter')
                # Convert the dataframe to an XlsxWriter Excel object.
                df.to_excel(writer, sheet_name='Sheet1')
                # Close the Pandas Excel writer and output the Excel file.
                writer.save()
                self.msg('info', 'Info', \
                         "File saved to: {}".format(completepath), "" )
            except:
                print(filepath[-6])
                self.msg('info', 'Info', \
                         'Invalid Option', "Path Doesn't Exist")
        elif len(savename) > 0 and filetype == '.txt (Text) File':
            if filepath[-1:] == '/':
                completepath = filepath + savename + '.txt'
            elif filepath[-1:] != '/':
                completepath = filepath + '/' + savename + '.txt'
            try:
                df = self.search2_Button()
                savefile = open(completepath, 'a')
                savefile.write("\n")
                savefile.write("---------------------------------------------")
                savefile.write('\n')
                savefile.write(df.to_string())
                savefile.write('\n')
                savefile.write("---------------------------------------------")
                savefile.write('\n')
                savefile.close()
                self.msg('info', "Info", \
                         "File Saved to: {}".format(completepath), "")
            except:
                self.msg('info', 'Info', \
                         'Invalid Option', "Path Doesn't Exist")
        elif len(savename) == 0:
                self.msg('info', 'Info', \
                         'Invalid Option', "Please Enter a file name")

    def search2_Button(self):
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 1000)
        pd.set_option('display.expand_frame_repr', False)
        pd.set_option('display.latex.multirow', True)
        pd.set_option('max_colwidth', 3000)

        global database
        group = str(self.group2Box.currentText())
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        #templist=[]
        #self.templist=[]

        self.orderbydict = {'None': 'None',\
                         'Bday Asc.': 'bday', 'Bday Des.': 'bday',\
                         'BodyCond Asc.':'bodycon', 'BodyCond Des.':'bodycon',\
                         'Date Asc.': 'date', 'Date Des.': 'date',\
                         'Father Asc.': 'father', 'Father Des.': 'father',\
                         'Gender Asc.': 'gender', 'Gender Des.': 'gender',\
                         'Group Asc.': 'groups', 'Group Des.': 'groups',\
                         'HoofCond Asc.':'hoofcon', 'HoofCond Des.':'hoofcon',\
                         'ID Asc.': 'id', 'ID Des.': 'id',\
                         'Mother Asc.': 'mother', 'Mother Des.': 'mother',\
                         'Name Asc.': 'name', 'Name Des.': 'name',\
                         'Notes Asc.': 'notes', 'Notes Des.': 'notes',\
                         'Sold Asc.': 'sold', 'Sold Des.': 'sold',\
                         'Weight Asc.': 'weight', 'Weight Des.': 'weight'}

        self.searchlist = []
        self.searchlist2 = []
        self.get_Cbvalues()
        print("SEACHLIST: {}".format(self.searchlist2))
        print("newlist: {}".format(self.newlist))

        self.templist_Append(self.datecbButton, 'date')
        self.templist_Append(self.groupcbButton, 'groups')
        self.templist_Append(self.rfidcbButton, 'rfid')
        self.templist_Append(self.idcbButton, 'id')
        self.templist_Append(self.namecbButton, 'name')
        self.templist_Append(self.weightcbButton, 'weight')
        self.templist_Append(self.mothercbButton, 'mother')
        self.templist_Append(self.fathercbButton, 'father')
        self.templist_Append(self.bdaycbButton, 'bday')
        self.templist_Append(self.notescbButton, 'notes')
        self.templist_Append(self.gendercbButton, 'gender')
        self.templist_Append(self.hoofconcbButton, 'hoofcon')
        self.templist_Append(self.bodyconcbButton, 'bodycon')
        self.templist_Append(self.soldcbButton, 'sold')

        self.tempstr = ', '.join(self.searchlist)
        self.searchlist2 = self.searchlist[:]

        print('TEMPSTR: {}'.format(self.tempstr))
        print("TableBox: {}".format(self.tableBox.currentText()))

        if self.distinctcbButton.isChecked() \
           and len(self.name2Entry.text()) == 0 \
           and len(self.id2Entry.text()) == 0 \
           and len(self.rfid2Entry.text()) == 0 \
           and self.newlist != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            if self.tableBox.currentText() == 'Historical Data':
                if group != 'All':
                    self.sql = "SELECT DISTINCT " + \
                               self.tempstr + " from animals where groups = ? "
                    x = pd.read_sql_query(self.sql, conn, params=[group])
                elif group == 'All':
                    self.sql = "SELECT DISTINCT " + \
                               self.tempstr + " from animals"
                    x = pd.read_sql_query(self.sql, conn)
            if self.tableBox.currentText() == 'Clean Data':
                if group != 'All':
                    self.sql = "SELECT DISTINCT " + \
                               self.tempstr + \
                               " from cleananimals where groups = ? "
                    x = pd.read_sql_query(self.sql, conn, params=[group])
                elif group == 'All':
                    self.sql = "SELECT DISTINCT " + \
                               self.tempstr + " from cleananimals"
                    x = pd.read_sql_query(self.sql, conn)

        elif self.distinctcbButton.isChecked() == False \
             and len(self.name2Entry.text()) > 0 \
             and self.newlist != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            if self.tableBox.currentText() == 'Historical Data':
                self.sql = "SELECT " + self.tempstr + \
                    " from animals where name IS " + "'" + \
                    self.name2Entry.text() + "'"
                print(self.sql)
                x = pd.read_sql_query(self.sql, conn)
            if self.tableBox.currentText() == 'Clean Data':
                self.sql = "SELECT " + self.tempstr + \
                    " from cleananimals where name IS " + "'" + \
                    self.name2Entry.text() + "'"
                print(self.sql)
                x = pd.read_sql_query(self.sql, conn)

        elif self.distinctcbButton.isChecked() == False \
             and len(self.rfid2Entry.text()) > 0 \
             and self.newlist != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            if self.tableBox.currentText() == 'Historical Data':
                self.sql = "SELECT " + self.tempstr + \
                    " from animals where rfid IS " + "'" + \
                    self.rfid2Entry.text() + "'"
                print(self.sql)
                x = pd.read_sql_query(self.sql, conn)
            if self.tableBox.currentText() == 'Clean Data':
                self.sql = "SELECT " + self.tempstr + \
                    " from cleananimals where rfid IS " + "'" + \
                    self.rfid2Entry.text() + "'"
                print(self.sql)
                x = pd.read_sql_query(self.sql, conn)

        elif self.distinctcbButton.isChecked() == False \
             and len(self.id2Entry.text()) > 0 \
             and self.newlist != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            if self.tableBox.currentText() == 'Historical Data':
                self.sql = "SELECT " + self.tempstr + \
                    " from animals where id IS " + "'" + \
                    self.id2Entry.text() + "'"
                print(self.sql)
                x = pd.read_sql_query(self.sql, conn)
            if self.tableBox.currentText() == 'Clean Data':
                self.sql = "SELECT " + self.tempstr + \
                    " from cleananimals where id IS " + "'" + \
                    self.id2Entry.text() + "'"
                print(self.sql)
                x = pd.read_sql_query(self.sql, conn)

        elif self.distinctcbButton.isChecked() \
             and len(self.name2Entry.text()) > 0:
            print("Invalid Option. Cannot search Name with Distinct.")
            self.sql=""
            x = ""
            self.msg('info', 'Info', 'Invalid Option', \
                     "Cannot search Name with Distinct")
            self.p = ""

        elif self.distinctcbButton.isChecked() \
             and len(self.rfid2Entry.text()) > 0:
            print("Invalid Option. Cannot search RFID with Distinct.")
            self.sql=""
            x = ""
            self.msg('info', 'Info', 'Invalid Option', \
                     "Cannot search RFID with Distinct")
            self.p = ""

        elif self.distinctcbButton.isChecked() \
             and len(self.id2Entry.text()) > 0:
            print("Invalid Option. Cannot search ID with Distinct.")
            self.sql=""
            x = ""
            self.msg('info', 'Info', 'Invalid Option', \
                     "Cannot search ID with Distinct")
            self.p = ""

        elif len(self.name2Entry.text()) > 0 \
             or len(self.rfid2Entry.text()) > 0 \
             or len(self.id2Entry.text()) > 0 \
             and self.newlist == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            print("NEWLIST: {}".format(self.newlist))
            self.msg('info', 'Info', \
                     "Please select atleast one checkbox", '' )
            self.sql=''
            x = ""
            self.p = ""

        elif str(self.orderbyBox.currentText()) != 'None' \
             and self.newlist == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            self.msg('info', 'Info', \
                     '''Please select at least the
                     checkbox you have Ordered by''', '')
            self.sql=''
            x = ''
            self.p = ""

        elif self.distinctcbButton.isChecked() \
             and self.newlist == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Invalid Option. Please select a checkbox")
            msg.setWindowTitle("Info")
            msg.exec()
            self.msg('info', 'Info', 'Invalid Option', \
                     "Please select at least one checkbox")
            x = ''
            self.p = ""
        else:
            try:
                if self.tableBox.currentText() == 'Historical Data':
                    print("Group: {}".format(group))
                    print("Prestring: {}".format(self.tempstr))
                    print(group == 'All')
                    if group != 'All':
                        self.sql = "SELECT " + self.tempstr + \
                                   " from animals where groups = ?"
                        x = pd.read_sql_query(self.sql, conn, params=[group])
                    elif group == 'All':
                        print("From all: {}".format(self.tempstr))
                        self.sql = "SELECT " + self.tempstr + " from animals"
                        x = pd.read_sql_query(self.sql, conn)
                elif self.tableBox.currentText() == 'Clean Data':
                    print("Group: {}".format(group))
                    print("Prestring: {}".format(self.tempstr))
                    print(group == 'All')
                    if group != 'All':
                        self.sql = "SELECT " + self.tempstr + \
                                   " from cleananimals where groups = ?"
                        x = pd.read_sql_query(self.sql, conn, params=[group])
                    elif group == 'All':
                        print("From all: {}".format(self.tempstr))
                        self.sql = "SELECT " + self.tempstr + \
                                   " from cleananimals"
                        x = pd.read_sql_query(self.sql, conn)
            except:
                if self.newlist == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
                    x = "Nothing Selected!"
                    self.p='None'
                    self.msg('info', 'Info', 'Invalid Option', \
                             "Nothing Selected")

        try:
            if self.newlist != [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
                self.orderbyval = str(self.orderbyBox.currentText())
                self.orderbyval2 = str(self.orderby2Box.currentText())
                x.index = x.index + 1
                if self.orderbyval == "None":
                    self.q=x
                elif self.orderbyval != 'None':
                    for key, val in self.orderbydict.items():
                        if self.orderbyval == key \
                           and self.orderbyval[-4:] == 'Asc.':
                            self.q=x.sort_values(by=[val])
                        elif self.orderbyval == key \
                             and self.orderbyval[-4:] == 'Des.':
                            self.q=x.sort_values(by =[val], ascending=False)



                print("Self.q: \n{}".format(self.q))

        except:
            if self.newlist == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]:
                self.msg('info', 'Info', 'Invalid Option', \
                         "Nothing selected")
                self.p="none"

        if self.orderbyval2 == "None":
            print("WE DID THIS ONE")
            self.p = self.q
        elif self.orderbyval2 != 'None':
            for key, val in self.orderbydict.items():
                if self.orderbyval2 == key and self.orderbyval2[-4:] == 'Asc.':
                    print(val)
                    print("WE DID THIS ONE NUMBER TWO")
                    self.p=self.q.sort_values(by=[self.orderbydict\
                                                  [self.orderbyval], val])
                elif self.orderbyval2 == key \
                     and self.orderbyval2[-4:] == 'Des.':
                    print("WE DID THIS ONE NUMBER THREE")
                    self.p=self.q.sort_values(by =[self.orderbydict\
                                                   [self.orderbyval], val], \
                                              ascending=False)
        print("Self.p: \n{}".format(self.p))

        self.searchlist.clear()
        curs.close()
        conn.close()
        return self.p

    def search22_Button(self):
        self.y = self.search2_Button()
        if isinstance(self.y, pd.core.frame.DataFrame):
            self.window = DisplayPage()
            df = self.y
            self.window.table.setColumnCount(len(df.columns))
            self.window.table.setRowCount(len(df.index))
            self.window.table.setHorizontalHeaderLabels(self.searchlist2)
            for i in range(len(df.index)):
                for j in range(len(df.columns)):
                    self.window.table.setItem(i,j,QTableWidgetItem(str(df.iloc[i, j])))
            self.window.table.setWordWrap(True)
            self.window.table.resizeRowsToContents()
            self.window.table.resizeColumnsToContents()
            self.window.show()
        elif isinstance(self.y, pd.core.frame.DataFrame) == False:
            pass

    def get_Cbvalues(self):
        print("Getting CB Values")
        self.templist = {'self.gendercbButton': self.gendercbButton,
                         'self.datecbButton': self.datecbButton,
                         'self.groupcbButton': self.groupcbButton,
                         'self.namecbButton': self.namecbButton,
                         'self.bdaycbButton': self.bdaycbButton,
                         'self.rfidcbButton': self.rfidcbButton,
                         'self.idcbButton': self.idcbButton,
                         'self.mothercbButton': self.mothercbButton,
                         'self.fathercbButton': self.fathercbButton,
                         'self.weightcbButton': self.weightcbButton,
                         'self.hoofconcbButton': self.hoofconcbButton,
                         'self.bodyconcbButton': self.bodyconcbButton,
                         'self.notescbButton': self.notescbButton,
                         'self.soldcbButton': self.soldcbButton
                         }
        self.newdict = {}
        self.newlist = []
        self.newlist.clear()

        for key, value in self.templist.items():
            if value.isChecked():
                self.newdict[key] = 1
                self.newlist.append(1)
            elif value.isChecked() == False:
                self.newdict[key] = 0
                self.newlist.append(0)

        print("New list: {}".format(self.newlist))
        print("Got CB Values")
        return self.newlist

    def templist_Append(self, cbvar, dbvar):
        global database
        if cbvar.isChecked():
            group = str(self.group2Box.currentText())
            conn = sqlite3.connect(database)
            curs = conn.cursor()
            o = dbvar
            if group != 'All':
                curs.execute('SELECT ? FROM animals WHERE groups = ?', \
                             (o, group,))
            elif group == 'All':
                curs.execute('SELECT ? FROM animals', (o,))
            tempstr = curs.fetchall()
            if len(tempstr) > 0:
                self.searchlist.append(o)
            print('SEARCHLIST: {}'.format(self.searchlist))
            curs.close()
            conn.close()

    def goto_Genealogypage(self):
        dialog = GenealogyPage(self)
        self.dialogs.append(dialog)
        dialog.show()

class GenealogyPage(QtWidgets.QMainWindow, genealogywindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(GenealogyPage, self).__init__()
        self.setupUi(self)

        self.searchButton.clicked.connect(self.print_Display)
        self.closeButton.clicked.connect(self.close)

    def msg(self, messagetype, messagetitle, infotext, messagetext):
        if messagetype == 'info':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()
        if messagetype == 'crit':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()
        if messagetype == "":
            msg = QtWidgets.QMessageBox()
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()

    def test(self):
        family = self.create_Family()
        print(family)
        for thing in family['siblings'].values():
            print(thing[2])

    def print_Display(self):
        self.window = PrintPage()
        family = self.create_Family()
        if family == False:
            pass
        elif family != False:
            self.window.textBrowser.append('# Name: {}'.format(family['name'][0]))
            self.window.textBrowser.append('----------------------------')
            self.window.textBrowser.append('''{} (M, bday={})'''.format(family['parents']['father'][0], \
                                                                        family['parents']['father'][1]))
            self.window.textBrowser.append('''{} (F, bday={})'''.format(family['parents']['mother'][0], \
                                                                        family['parents']['mother'][1]))
            if family['name'][2] == 'female':
                self.window.textBrowser.append('''\t{} (F, bday={})'''.format(family['name'][0], family['name'][1]))
            elif family['name'][2] == 'male' or family['name'][2] == 'weather':
                self.window.textBrowser.append('''\t{} (M, bday={})'''.format(family['name'][0], family['name'][1]))
            if self.nohalfcbButton.isChecked():
                print('SIBLINGS2: {}'.format(family['siblings']))
                for sibling in family['siblings'].values():
                    if sibling[2] == 'female':
                        gender = 'F'
                    elif sibling[2] == 'male' \
                        or sibling[2] == 'weather':
                        gender = 'M'
                    self.window.textBrowser.append('''\t{} ({}, bday={})'''.format(sibling[0],gender,sibling[1]))
                self.window.textBrowser.append('')
            if self.halffathercbButton.isChecked():
                motherlist = []
                for sibling in family['siblings'].values():
                    motherlist.append(sibling[3])
                myset = set(motherlist)
                newlist = list(myset)
                if family['parents']['mother'][0] in newlist:
                    newlist.insert(0, newlist.pop(newlist.index(family['parents']['mother'][0])))
                    for sibling in family['siblings'].values():
                        if sibling[3] == family['parents']['mother'][0]:
                            if sibling[2] == 'female':
                                self.window.textBrowser.append('''\t{} (F, bday={})'''.format(sibling[0], sibling[1]))
                            elif sibling[2] == 'male' or sibling[2] == 'weather':
                                self.window.textBrowser.append('''\t{} (M, bday={})'''.format(sibling[0], sibling[1]))
                    self.window.textBrowser.append('')
                for mother in newlist:
                    if mother != family['parents']['mother'][0]:
                        self.window.textBrowser.append('''{} (M, bday={})'''.format(family['parents']['father'][0], \
                                                                                    family['parents']['father'][1]))
                        self.window.textBrowser.append('''{} (F, bday={})'''.format(mother, self.get_Bday(mother)))
                        for sibling in family['siblings'].values():
                            if sibling[3] == mother:
                                if sibling[2] == 'female':
                                    self.window.textBrowser.append('''\t{} (F, bday={})'''.format(sibling[0], sibling[1]))
                                elif sibling[2] == 'male' or sibling[2] == 'weather':
                                    self.window.textBrowser.append('''\t{} (M, bday={})'''.format(sibling[0], sibling[1]))
                        self.window.textBrowser.append('')
                self.window.textBrowser.append('')
            elif self.halfmothercbButton.isChecked():
                fatherlist = []
                for sibling in family['siblings'].values():
                    fatherlist.append(sibling[3])
                myset = set(fatherlist)
                newlist = list(myset)
                if family['parents']['father'][0] in newlist:
                    newlist.insert(0, newlist.pop(newlist.index(family['parents']['father'][0])))
                    for sibling in family['siblings'].values():
                        if sibling[3] == family['parents']['father'][0]:
                            if sibling[2] == 'female':
                                self.window.textBrowser.append('''\t{} (F, bday={})'''.format(sibling[0], sibling[1]))
                            elif sibling[2] == 'male' or sibling[2] == 'weather':
                                self.window.textBrowser.append('''\t{} (M, bday={})'''.format(sibling[0], sibling[1]))
                    self.window.textBrowser.append('')
                for father in newlist:
                    if father != family['parents']['father'][0]:
                        self.window.textBrowser.append('''{} (M, bday={})'''.format(father, self.get_Bday(father)))
                        self.window.textBrowser.append('''{} (F, bday={})'''.format(family['parents']['mother'][0], \
                                                                                    family['parents']['mother'][1]))
                        for sibling in family['siblings'].values():
                            if sibling[3] == father:
                                if sibling[2] == 'female':
                                    self.window.textBrowser.append('''\t{} (F, bday={})'''.format(sibling[0], sibling[1]))
                                elif sibling[2] == 'male' or sibling[2] == 'weather':
                                    self.window.textBrowser.append('''\t{} (M, bday={})'''.format(sibling[0], sibling[1]))
                        self.window.textBrowser.append('')
                self.window.textBrowser.append('')
            for partner in family['partners'].values():
                if family['name'][2] == 'female':
                    self.window.textBrowser.append('''\t{} (M, bday={})'''.format(partner, self.get_Bday(partner)))
                    self.window.textBrowser.append('''\t{} (F, bday={})'''.format(family['name'][0], family['name'][1]))
                elif family['name'][2] == 'male' or family['name'][2] == 'weather':
                    self.window.textBrowser.append('''\t{} (M, bday={})'''.format(family['name'][0], family['name'][1]))
                    self.window.textBrowser.append('''\t{} (F, bday={})'''.format(partner, self.get_Bday(partner)))
                for child in family['children']['{}'.format(partner)]:
                    if child[2] == 'female':
                        self.window.textBrowser.append('''\t\t{} (F, bday={})'''.format(child[0], child[1]))
                    elif child[2] == 'male' or child[2] == 'weather':
                        self.window.textBrowser.append('''\t\t{} (M, bday={})'''.format(child[0], child[1]))
                self.window.textBrowser.append('')
            self.window.show()

    def create_Familytree(self):
        family = self.create_Family()

    def create_Family(self):
        name = self.nameEdit.text()
        if len(name) == 0:
            self.msg('', 'Info', 'Please enter a name', '')
            return False
        elif self.check_Nameexists(name) == False:
            self.msg('', 'Info', 'Name not found', '')
            return False
        elif self.check_Nameexists(name) == True:
            name2 = self.get_Info(name)
            parents = self.get_Parents(name)
            partnerdict = self.get_Partnerdict(name)
            children = self.get_Children(name)
            siblings = self.get_Siblings(name)

            familydict = {'name':name2,
                        'parents':parents,
                        'partners':partnerdict,
                        'children':children,
                        'siblings':siblings}

            return familydict

    def get_Info(self, name):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('''select name, bday, gender from cleananimals where name = ?''', (name,))
        result = curs.fetchall()
        conn.close()
        return result[0]

    def check_Nameexists(self, name):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('''select name from cleananimals where name = ?''', (name,))
        result = curs.fetchone()
        if result:
            conn.close()
            return True
        else:
            conn.close()
            return False

    def get_Bday(self, name):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        try:
            curs.execute('''select bday from cleananimals where name = ?''', (name,))
            bdayfetch = curs.fetchall()
            bday = bdayfetch[0][0]
            conn.close()
            return gender
        except:
            conn.close()
            bday = '2000-00-00'
            return bday

    def get_Gender(self, name):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('''select gender from cleananimals where name = ?''', (name,))
        genderfetch = curs.fetchall()
        gender = genderfetch[0][0]
        conn.close()
        return gender

    def get_Parents(self, name):
        parentsdict = {}
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('''select mother, father from cleananimals where name = ?''', (name,))
        parentsdirty = curs.fetchall()
        mother = parentsdirty[0][0]
        father = parentsdirty[0][1]
        try:
            curs.execute('select bday from cleananimals where name = ?', \
                         (mother,))
            motherbdayfetch = curs.fetchall()
            motherbday = motherbdayfetch[0][0]
        except:
            motherbday = "2000-00-00"
        try:
            curs.execute('select bday from cleananimals where name = ?', \
                         (father,))
            fatherbdayfetch = curs.fetchall()
            fatherbday = fatherbdayfetch[0][0]
        except:
            fatherbday = "2000-00-00"

        parentsdict = {'mother':[mother, motherbday],
                       'father':[father, fatherbday]}
        conn.close()
        return parentsdict

    def get_Partnerdict(self, name):
        partnerdict = {}
        counter = 1
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        gender = self.get_Gender(name)
        if gender == 'female':
            curs.execute('''select father from cleananimals where mother = ?''', (name,))
        elif gender == 'male':
            curs.execute('''select mother from cleananimals where father = ?''', (name,))
        elif gender == 'weather':
            conn.close()
            return partnerdict
        partnersfetch = curs.fetchall()
        partnersset = set(partnersfetch)
        partnerslist = list(partnersset)
        for line in partnerslist:
            partnerdict['{}'.format(counter)] = line[0]
            counter = counter + 1
        conn.close()
        return partnerdict

    def get_Children(self, name):
        childrendict = {}
        conn = sqlite3.connect(database)
        curs = conn.cursor()

        partnerdict = self.get_Partnerdict(name)
        gender = self.get_Gender(name)
        if len(partnerdict) == 0:
            conn.close()
            return childrendict
        if gender == 'female':
            for partner in partnerdict.values():
                curs.execute('''select name, bday, gender from cleananimals where mother = ? and father = ?''',\
                                (name, partner,))
                childrenfetch = curs.fetchall()
                childrendict['{}'.format(partner)] = childrenfetch
        elif gender == 'male':
            for partner in partnerdict.values():
                curs.execute('''select name, bday, gender from cleananimals where father = ? and mother = ?''',\
                                (name, partner,))
                childrenfetch = curs.fetchall()
                childrendict['{}'.format(partner)] = childrenfetch
        elif gender == 'weather':
            conn.close()
            return childrendict
        conn.close()
        return childrendict

    def get_Siblings(self, name):
        siblingsdict = {}
        counter = 0
        conn = sqlite3.connect(database)
        curs = conn.cursor()

        parents = self.get_Parents(name)
        if self.nohalfcbButton.isChecked():
            if parents['mother'][0] != 'N/A':
                curs.execute('''select name, bday, gender from cleananimals
                                where mother = ? and father = ? and name != ?''', (parents['mother'][0], parents['father'][0], name,))
                siblingsfetch = curs.fetchall()
                for line in siblingsfetch:
                    siblingsdict["{}".format(counter)] = line
                    counter = counter + 1
            elif parents['mother'][0] == 'N/A':
                conn.close
                return siblingsdict
        elif self.halffathercbButton.isChecked():
            if parents['mother'][0] != 'N/A':
                curs.execute('''select name, bday, gender, mother from cleananimals
                                where father = ? and name != ?''', (parents['father'][0], name,))
                siblingsfetch = curs.fetchall()
                for line in siblingsfetch:
                    siblingsdict["{}".format(counter)] = line
                    counter = counter + 1
            elif parents['mother'][0] == 'N/A':
                conn.close
                return siblingsdict
        elif self.halfmothercbButton.isChecked():
            if parents['mother'][0] != 'N/A':
                curs.execute('''select name, bday, gender, father from cleananimals
                                where mother = ? and name != ?''', (parents['mother'][0], name,))
                siblingsfetch = curs.fetchall()
                for line in siblingsfetch:
                    siblingsdict["{}".format(counter)] = line
                    counter = counter + 1
            elif parents['mother'][0] == 'N/A':
                conn.close
                return siblingsdict

        conn.close()
        return siblingsdict

class OptionsPage(QtWidgets.QMainWindow, optionswindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(OptionsPage, self).__init__()
        self.setupUi(self)

        self.defaultdirEntry.setText(str(self.get_defaultdir()))
        self.databaseEdit.setText(str(self.get_defaultdb()))

        self.save3Button.clicked.connect(self.save_Options)
        self.close3Button.clicked.connect(self.close)

    def msg(self, messagetype, messagetitle, infotext, messagetext):
        if messagetype == 'info':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            #msg.setBaseSize(QtCore.QSize(600, 120))
            msg.exec()
        if messagetype == 'crit':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            #msg.setBaseSize(QtCore.QSize(600, 120))
            msg.exec()
        if messagetype == "":
            msg = QtWidgets.QMessageBox()
            msg.setText(infotext)
            msg.setInformativeText(messagetext)
            msg.setWindowTitle(messagetitle)
            msg.exec()

    def get_defaultdir(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['DEFAULT']['savedir']

    def get_defaultdb(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['DEFAULT']['database']

    def save_Options(self):
        config = configparser.ConfigParser()
        dirpath = self.defaultdirEntry.text()
        databaseEditv = self.databaseEdit.text()
        print(dirpath)
        print(databaseEditv)
        #config['Default']['database'] = databaseEditv
        #config['Default']['savedir'] = dirpath
        config.set('DEFAULT', 'database', databaseEditv)
        config.set('DEFAULT', 'savedir', dirpath)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        self.msg('info', 'Info', \
                 '''Saved. If you changed database requires
                 a restart to take affect.''', '')

class addgroupPage(QtWidgets.QDialog, addgroupdialog.Ui_Dialog):

    def __init__(self, parent=None):
        super(addgroupPage, self).__init__()
        self.setupUi(self)

class savefilePage(QtWidgets.QDialog, savefilewindow.Ui_Dialog):

    def __init__(self, parent=None):
        super(savefilePage, self).__init__()
        self.setupUi(self)

        self.filetypelist = ['.xlsx (Excel) File', '.txt (Text) File']

        self.filetypeBox.addItems(self.filetypelist)

        self.filetypeBox.currentTextChanged.connect(self.on_combo_Change)

        self.path = os.path.join(os.environ.get("HOME"), "Documents", \
                                 "AnimalTracker", "")
        self.savepathEntry.setText(str(self.get_defaultdir()))

    def on_combo_Change(self, value):
        filetype = value[:5]
        self.label_5.setText(filetype)

    def get_defaultdir(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config['DEFAULT']['savedir']

class PrintPage(QtWidgets.QMainWindow, printwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(PrintPage, self).__init__()
        self.widget = QWidget()
        self.setupUi(self)
        self.closeButton.clicked.connect(self.close)

class DisplayPage(QtWidgets.QMainWindow, tablewindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(DisplayPage, self).__init__()
        self.widget = QWidget()
        self.setupUi(self)

        self.actionClose_2.triggered.connect(self.close)
        self.actionSave_As.triggered.connect(self.saveas_Button)

    def saveas_Button(self):
        widget = self.table
        pixmap = QtGui.QPixmap(widget.size())
        widget.render(pixmap)
        pixmap.save('save.png', 'PNG', 100)
        #pix=widget.grab()
        #widget.render(pix)
        #pix.save("save.png")

def main():
    #app = QApplication(sys.argv)
    #main = ATApp()
    #main.show()
    #sys.exit(app.exec_())

    app = QApplication(sys.argv)
    app.setStyleSheet(open("./UI/style.qss", "r").read())
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(91, 91, 91))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(40, 40, 40))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(200, 43, 54))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(120, 120, 120))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Highlight, \
                     QtGui.QColor(51, 102, 153).lighter())
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.white)
    app.setPalette(palette)
    MainWindow = ATApp()
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
