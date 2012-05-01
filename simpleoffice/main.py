# -*- coding: utf-8 -*-

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from ui.mainwindow_ui import Ui_MainWindow
from programs.simpleWord import *


class main(QMainWindow):

    def __init__(self, parent=None):
        super(main, self).__init__(parent)
        self.ui = ui = Ui_MainWindow()

        ui.setupUi(self)


    def openFile(self, file):
        pass

    def newTabOpen(self, doctype, status):
        #doctype is the format to be opened and status means if it's to create
        #a new file or use a pre-exsisting one
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('cleanlooks')
    mainWindow = main()
    mainWindow.show()
    app.exec_()
