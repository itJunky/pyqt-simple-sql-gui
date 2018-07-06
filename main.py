# pyqt test work by itjunky

import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

import design
import db

offset = 0
views = []

class DBAdminApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, dbModel=None):
        super().__init__()
        self.setupUi(self, dbModel)
        self.pushButton.clicked.connect(self.browseFolder)


    def browseFolder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose dir")

        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)

def createView(title, model):
    global offset, views

    view = QtWidgets.QTableView()
    views.append(view)
    view.setModel(model)
    view.setWindowTitle(title)
    view.adjustSize()
    view.move(100 + offset, 200 + offset)
    offset += 20
    view.show()

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

    dbPath = None
    if not db.createConnection(dbPath):
        sys.exit(1)

    exampleModel = ExampleData()
    initializeModel(exampleModel)
    window = DBAdminApp(exampleModel)

    # createView("Example", exampleModel)
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
