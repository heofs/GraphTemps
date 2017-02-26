#! /usr/bin/env python3
import sys
from PyQt5 import QtWidgets

from design import Ui_MainWindow


class Application(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    dialog = QtWidgets.QMainWindow()
    prog = Application(dialog)

    dialog.show()
    sys.exit(app.exec_())
