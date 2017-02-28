# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 546)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plot = PlotWidget(self.centralwidget)
        self.plot.setGeometry(QtCore.QRect(160, 100, 721, 441))
        self.plot.setObjectName("plot")
        self.plotButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.plotButtonStart.setGeometry(QtCore.QRect(10, 100, 131, 81))
        self.plotButtonStart.setObjectName("plotButtonStart")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(170, 30, 701, 21))
        self.horizontalSlider.setMinimum(10)
        self.horizontalSlider.setMaximum(5000)
        self.horizontalSlider.setSingleStep(10)
        self.horizontalSlider.setProperty("value", 500)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 131, 41))
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setProperty("intValue", 500)
        self.lcdNumber.setObjectName("lcdNumber")
        self.plotButtonEnd = QtWidgets.QPushButton(self.centralwidget)
        self.plotButtonEnd.setGeometry(QtCore.QRect(10, 200, 131, 81))
        self.plotButtonEnd.setObjectName("plotButtonEnd")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.sliderMoved['int'].connect(self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plotButtonStart.setText(_translate("MainWindow", "Plot Start"))
        self.plotButtonEnd.setText(_translate("MainWindow", "Plot Slutt"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

