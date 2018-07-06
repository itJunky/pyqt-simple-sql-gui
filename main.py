# pyqt test work by itjunky

import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableView
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

import design
import db

class DBSelectorApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # access to objects in design.py
        super().__init__()
        # init design
        self.setupUi(self)
        self.pushButton.clicked.connect(self.browse_folder)

        self.setStyleSheet("QTableView {background-color: transparent;}")


    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose db file")

        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)


    def browse_folder_t(self):
        # self.tableView.clear()
        table = self.createView()


def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view


class ExampleData(QSqlQueryModel):
    def data(self, index, role):
        value = super(ExampleData, self).data(index, role)
        if value is not None and role == Qt.DisplayRole:
            if index.column() == 0:
                return '#%d' % value
            elif index.column() == 2:
                return value.upper()

        if role == Qt.TextColorRole and index.column() == 1:
            return QColor(Qt.blue)

        return value


def initializeModel(model):
    model.setQuery('select * from user')
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "Name")
    model.setHeaderData(2, Qt.Horizontal, "Email")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = DBSelectorApp()
    window.show()

    if not db.createConnection(): sys.exit(1)
    exampleModel = QSqlQueryModel()
    initializeModel(exampleModel)
    createView("Example", exampleModel)
    app.exec_()


if __name__ == '__main__':
    main()
