"""
.. module:: demo_1_qt
   :platform: Windows, Linux (Raspbian-ARM)
   :synopsis: Define the main User Interface for the ELEC 391 Group C3 (W2016 T2)
              Demo 1
   :Revision History:
              2017-01-23: v0.1 Communicate with Arduino over PySerial
                               Display the output of the Arduino on the GUI

.. moduleauthor: Roger (Sichen) Luo - The University of British Columbia
"""

import sys
import serial
import time
from os import path

from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import Qt, QThread, QString, pyqtSignal, QDate

from demo_1 import Ui_HomePage
from main_qt import main

class HomePage(QMainWindow, Ui_HomePage):


    def __init__(self, headless=False):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.headless = headless
        self.setWindowModality(Qt.ApplicationModal)
        self.update_date()
        self.run_thread()


    def update_date(self):
        self.curr_day = QDate.currentDate().toString('MMMM d, yyyy')
        self.date.setText(self.curr_day)

    def update_text(self, message_list):
        self.name_0.setText("Pulse Count")
        self.data_0.setText(message_list[0])
        self.name_1.setText("Force")
        self.data_1.setText(message_list[1])
        if int(message_list[1]) > 400:
            self.data_1.setStyleSheet("color: rgb(255,255,255);background-color: rgba(0,255,0,200)")
        else:
            self.data_1.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,0,0,200)")
        self.name_3.setText("Duty Cycle")
        self.data_3.setText(message_list[2])
        self.name_4.setText("Delay 1")
        self.data_4.setText(message_list[3])
        self.name_5.setText("Delay 2")
        self.data_5.setText(message_list[4])

    def run_thread(self):

        self.serial_message = SerialMessage(self)
        self.serial_message.start()
        self.serial_message.msg_signal.connect(self.update_text)

class SerialMessage(QThread):

    """Splitted Message strings from the Arduino"""
    msg_signal = pyqtSignal(list)

    def __init__(self, headless=False):
        super(self.__class__, self).__init__()

        self.port = "COM5"
        self.ser = serial.Serial(self.port, 9600, timeout = None)
        print "Connected to", self.port

    def run(self):
        while True:
            self.process_message_stream();

    def process_message_stream(self):

        self.line = self.ser.readline()
        if len(self.line) > 0 :
            self.msg_list = str(self.line).split(',') # Split the output of Arduino
            self.msg_signal.emit(self.msg_list)
            print self.msg_list


if __name__ == '__main__':
    main(HomePage)
