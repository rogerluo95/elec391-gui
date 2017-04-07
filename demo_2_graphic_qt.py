"""
.. module:: demo_2_graphic_qt
   :platform: Windows, Linux (Raspbian-ARM)
   :synopsis: Define the main User Interface for the ELEC 391 Group C3 (W2016 T2)
              Demo 2
              This module uses pyqtgraph as the plotting framework
   :Revision History:
              2017-02-20: v0.1 Connect with Matplotlib for plotting the Handle Position
                               and the motor status

.. moduleauthor: Roger (Sichen) Luo - The University of British Columbia
"""

import sys
import serial
import time
import datetime
import math
from os import path

#import for PyQt
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QPen, QColor, QGraphicsItem
from PyQt4.QtCore import Qt, QThread, QString, pyqtSignal, QDate, QTimer

#import for Matplotlib
import numpy as np
import pyqtgraph as pg
import random

from demo_2_graphic import Ui_HomePage
from main_qt import main

class HomePage(QMainWindow, Ui_HomePage):


    def __init__(self, headless=False):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.headless = headless
        self.setWindowModality(Qt.ApplicationModal)
        self.update_date()
        #self.text_file = open("//vmware-host/Shared Folders/ELEC 391/02_Control/05_Data_log/"
        #                                                        +self.start_time+".txt","w")
        #self.text_file = open("log/"+self.start_time+".txt","w")

        self.setup_graph()
        self.run_thread()

    def update_date(self):
        self.start_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        self.curr_day = QDate.currentDate().toString('MMMM d, yyyy')
        self.date.setText(self.curr_day)

    def setup_graph(self):
        # set up Pen for plotting the device
        self.motor = QPen()
        self.motor.setColor(QColor(255,255,255))
        self.motor.setWidth(3)
        self.motor_active = QPen()
        self.motor_active.setColor(QColor(254,102,13))
        self.motor_active.setWidth(1)
        self.rotor = QPen()
        self.rotor.setColor(QColor(125,125,125))
        self.rotor.setWidth(1)
        self.arm = QPen()
        self.arm.setColor(QColor(0,100,104,150))
        self.arm.setWidth(0.5)
        self.arm_fake = QPen()
        self.arm_fake.setColor(QColor(23,161,165))
        self.arm_fake.setWidth(0.99)
        self.wall_color = QPen()
        self.wall_color.setColor(QColor(255,255,255,150))
        self.wall_color.setWidth(0.5)
        # set up plot of the device
        self.device = pg.PlotWidget(title = "Device Monitor")
        self.device.setRange(xRange=[-30,30])
        self.device.setRange(yRange=[-0.7,15])
        self.device.hideAxis("left")
        self.device.plotItem.plot()
        self.device_container.addWidget(self.device)
        # set up plots of data flow
        # generic chunk settings
        self.chunk_size = 100
        self.max_chunks = 10
        self.start_time = pg.ptime.time()
        # plot 0
        self.plot_0 = pg.PlotWidget(title = "Y Position")
        self.plot_0.setLabel('bottom','Time', 's')
        self.plot_0.setLabel('left','Y', 'cm')
        self.plot_0.setXRange(-10,0)
        self.data_to_plot_0 = np.empty((self.chunk_size+1,2))
        self.ptr_0 = 0
        self.curves_0 = []
        self.plot_0.plotItem.plot()
        self.plot_container_0.addWidget(self.plot_0)
        # plot 1
        self.plot_1 = pg.PlotWidget(title = "Y Force")
        self.plot_1.setLabel('bottom','Time', 's')
        self.plot_1.setLabel('left','Force on Y Direction', 'N')
        self.plot_1.setXRange(-10,0)
        self.data_to_plot_1 = np.empty((self.chunk_size+1,2))
        self.ptr_1 = 0
        self.curves_1 = []
        self.plot_1.plotItem.plot()
        self.plot_container_1.addWidget(self.plot_1)

    def update_device(self,q1,q2,x,y,q1_active,q2_active):
        #Plot the Device itself
        self.device.clear()
        #self.wall = 7
        #if y > self.wall:
        #    self.y = self.wall
        #else:
        #    self.y = y
        self.arm_L = self.device.plot([q1,x], [0,y], pen=self.arm_fake)
        self.arm_R = self.device.plot([x,q2], [y,0], pen=self.arm_fake)
        self.arm_L = self.device.plot([q1,x], [0,y], pen=self.arm)
        self.arm_R = self.device.plot([x,q2], [y,0], pen=self.arm)
        self.motor_L_ro = self.device.plot([q1,-15], [0,0], pen=self.rotor)
        self.motor_R_ro = self.device.plot([q2,15], [0,0], pen=self.rotor)
        self.motor_L = self.device.plot(list(range(-30,-15)), [0]*15, pen=self.motor)
        self.motor_R = self.device.plot(list(range(16,31)), [0]*15, pen=self.motor)
        #Plot the activity
        self.motor_L_active = self.device.plot([-24.5, -24.5+q1_active], [1,1], pen=self.motor_active)
        self.motor_R_active = self.device.plot([24.5, 24.5+q2_active], [1,1], pen=self.motor_active)
        if self.mode == 4:
            self.bound_1 = self.device.plot([-10,10], [6.5,6.5],pen=self.wall_color)
            self.bound_2 = self.device.plot([-10,10], [10,10],pen=self.wall_color)
            #self.bound_3 = self.device.plot([-10,10], [11,11],pen=self.wall_color)


    def update_plot_0(self,data_0):
        self.now = pg.ptime.time()
        for self.c_0 in self.curves_0:
            self.c_0.setPos(-(self.now-self.start_time),0)

        self.i_0 = self.ptr_0 % self.chunk_size
        if self.i_0 == 0:
            self.curve_0 = self.plot_0.plot()
            self.curves_0.append(self.curve_0)
            self.last_0 = self.data_to_plot_0[-1]
            self.data_to_plot_0 = np.empty((self.chunk_size+1,2))
            self.data_to_plot_0[0] = self.last_0
            while len(self.curves_0) > self.max_chunks:
                self.c_0 = self.curves_0.pop(0)
                self.plot_0.removeItem(self.c_0)
        else:
            self.curve_0 = self.curves_0[-1]
        self.data_to_plot_0[self.i_0+1,0] = self.now - self.start_time
        self.data_to_plot_0[self.i_0+1,1] = data_0
        self.curve_0.setData(x=self.data_to_plot_0[:self.i_0+2,0], y=self.data_to_plot_0[:self.i_0+2,1])
        self.ptr_0 += 1

    def update_plot_1(self,data_1):
        for self.c_1 in self.curves_1:
            self.c_1.setPos(-(self.now-self.start_time),0)

        self.i_1 = self.ptr_1 % self.chunk_size
        if self.i_1 == 0:
            self.curve_1 = self.plot_1.plot()
            self.curves_1.append(self.curve_1)
            self.last_1 = self.data_to_plot_1[-1]
            self.data_to_plot_1 = np.empty((self.chunk_size+1,2))
            self.data_to_plot_1[0] = self.last_1
            while len(self.curves_1) > self.max_chunks:
                self.c_1 = self.curves_1.pop(0)
                self.plot_0.removeItem(self.c_1)
        else:
            self.curve_1 = self.curves_1[-1]
        self.data_to_plot_1[self.i_1+1,0] = self.now - self.start_time
        self.data_to_plot_1[self.i_1+1,1] = data_1
        self.curve_1.setData(x=self.data_to_plot_1[:self.i_1+2,0], y=self.data_to_plot_1[:self.i_1+2,1])
        self.ptr_1 += 1


    def update_text(self, message_list):
        self.mode = float(message_list[0])

        if self.mode == 0:
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(90,166,219,100)")
            self.mode_4.setText("INITIALIZING...\n\nMove to the left\nto calibrate\nthe Left motor")
        elif self.mode == 1:
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(90,166,219,100)")
            self.mode_4.setText("INITIALIZING...\n\nMove to the right\nto calibrate\nthe Right motor")
        elif self.mode == 2:
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(0,255,0,100)")
            self.mode_4.setText("CALIBRATION\nSUCCESSFUL\n\nReady to use the device")
        elif self.mode == 3:
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_4.setText("Autonomous Mode")
        elif self.mode == 4:
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_4.setText("Haptic Mode")


        self.q1 = float(message_list[4])
        self.q2 = float(message_list[6])
        self.x = float(message_list[7])
        self.y = float(message_list[8])
        self.x_v = float(message_list[9])
        self.y_v = float(message_list[10])
        self.current_handle_state = float (message_list[11])
        self.next_handle_state = float (message_list[12])
        self.force_x = float(message_list[13])
        self.force_y = float(message_list[14])
        self.force_q1 = float(message_list[15])
        self.force_q2 = float(message_list[16])
        self.pwm_q1 = float(message_list[17])
        self.pwm_q2 = float(message_list[18])
        self.pressure = float(message_list[19])

        self.name_0.setText("Q1")
        self.data_0.setText(str(self.q1) + " cm")
        self.name_1.setText("Q2")
        self.data_1.setText(str(self.q2) + " cm")
        self.name_2.setText("X")
        self.data_2.setText(str(self.x) + " cm")
        self.name_3.setText("Y")
        self.data_3.setText(str(self.y) + "2 cm")
        self.name_4.setText("Y Velocity")
        self.data_4.setText(str(self.y_v) +  " m/s^2")
        self.name_5.setText("Y Force")
        self.data_5.setText(str(self.force_y) +  " N")
        self.name_6.setText("Q2 Force")
        self.data_6.setText(str(self.force_q2) +  " N")
        self.name_7.setText("Q2 PWM")
        self.data_7.setText(str(self.pwm_q2))

        self.mode_0.setText("4")
        self.mode_1.setText("3")
        self.mode_2.setText("2")
        self.mode_3.setText("1")

        if self.current_handle_state == 4 :
            self.mode_0.setStyleSheet("color: rgb(255,255,255);background-color: rgba(0,255,0,200)")
            self.mode_1.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_2.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_3.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
        elif self.current_handle_state == 3:
            self.mode_0.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_1.setStyleSheet("color: rgb(255,255,255);background-color: rgba(0,255,0,200)")
            self.mode_2.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_3.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
        elif self.current_handle_state == 2:
            self.mode_0.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_1.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_2.setStyleSheet("color: rgb(255,255,255);background-color: rgba(0,255,0,200)")
            self.mode_3.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
        elif self.current_handle_state == 1:
            self.mode_0.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_1.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_2.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_3.setStyleSheet("color: rgb(255,255,255);background-color: rgba(0,255,0,200)")
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
        elif self.current_handle_state == 0:
            self.mode_0.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_1.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_2.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_3.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,255,255,30)")
            self.mode_4.setStyleSheet("color: rgb(255,255,255);background-color: rgba(255,0,0,200)")
            self.mode_4.setText("Reset the Device")

        # compute activity
        if self.force_q1 < 0:
            self.q1_active = -5*(self.pwm_q1)/255
        else:
            self.q1_active = 5*(self.pwm_q1)/255
        if self.force_q2 < 0:
            self.q2_active = -5*(self.pwm_q2+1)/255
        else:
            self.q2_active = 5*(self.pwm_q2+1)/255

        self.update_device(self.q1, self.q2, self.x, self.y, self.q1_active, self.q2_active)
        self.update_plot_0(self.y)
        self.update_plot_1(self.force_y)

    def write_file(self, message_list):
        for item in message_list:
            self.text_file.write("%s " %item)

    def run_thread(self):
        self.serial_message = SerialMessage(self)
        self.serial_message.start()
        self.serial_message.msg_signal.connect(self.update_text)
        self.serial_message.msg_signal.connect(self.write_file)
        #self.serial_message.msg_signal.connect(self.get_position)

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
            self.msg_list = [None]*20
            self.msg_list = str(self.line).split(',') # Split the output of Arduino
            self.msg_signal.emit(self.msg_list)
            #print self.msg_list

if __name__ == '__main__':
    main(HomePage)
