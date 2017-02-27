#! /usr/bin/env python3
import sys
from PyQt5 import QtWidgets
import pyqtgraph

from design import Ui_MainWindow

def get_data():
    pass

class Application(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)
        self.plotButton.clicked.connect(self.plot_graph)


    def plot_graph(self):
        print('Plotting graph..')
        pgwindow.clear()
        self.data = [10, 20 ,30, 20, 10, 21, 123 , 50 , 124]
        self.curve = self.plot.getPlotItem().plot()
        prog.curve.setData(prog.data)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    dialog = QtWidgets.QMainWindow()
    prog = Application(dialog)

    pgwindow = prog.plot
    pgwindow.setRange(yRange=[-5, 40])

    dialog.show()
    sys.exit(app.exec_())
