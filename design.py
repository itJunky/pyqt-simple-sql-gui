# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, dbModel):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 349)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sqlConnectionEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sqlConnectionEdit.setObjectName("sqlConnectionEdit")
        self.verticalLayout.addWidget(self.sqlConnectionEdit)
        self.sqlRequestEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sqlRequestEdit.setObjectName("sqlRequestEdit")
        self.verticalLayout.addWidget(self.sqlRequestEdit)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(dbModel)
        self.verticalLayout.addWidget(self.tableView)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DBAdmin"))
        self.sqlConnectionEdit.setText(_translate("MainWindow", ":memory:"))
        self.sqlRequestEdit.setText(_translate("MainWindow", "select * from user"))
        self.pushButton.setText(_translate("MainWindow", "Show"))

