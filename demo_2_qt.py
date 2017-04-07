"""
.. module:: demo_2_qt
   :platform: Windows, Linux (Raspbian-ARM)
   :synopsis: Define the main User Interface for the ELEC 391 Group C3 (W2016 T2)
              Demo 2
   :Revision History:
              2017-02-20: v0.1 Connect with Matplotlib for plotting the Handle Position
                               and the motor status

.. moduleauthor: Roger (Sichen) Luo - The University of British Columbia
"""

import sys
import serial
import time
from os import path

#import for PyQt
from PyQt4.QtGui import QApplication, QMainWindow, QWidget
from PyQt4.QtCore import Qt, QThread, QString, pyqtSignal, QDate

#import for Matplotlib
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

from demo_2 import Ui_HomePage
from main_qt import main

class HomePage(QMainWindow, Ui_HomePage):


    def __init__(self, headless=False):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.headless = headless
        self.setWindowModality(Qt.ApplicationModal)
        self.update_date()

        self.fig1 = Figure()
        self.sample = self.fig1.add_subplot(111)
        self.sample.plot(np.random.rand(128))
        self.addmpl(self.fig1)


    def update_date(self):
        self.curr_day = QDate.currentDate().toString('MMMM d, yyyy')
        self.date.setText(self.curr_day)

    def addmpl(self,fig):
        self.canvas = FigureCanvas(fig)
        self.device_container.addWidget(self.canvas)
        self.canvas.draw()

if __name__ == '__main__':
    main(HomePage)
