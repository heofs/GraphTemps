#! /usr/bin/env python3
import sys
from PyQt5 import QtWidgets
import pyqtgraph

from design import Ui_MainWindow
from getData import GetLogData

class Application(Ui_MainWindow, GetLogData):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

        self.plotButtonStart.clicked.connect(self.plotStart)
        self.plotButtonEnd.clicked.connect(self.plotEnd)

        self.PlotStart = GetLogData('Start')
        self.PlotEnd = GetLogData('End')


        self.horizontalSlider.setMaximum(self.getLogLength())


    def plotStart(self):
        print('Plotting start..')
        pgwindow.clear()
        graphingNumber = self.horizontalSlider.value()
        self.data = self.PlotStart.getData(graphingNumber)

        self.curve = self.plot.getPlotItem().plot()
        prog.curve.setData(prog.data)

    def plotEnd(self):
        print('Plotting end..')
        pgwindow.clear()
        graphingNumber = self.horizontalSlider.value()
        self.data = self.PlotEnd.getData(graphingNumber)

        self.curve = self.plot.getPlotItem().plot()
        prog.curve.setData(prog.data)

        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    dialog = QtWidgets.QMainWindow()
    prog = Application(dialog)

    pgwindow = prog.plot
    #pgwindow.setRange(yRange=[-5, 40])

    dialog.show()
    sys.exit(app.exec_())
