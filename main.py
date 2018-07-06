# pyqt test work by itjunky

import sys, os
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
        self.pushButton.clicked.connect(self.initializeModel)


    # def browseFolder(self):
    #     self.listWidget.clear()
    #     directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Choose dir")
	#
    #     if directory:
    #         for file_name in os.listdir(directory):
    #             self.listWidget.addItem(file_name)

    def initializeModel(self):
        model = ExampleData()
        request = self.sqlRequestEdit.text()
        model.setQuery(request)
        model.setHeaderData(0, Qt.Horizontal, "ID")
        model.setHeaderData(1, Qt.Horizontal, "Name")
        model.setHeaderData(2, Qt.Horizontal, "Email")
        self.tableView.setModel(model)


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


def main():
    app = QtWidgets.QApplication(sys.argv)

    dbPath = None
    if not db.createConnection(dbPath):
        sys.exit(1)

    window = DBAdminApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
