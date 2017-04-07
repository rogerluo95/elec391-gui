"""
.. module:: demo_2_graphic_qt
   :platform: Windows, Linux (Raspbian-ARM)
   :synopsis: Define the main User Interface for the ELEC 391 Group C3 (W2016 T2)
              Demo 3
              This module uses pyqtgraph as the plotting framework
   :Revision History:
              2017-03-17: GUI used for Final Project Demo. Featuring:
                        - 4 Live graph showing the Force vs. Position
                        - 1 Device Monitor showing motor status
                        - Value display for position variable visualization
                        - Gear Position indicator based on the position current state
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
from PyQt4.QtCore import Qt, QThread, QString, pyqtSignal, QDate, QTimer, QString

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


#import for Matplotlib
import numpy as np
import pyqtgraph as pg
import random

from demo_3_graphic import Ui_HomePage
from main_qt import main

class HomePage(QMainWindow, Ui_HomePage):


    def __init__(self, headless=False):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.headless = headless
        self.setWindowModality(Qt.ApplicationModal)
        self.update_date()
        self.showFullScreen()
        self.hide_gear_positions()

        #self.text_file = open("//vmware-host/Shared Folders/ELEC 391/02_Control/05_Data_log/"
        #                                                        +self.start_time+".txt","w")
        self.text_file = open("log/"+self.start_time+".txt","w")

        self.setup_graph()
        self.run_thread()
        self._setup_slots()


    def _setup_slots(self):
        self.action_exit.clicked.connect(self.close_application)

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
        self.arm.setColor(QColor(255,255,255,255))
        self.arm.setWidth(0.99)
        self.wall_color = QPen()
        self.wall_color.setColor(QColor(255,255,255,255))
        self.wall_color.setWidth(0.3)
        self.gear_color = QPen()
        self.gear_color.setColor(QColor(0,255,0,150))
        self.gear_color.setWidth(0.9)
        self.boundary_color = QPen()
        self.boundary_color.setColor(QColor(255,0,0,150))
        self.boundary_color.setWidth(0.9)
        # set up plot of the device
        self.device = pg.PlotWidget(title = "Device Monitor")
        self.device.setRange(xRange=[-30,30])
        self.device.setRange(yRange=[-0.7,10])
        self.device.hideAxis("left")
        self.device.plotItem.plot()
        self.device_container.addWidget(self.device)

        # set up plots of data flow
        # generic chunk settings
        self.chunk_size = 100
        self.max_chunks = 10
        self.start_time = pg.ptime.time()
        # plot 0
        self.plot_0 = pg.PlotWidget(title = "X Position")
        self.plot_0.setLabel('bottom','Time', 's')
        self.plot_0.setLabel('left','X', 'cm')
        self.plot_0.setXRange(-10,0)
        self.data_to_plot_0 = np.empty((self.chunk_size+1,2))
        self.ptr_0 = 0
        self.curves_0 = []
        self.plot_0.plotItem.plot()
        self.plot_container_up_l.addWidget(self.plot_0)
        # plot 1
        self.plot_1 = pg.PlotWidget(title = "X Force")
        self.plot_1.setLabel('bottom','Time', 's')
        self.plot_1.setLabel('left','Force on X Direction', 'N')
        self.plot_1.setXRange(-10,0)
        self.data_to_plot_1 = np.empty((self.chunk_size+1,2))
        self.ptr_1 = 0
        self.curves_1 = []
        self.plot_1.plotItem.plot()
        self.plot_container_btm_l.addWidget(self.plot_1)
        # plot 2
        self.plot_2 = pg.PlotWidget(title = "Y Position")
        self.plot_2.setLabel('bottom','Time', 's')
        self.plot_2.setLabel('left','Y', 'cm')
        self.plot_2.setXRange(-10,0)
        self.data_to_plot_2 = np.empty((self.chunk_size+1,2))
        self.ptr_2 = 0
        self.curves_2 = []
        self.plot_2.plotItem.plot()
        self.plot_container_up_r.addWidget(self.plot_2)
        # plot 3
        self.plot_3 = pg.PlotWidget(title = "Y Force")
        self.plot_3.setLabel('bottom','Time', 's')
        self.plot_3.setLabel('left','Force on Y Direction', 'N')
        self.plot_3.setXRange(-10,0)
        self.data_to_plot_3 = np.empty((self.chunk_size+1,2))
        self.ptr_3 = 0
        self.curves_3 = []
        self.plot_3.plotItem.plot()
        self.plot_container_btm_r.addWidget(self.plot_3)

    def update_device(self,q1,q2,x,y,q1_active,q2_active):
        #Plot the Device itself
        self.device.clear()
        self.arm_L = self.device.plot([q1,x], [0,y], pen=self.arm)
        self.arm_R = self.device.plot([x,q2], [y,0], pen=self.arm)
        self.motor_L_ro = self.device.plot([q1,-15], [0,0], pen=self.rotor)
        self.motor_R_ro = self.device.plot([q2,15], [0,0], pen=self.rotor)
        self.motor_L = self.device.plot(list(range(-30,-15)), [0]*15, pen=self.motor)
        self.motor_R = self.device.plot(list(range(16,31)), [0]*15, pen=self.motor)
        #Plot the activity
        self.motor_L_active = self.device.plot([-24.5, -24.5+q1_active], [1,1], pen=self.motor_active)
        self.motor_R_active = self.device.plot([24.5, 24.5+q2_active], [1,1], pen=self.motor_active)
        self.region_1_left = self.device.plot([-1,-1], [9.55,9.7],pen=self.wall_color)
        self.region_1_right = self.device.plot([1,1], [9.55,9.7],pen=self.wall_color)
        self.region_2_top = self.device.plot([1,2], [9.55,9.55],pen=self.wall_color)
        self.region_2_top_boundary = self.device.plot([2,3.5], [9.55,9.55],pen=self.boundary_color)
        self.region_2_bottom = self.device.plot([1,2], [7.15,7.15],pen=self.wall_color)
        self.region_2_bottom_boundary = self.device.plot([2,3.5], [7.15,7.15],pen=self.boundary_color)
        self.region_3_left = self.device.plot([-1,-1], [4.6,7.15],pen=self.wall_color)
        self.region_3_right = self.device.plot([1,1], [4.6,7.15],pen=self.wall_color)
        self.region_4_top = self.device.plot([-2,-1], [9.55,9.55],pen=self.wall_color)
        self.region_4_top_boundary = self.device.plot([-3.5,-2], [9.55,9.55],pen=self.boundary_color)
        self.region_4_bottom_boundary = self.device.plot([-3.5,-2], [7.15,7.15],pen=self.boundary_color)
        self.region_4_bottom = self.device.plot([-2,-1], [7.15,7.15],pen=self.wall_color)
        self.ev_right = self.device.plot([-2,-2], [7.15,9.55],pen=self.gear_color)
        self.p_left = self.device.plot([2,2], [7.15,9.55],pen=self.gear_color)
        self.N_left = self.device.plot([-1,-1], [7.15,9.55],pen=self.gear_color)
        self.N_right = self.device.plot([1,1], [7.15,9.55],pen=self.gear_color)
        self.N_top = self.device.plot([-1,1], [9.55,9.55],pen=self.gear_color)
        self.N_bottom = self.device.plot([-1,1], [7.15,7.15],pen=self.gear_color)
        self.R_top = self.device.plot([-1,1], [9.55,  9.55],pen=self.gear_color)
        self.R_bottom = self.device.plot([-1,1], [9.7,9.7],pen=self.gear_color)
        self.D_top = self.device.plot([-1,1], [7.15,7.15],pen=self.gear_color)
        self.D_bottom = self.device.plot([-1,1], [5.2,5.2],pen=self.gear_color)

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
                self.plot_1.removeItem(self.c_1)
        else:
            self.curve_1 = self.curves_1[-1]
        self.data_to_plot_1[self.i_1+1,0] = self.now - self.start_time
        self.data_to_plot_1[self.i_1+1,1] = data_1
        self.curve_1.setData(x=self.data_to_plot_1[:self.i_1+2,0], y=self.data_to_plot_1[:self.i_1+2,1])
        self.ptr_1 += 1

    def update_plot_2(self,data_2):
        for self.c_2 in self.curves_2:
            self.c_2.setPos(-(self.now-self.start_time),0)

        self.i_2 = self.ptr_2 % self.chunk_size
        if self.i_2 == 0:
            self.curve_2 = self.plot_2.plot()
            self.curves_2.append(self.curve_2)
            self.last_2 = self.data_to_plot_2[-1]
            self.data_to_plot_2 = np.empty((self.chunk_size+1,2))
            self.data_to_plot_2[0] = self.last_2
            while len(self.curves_2) > self.max_chunks:
                self.c_2 = self.curves_2.pop(0)
                self.plot_2.removeItem(self.c_2)
        else:
            self.curve_2 = self.curves_2[-1]
        self.data_to_plot_2[self.i_2+1,0] = self.now - self.start_time
        self.data_to_plot_2[self.i_2+1,1] = data_2
        self.curve_2.setData(x=self.data_to_plot_2[:self.i_2+2,0], y=self.data_to_plot_2[:self.i_2+2,1])
        self.ptr_2 += 1

    def update_plot_3(self,data_3):
        for self.c_3 in self.curves_3:
            self.c_3.setPos(-(self.now-self.start_time),0)

        self.i_3 = self.ptr_3 % self.chunk_size
        if self.i_3 == 0:
            self.curve_3 = self.plot_3.plot()
            self.curves_3.append(self.curve_3)
            self.last_3 = self.data_to_plot_3[-1]
            self.data_to_plot_3 = np.empty((self.chunk_size+1,2))
            self.data_to_plot_3[0] = self.last_3
            while len(self.curves_3) > self.max_chunks:
                self.c_3 = self.curves_3.pop(0)
                self.plot_3.removeItem(self.c_3)
        else:
            self.curve_3 = self.curves_3[-1]
        self.data_to_plot_3[self.i_3+1,0] = self.now - self.start_time
        self.data_to_plot_3[self.i_3+1,1] = data_3
        self.curve_3.setData(x=self.data_to_plot_3[:self.i_3+2,0], y=self.data_to_plot_3[:self.i_3+2,1])
        self.ptr_3 += 1

    def update_text(self, message_list):
        self.mode = float(message_list[0])
        if self.mode == 0:
            self.clear_ui()
            self.set_mode_0_ui()
        elif self.mode == 1:
            self.clear_ui()
            self.set_mode_1_ui()
        elif self.mode == 2:
            self.set_mode_2_ui()
        elif self.mode == 3:
            self.set_mode_3_ui()
        elif self.mode == 4:
            self.set_mode_4_ui()

        self.handle_force = int(message_list[1])
        self.pulse_cnt_l = float(message_list[2])
        self.pulse_cnt_r = float(message_list[3])
        self.q1 = float(message_list[6])
        self.q2 = float(message_list[7])
        self.x = float(message_list[8])
        self.y = float(message_list[9])
        self.x_v = float(message_list[12])
        self.y_v = float(message_list[13])
        self.j11 = float(message_list[14])
        self.j12 = float(message_list[15])
        self.j21 = float(message_list[16])
        self.j22 = float(message_list[17])
        self.path = int(message_list[18])
        self.path_total = int(message_list[19])
        self.gear = float (message_list[20])
        self.next_gear = float (message_list[21])
        self.force_x = float(message_list[22])
        self.force_y = float(message_list[23])
        self.force_q1 = float(message_list[24])
        self.force_q2 = float(message_list[25])
        self.pwm_q1 = float(message_list[26])
        self.pwm_q2 = float(message_list[27])

        if self.gear == 11:
            self.gear_letter = "N";
        elif self.gear == 12:
            self.gear_letter = "P";
        elif self.gear == 13:
            self.gear_letter = "R";
        elif self.gear == 14:
            self.gear_letter = "EV";
        elif self.gear == 15:
            self.gear_letter = "D";
        else:
            self.gear_letter = "INIT"


        if self.next_gear == 11:
            self.gear_letter_next = "N";
        elif self.next_gear == 12:
            self.gear_letter_next = "P";
        elif self.next_gear == 13:
            self.gear_letter_next = "R";
        elif self.next_gear == 14:
            self.gear_letter_next = "EV";
        elif self.next_gear == 15:
            self.gear_letter_next = "D";
        else:
            self.gear_letter_next = "INIT"

        if self.mode == 4:
            self.gear_position.setText(self.gear_letter)
        else:
            self.gear_position.setText(str(self.path)+"/"+str(self.path_total))

        self.q1_data.setText(str(self.q1) + " cm")
        self.q2_data.setText(str(self.q2) + " cm")
        self.x_data.setText(str(self.x) + " cm")
        self.y_data.setText(str(self.y) + " cm")
        self.j11_name.setText("X_Velocity")
        self.j11_data.setText(str(self.x_v) )
        self.j12_name.setText("Y_Velocity")
        self.j12_data.setText(str(self.y_v) )
        self.j21_name.setText("PWM_Q1")
        self.j21_data.setText(str(self.pwm_q1) )
        self.j22_name.setText("PWM_Q2")
        self.j22_data.setText(str(self.pwm_q2) )

        # compute activity
        if self.force_q1 <= 0:
            self.q1_active = 5*(self.pwm_q1)/255
        else:
            self.q1_active = 5*(self.pwm_q1)/255
        if self.force_q2 <= 0:
            self.q2_active = 5*(self.pwm_q2)/255
        else:
            self.q2_active = 5*(self.pwm_q2)/255
        self.update_device(self.q1, self.q2, self.x, self.y, self.q1_active, self.q2_active)
        self.update_plot_0(self.x)
        self.update_plot_1(self.force_x)
        self.update_plot_2(self.y)
        self.update_plot_3(self.force_y)

        if self.gear_letter == "P":
            self.at_p.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 255);\nfont: 75 40pt \"Forza Medium\";"))
        elif self.gear_letter_next == "P":
            self.at_p.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 180);\nfont: 75 35pt \"Forza Medium\";"))
        else:
            self.at_p.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\nfont: 75 25pt \"Forza Medium\";"))

        if self.gear_letter == "R":
            self.at_r.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 255);\nfont: 75 40pt \"Forza Medium\";"))
        elif self.gear_letter_next == "R":
            self.at_r.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 150);\nfont: 75 30pt \"Forza Medium\";"))
        else:
            self.at_r.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\nfont: 75 25pt \"Forza Medium\";"))

        if self.gear_letter == "N":
            self.at_n.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 255);\nfont: 75 40pt \"Forza Medium\";"))
        elif self.gear_letter_next == "N":
            self.at_n.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 150);\nfont: 75 30pt \"Forza Medium\";"))
        else:
            self.at_n.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\nfont: 75 25pt \"Forza Medium\";"))

        if self.gear_letter == "D":
            self.at_d.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 255);\nfont: 75 40pt \"Forza Medium\";"))
        elif self.gear_letter_next == "D":
            self.at_d.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 150);\nfont: 75 30pt \"Forza Medium\";"))
        else:
            self.at_d.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\nfont: 75 25pt \"Forza Medium\";"))

        if self.gear_letter == "EV":
            self.at_ev.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 255);\nfont: 75 40pt \"Forza Medium\";"))
        elif self.gear_letter_next == "EV":
            self.at_ev.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 150);\nfont: 75 30pt \"Forza Medium\";"))
        else:
            self.at_ev.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\nfont: 75 25pt \"Forza Medium\";"))

    def clear_ui(self):
        self.setStyleSheet(_fromUtf8("QMainWindow {\n"
" background-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.801136 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 191));\n"
"}"))
        self.j21_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.j22_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.hide_gear_positions()
        self.title.setText("Move the handle to the lowest position")
        self.gear_position.setText("")
        self.mode_display.setText("")
        self.q1_data.setText("")
        self.q2_data.setText("")
        self.x_data.setText("")
        self.y_data.setText("")
        self.j11_name.setText("")
        self.j11_data.setText("Calibration")
        self.j12_name.setText("")
        self.j12_data.setText("Calibration")
        self.j21_name.setText("")
        self.j21_data.setText("")
        self.j22_name.setText("")
        self.j22_data.setText("")
        self.device.clear()
        self.plot_0.clear()
        self.plot_1.clear()
        self.plot_2.clear()
        self.plot_3.clear()
        self.plot_4.clear()

    #blue
    def set_mode_0_ui(self):
        self.title.setText("Move the handle to the lowest position")
        self.j11_data.setText("Calibration")
        self.j21_data.setText("")
        self.j12_data.setText("Calibration")
        self.j22_data.setText("")
        self.hide_gear_positions()

    def set_mode_1_ui(self):
        self.title.setText("Move the handle to the lowest position")
        self.j11_data.setText("Calibration")
        self.j21_data.setStyleSheet("color: rgb(255,255,255);background-color: rgba(0,255,0,200)")
        self.j21_data.setText("Successful")
        self.j12_data.setText("Calibration")
        self.j22_data.setText("")
        self.hide_gear_positions()

    def set_mode_2_ui(self):
        self.setStyleSheet(_fromUtf8("QMainWindow {\n"
" background-color:  qlineargradient(spread:pad, x1:1, y1:0.721, x2:1, y2:1, stop:0.232955 rgba(0, 0, 0, 255), stop:1 rgba(62, 90, 102, 234));\n"
"}"))
        self.title.setText("Welcome!")
        self.j11_data.setText("Calibration")
        self.j21_data.setStyleSheet("color: rgb(255,255,255);background-color: rgba(0,255,0,200)")
        self.j21_data.setText("Successful")
        self.j12_data.setText("Calibration")
        self.j22_data.setStyleSheet("color: rgb(255,255,255);background-color: rgba(0,255,0,200)")
        self.j22_data.setText("Successful")

    def set_mode_3_ui(self):
        self.title.setText("")
        self.j21_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.j22_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.hide_gear_positions()
        self.mode_display.setText("Autonomous\n Motion")

    def set_mode_4_ui(self):
        self.title.setText("SHIFT-BY-WIRE")
        self.j21_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.j22_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.at_p.show()
        self.at_r.show()
        self.at_n.show()
        self.at_d.show()
        self.at_ev.show()
        self.at_bar_1.show()
        self.at_bar_2.show()
        self.mode_display.setText("Haptics")

    def hide_gear_positions(self):
        self.at_p.hide()
        self.at_r.hide()
        self.at_n.hide()
        self.at_d.hide()
        self.at_ev.hide()
        self.at_bar_1.hide()
        self.at_bar_2.hide()

    def write_file(self, message_list):
        if "0" or "1" or "2" or "3" not in message_list[0]:
            for item in message_list:
                self.text_file.write("%s " %item)

    def run_thread(self):
        self.serial_message = SerialMessage(self)
        self.serial_message.start()
        self.serial_message.msg_signal.connect(self.update_text)
        self.serial_message.msg_signal.connect(self.write_file)

    def close_application(self):
        sys.exit()

class SerialMessage(QThread):

    """Splitted Message strings from the Arduino"""
    msg_signal = pyqtSignal(list)

    def __init__(self, headless=False):
        super(self.__class__, self).__init__()

        self.port = "COM3"
        self.ser = serial.Serial(self.port, 9600, timeout = None)
        print "Connected to", self.port

    def run(self):
        while True:
            self.process_message_stream();

    def process_message_stream(self):

        self.line = self.ser.readline()
        if len(self.line) > 0 :
            self.msg_list = [None]*27
            self.msg_list = str(self.line).split(',') # Split the output of Arduino
            self.msg_signal.emit(self.msg_list)

if __name__ == '__main__':
    main(HomePage)
