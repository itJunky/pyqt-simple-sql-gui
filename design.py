# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
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
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.allTableButton = QtWidgets.QPushButton(self.centralwidget)
        self.allTableButton.setObjectName("allTableButton")
        self.horizontalLayout.addWidget(self.allTableButton)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DBAdmin"))
        if sys.argv[1:]:
            print(sys.argv[1])
            self.sqlConnectionEdit.setText(_translate("MainWindow", sys.argv[1]))
        else:
            self.sqlConnectionEdit.setText(_translate("MainWindow", ":memory:"))
        self.sqlRequestEdit.setText(_translate("MainWindow", "SELECT name FROM sqlite_master WHERE type='table'"))
        self.allTableButton.setText(_translate("MainWindow", "All Tables"))
        self.pushButton.setText(_translate("MainWindow", "Query"))
