# -*- coding: utf-8 -*-

# pyqt test work by itjunky

import sys
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

import design
import db


class DBAdminApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.requestToDb)
        self.allTableButton.clicked.connect(self.showAllTables)

    def initializeModel(self):
        self.model = ExampleData()

        dbPath = self.sqlConnectionEdit.text()
        if not db.createConnection(dbPath):
            QtWidgets.QMessageBox.about(self, 'ERROR', 'Can\'t connect to database')

    def requestToDb(self):
        self.initializeModel()
        request = self.sqlRequestEdit.text()
        self.model.setQuery(request)
        self.tableView.setModel(self.model)

    def showAllTables(self):
        self.initializeModel()
        request = "SELECT name FROM sqlite_master WHERE type='table'"
        self.model.setQuery(request)
        self.tableView.setModel(self.model)

    # A key has been pressed!
    def keyPressEvent(self, event):
        print("ent: " + str(Qt.Key_Return))
        # Did the user press the Escape key?
        key = event.key()
        print(key)
        if key == Qt.Key_Escape:
            # Close the window
            self.close()
        elif key == Qt.Key_Return:
            # Request like a button press
            self.pushButton.click()
            print('Push')

        # No:  Do nothing.


class ExampleData(QSqlQueryModel):
    def data(self, index, role):
        value = super(ExampleData, self).data(index, role)
        if value is not None and role == Qt.DisplayRole:
            # if index.column() == 0:
            #     return '#%d' % value
            # elif index.column() == 2:
            #     return value.upper()
            pass

        if role == Qt.TextColorRole and index.column() == 1:
            return QColor(Qt.blue)

        return value


def main():
    app = QtWidgets.QApplication(sys.argv)

    window = DBAdminApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
