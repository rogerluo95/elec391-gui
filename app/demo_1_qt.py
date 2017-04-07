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

class DtcPageWindow(QMainWindow, Ui_HomePage):


    def __init__(self, headless=False):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.headless = headless
        #self._setup_slots()
        self.setWindowModality(Qt.ApplicationModal)
        self.update_date()

    def _setup_slots(self):
        """
        Setup the slots for receiving button clicking events to:
            1. Trigger other methods to start a thread, and exit the application
            2. Flip pages to view multiple DTC on the text box for each sensor

        """
        self.action_connect_and_run.clicked.connect(self.run_thread)
        self.action_exit.clicked.connect(self.close_application)

    def update_date(self):
        """
        Get the current date and display on the date label of the UI
        """
        self.curr_day = QDate.currentDate().toString('MMMM d, yyyy')
        self.date.setText(self.curr_day)

    def run_thread(self):
        """
        Instanciates and fire up a QThread used for receiving pre-processed
        DTC strings via Bluetooth from the Network Interface Module;
        Receives the signals emitted from the thread and calls the update_sensor_xx
        to update the DTCs in real-time.
        """
        self.dtc_message = SerialMessage(self)
        self.dtc_message.start()

        self.dtc_message.dtc_codes_sig_fl.connect(self.update_sensor_fl)
        self.dtc_message.dtc_codes_sig_fr.connect(self.update_sensor_fr)
        self.dtc_message.dtc_codes_sig_rl.connect(self.update_sensor_rl)
        self.dtc_message.dtc_codes_sig_rr.connect(self.update_sensor_rr)

    def close_application(self):
        """
        Quit the application when the "Exit" button is clicked and print a message
        to indicate the application is closed.

        """
        print("Thanks for using LoQi!")
        sys.exit()


class SerialMessage(QThread):
    """
    Represents the QThread seperated from the main window to establish Bluetooth(serial)
    connection with the Network Interface Module.
    When the thread is running:
        1. Slice the DTC string coming from Bluetooth
        2. Emit the string ti the main application for display

    Args:
        headless (Optional[bool]): Determines whether or not to display a GUI. Defaults to False.
            Used for testing purposes.

    Attributes:
        port: The name of the Bluetooth device configured in the operating system
            as a serial port to establish wireleess conenction.
        ser: The serial conenction to be established, given the port, baudrate,
            and timeout.
    """


    dtc_codes_sig_fl = pyqtSignal(list)
    """DTC String for the Front Left Sensor"""
    dtc_codes_sig_fr = pyqtSignal(list)
    """DTC String for the Front Right Sensor"""
    dtc_codes_sig_rl = pyqtSignal(list)
    """DTC String for the Rear Left Sensor"""
    dtc_codes_sig_rr = pyqtSignal(list)
    """DTC String for the Rear Right Sensor"""

    def __init__(self, headless=False):
        super(self.__class__, self).__init__()

        self.port = "COM3"
        self.ser = serial.Serial(self.port, 9600, timeout = None)
        print "Connected to", self.port


    def run(self):
        while True:
            self.process_dtc_stream();

    def process_dtc_stream(self):
        """
        Receives pre-processed DTC strings via bluetooth and store the information
        into a list of DTC codes. Stores the first 3 bytes of the string as "dtc_confirm".

        Process the rest of the string in the following steps:

            1. Get chunks of data, each containing a 4-byte DTC
            2. Eliminate the spaces between each byte
            3. Eliminate the useless "FF" data byte at the end of the string

        Result in a list *dtc_list (list)*

        Emit the resulting list through pyqtSignals depending on the response ID of sensors
            to the main application for further decoding and display.

        """
        self.line = self.ser.readline()
        self.n = 12
        if len(self.line) > 0 and len(str(self.line).split(',')) == 2:
            self.dtc_id, self.dtc_codes = str(self.line).split(',') # Split id and data

            self.dtc_confirm = self.dtc_codes[0:9]   #skipping the first 3 bytes of response
            self.dtc_str = self.dtc_codes[9:]        #content of the DTC codes

            self.dtc_1 = [self.dtc_str[i:i+self.n][0:11] for i in range(0, len(self.line),self.n)]
            self.dtc_2 = [self.dtc_1[i].replace(" ","") for i in range(0, len(self.dtc_1)-2)]
            self.dtc_list = [ x for x in self.dtc_2 if "ff" not in x ]
            print self.dtc_list

            #Send signals to corresponding sensors
            if self.dtc_id == "0x18daf223":
                self.dtc_codes_sig_fl.emit(self.dtc_list)
            elif self.dtc_id == "0x18daf224":
                self.dtc_codes_sig_fr.emit(self.dtc_list)
            elif self.dtc_id == "0x73e":
                self.dtc_codes_sig_rl.emit(self.dtc_list)
            elif self.dtc_id == "0x7d5":
                self.dtc_codes_sig_rr.emit(self.dtc_list)


if __name__ == '__main__':
    main(DtcPageWindow)
