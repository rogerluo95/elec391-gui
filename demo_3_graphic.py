# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_3_graphic.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName(_fromUtf8("HomePage"))
        HomePage.setEnabled(True)
        HomePage.resize(1440, 900)
        HomePage.setMinimumSize(QtCore.QSize(1440, 900))
        HomePage.setMaximumSize(QtCore.QSize(1440, 900))
        HomePage.setStyleSheet(_fromUtf8("QMainWindow {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0.801136 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 191));\n"
"}"))
        self.centralwidget = QtGui.QWidget(HomePage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(630, 660, 161, 81))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.output_y = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.output_y.setObjectName(_fromUtf8("output_y"))
        self.y_name = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.y_name.setFont(font)
        self.y_name.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.y_name.setAlignment(QtCore.Qt.AlignCenter)
        self.y_name.setObjectName(_fromUtf8("y_name"))
        self.output_y.addWidget(self.y_name)
        self.y_data = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.y_data.setFont(font)
        self.y_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.y_data.setText(_fromUtf8(""))
        self.y_data.setAlignment(QtCore.Qt.AlignCenter)
        self.y_data.setObjectName(_fromUtf8("y_data"))
        self.output_y.addWidget(self.y_data)
        self.mode_display = QtGui.QLabel(self.centralwidget)
        self.mode_display.setGeometry(QtCore.QRect(1240, 620, 161, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Forza Medium"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.mode_display.setFont(font)
        self.mode_display.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.mode_display.setText(_fromUtf8(""))
        self.mode_display.setAlignment(QtCore.Qt.AlignCenter)
        self.mode_display.setObjectName(_fromUtf8("mode_display"))
        self.layoutWidget_15 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_15.setGeometry(QtCore.QRect(30, 170, 271, 201))
        self.layoutWidget_15.setObjectName(_fromUtf8("layoutWidget_15"))
        self.plot_container_up_l = QtGui.QVBoxLayout(self.layoutWidget_15)
        self.plot_container_up_l.setObjectName(_fromUtf8("plot_container_up_l"))
        self.action_exit = QtGui.QPushButton(self.centralwidget)
        self.action_exit.setGeometry(QtCore.QRect(510, 790, 681, 81))
        self.action_exit.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: rgba(255,255,255,0); border: none;\n"
"}"))
        self.action_exit.setText(_fromUtf8(""))
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.at_n = QtGui.QLabel(self.centralwidget)
        self.at_n.setGeometry(QtCore.QRect(1255, 401, 111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Forza Medium"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.at_n.setFont(font)
        self.at_n.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\n"
"font: 75 24pt \"Forza Medium\";"))
        self.at_n.setAlignment(QtCore.Qt.AlignCenter)
        self.at_n.setObjectName(_fromUtf8("at_n"))
        self.at_d = QtGui.QLabel(self.centralwidget)
        self.at_d.setGeometry(QtCore.QRect(1255, 470, 111, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Forza Medium"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.at_d.setFont(font)
        self.at_d.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\n"
"font: 75 24pt \"Forza Medium\";"))
        self.at_d.setAlignment(QtCore.Qt.AlignCenter)
        self.at_d.setObjectName(_fromUtf8("at_d"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(300, 170, 651, 401))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.device_container = QtGui.QVBoxLayout(self.layoutWidget)
        self.device_container.setObjectName(_fromUtf8("device_container"))
        self.layoutWidget_18 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_18.setGeometry(QtCore.QRect(30, 370, 271, 201))
        self.layoutWidget_18.setObjectName(_fromUtf8("layoutWidget_18"))
        self.plot_container_btm_l = QtGui.QVBoxLayout(self.layoutWidget_18)
        self.plot_container_btm_l.setObjectName(_fromUtf8("plot_container_btm_l"))
        self.gear_position = QtGui.QLabel(self.centralwidget)
        self.gear_position.setGeometry(QtCore.QRect(1240, 170, 161, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Forza Medium"))
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.gear_position.setFont(font)
        self.gear_position.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.gear_position.setText(_fromUtf8(""))
        self.gear_position.setAlignment(QtCore.Qt.AlignCenter)
        self.gear_position.setObjectName(_fromUtf8("gear_position"))
        self.date = QtGui.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(40, 50, 271, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.date.setFont(font)
        self.date.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.date.setObjectName(_fromUtf8("date"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(310, 600, 631, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Forza Medium"))
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 255);"))
        self.title.setText(_fromUtf8(""))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.layoutWidget_7 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(30, 580, 271, 81))
        self.layoutWidget_7.setObjectName(_fromUtf8("layoutWidget_7"))
        self.output_j11 = QtGui.QVBoxLayout(self.layoutWidget_7)
        self.output_j11.setObjectName(_fromUtf8("output_j11"))
        self.j11_name = QtGui.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.j11_name.setFont(font)
        self.j11_name.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.j11_name.setText(_fromUtf8(""))
        self.j11_name.setAlignment(QtCore.Qt.AlignCenter)
        self.j11_name.setObjectName(_fromUtf8("j11_name"))
        self.output_j11.addWidget(self.j11_name)
        self.j11_data = QtGui.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.j11_data.setFont(font)
        self.j11_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.j11_data.setText(_fromUtf8(""))
        self.j11_data.setAlignment(QtCore.Qt.AlignCenter)
        self.j11_data.setObjectName(_fromUtf8("j11_data"))
        self.output_j11.addWidget(self.j11_data)
        self.layoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(790, 660, 161, 81))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.output_q2 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.output_q2.setObjectName(_fromUtf8("output_q2"))
        self.q2_name = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.q2_name.setFont(font)
        self.q2_name.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.q2_name.setAlignment(QtCore.Qt.AlignCenter)
        self.q2_name.setObjectName(_fromUtf8("q2_name"))
        self.output_q2.addWidget(self.q2_name)
        self.q2_data = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.q2_data.setFont(font)
        self.q2_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.q2_data.setText(_fromUtf8(""))
        self.q2_data.setAlignment(QtCore.Qt.AlignCenter)
        self.q2_data.setObjectName(_fromUtf8("q2_data"))
        self.output_q2.addWidget(self.q2_data)
        self.layoutWidget_6 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(300, 660, 161, 81))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.output_q1 = QtGui.QVBoxLayout(self.layoutWidget_6)
        self.output_q1.setObjectName(_fromUtf8("output_q1"))
        self.q1_name = QtGui.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.q1_name.setFont(font)
        self.q1_name.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.q1_name.setAlignment(QtCore.Qt.AlignCenter)
        self.q1_name.setObjectName(_fromUtf8("q1_name"))
        self.output_q1.addWidget(self.q1_name)
        self.q1_data = QtGui.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.q1_data.setFont(font)
        self.q1_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.q1_data.setText(_fromUtf8(""))
        self.q1_data.setAlignment(QtCore.Qt.AlignCenter)
        self.q1_data.setObjectName(_fromUtf8("q1_data"))
        self.output_q1.addWidget(self.q1_data)
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(460, 660, 161, 81))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.output_x = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.output_x.setObjectName(_fromUtf8("output_x"))
        self.x_name = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.x_name.setFont(font)
        self.x_name.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.x_name.setAlignment(QtCore.Qt.AlignCenter)
        self.x_name.setObjectName(_fromUtf8("x_name"))
        self.output_x.addWidget(self.x_name)
        self.x_data = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.x_data.setFont(font)
        self.x_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.x_data.setText(_fromUtf8(""))
        self.x_data.setAlignment(QtCore.Qt.AlignCenter)
        self.x_data.setObjectName(_fromUtf8("x_data"))
        self.output_x.addWidget(self.x_data)
        self.layoutWidget_8 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_8.setGeometry(QtCore.QRect(30, 660, 271, 81))
        self.layoutWidget_8.setObjectName(_fromUtf8("layoutWidget_8"))
        self.output_j21 = QtGui.QVBoxLayout(self.layoutWidget_8)
        self.output_j21.setObjectName(_fromUtf8("output_j21"))
        self.j21_name = QtGui.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.j21_name.setFont(font)
        self.j21_name.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.j21_name.setText(_fromUtf8(""))
        self.j21_name.setAlignment(QtCore.Qt.AlignCenter)
        self.j21_name.setObjectName(_fromUtf8("j21_name"))
        self.output_j21.addWidget(self.j21_name)
        self.j21_data = QtGui.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.j21_data.setFont(font)
        self.j21_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.j21_data.setText(_fromUtf8(""))
        self.j21_data.setAlignment(QtCore.Qt.AlignCenter)
        self.j21_data.setObjectName(_fromUtf8("j21_data"))
        self.output_j21.addWidget(self.j21_data)
        self.layoutWidget_5 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(1090, 50, 311, 61))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.infobox = QtGui.QVBoxLayout(self.layoutWidget_5)
        self.infobox.setObjectName(_fromUtf8("infobox"))
        self.demo_num = QtGui.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.demo_num.setFont(font)
        self.demo_num.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.demo_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.demo_num.setObjectName(_fromUtf8("demo_num"))
        self.infobox.addWidget(self.demo_num)
        self.group_num = QtGui.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.group_num.setFont(font)
        self.group_num.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.group_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.group_num.setObjectName(_fromUtf8("group_num"))
        self.infobox.addWidget(self.group_num)
        self.layoutWidget_19 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_19.setGeometry(QtCore.QRect(950, 370, 271, 201))
        self.layoutWidget_19.setObjectName(_fromUtf8("layoutWidget_19"))
        self.plot_container_btm_r = QtGui.QVBoxLayout(self.layoutWidget_19)
        self.plot_container_btm_r.setObjectName(_fromUtf8("plot_container_btm_r"))
        self.layoutWidget_10 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_10.setGeometry(QtCore.QRect(950, 660, 271, 81))
        self.layoutWidget_10.setObjectName(_fromUtf8("layoutWidget_10"))
        self.output_j22 = QtGui.QVBoxLayout(self.layoutWidget_10)
        self.output_j22.setObjectName(_fromUtf8("output_j22"))
        self.j22_name = QtGui.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.j22_name.setFont(font)
        self.j22_name.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.j22_name.setText(_fromUtf8(""))
        self.j22_name.setAlignment(QtCore.Qt.AlignCenter)
        self.j22_name.setObjectName(_fromUtf8("j22_name"))
        self.output_j22.addWidget(self.j22_name)
        self.j22_data = QtGui.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.j22_data.setFont(font)
        self.j22_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.j22_data.setText(_fromUtf8(""))
        self.j22_data.setAlignment(QtCore.Qt.AlignCenter)
        self.j22_data.setObjectName(_fromUtf8("j22_data"))
        self.output_j22.addWidget(self.j22_data)
        self.logo_ubc = QtGui.QLabel(self.centralwidget)
        self.logo_ubc.setGeometry(QtCore.QRect(40, 790, 451, 61))
        self.logo_ubc.setText(_fromUtf8(""))
        self.logo_ubc.setPixmap(QtGui.QPixmap(_fromUtf8("resources/1_2016_UBCStandard_Signature_ReverseRGB72.png")))
        self.logo_ubc.setScaledContents(True)
        self.logo_ubc.setObjectName(_fromUtf8("logo_ubc"))
        self.at_r = QtGui.QLabel(self.centralwidget)
        self.at_r.setGeometry(QtCore.QRect(1275, 343, 71, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Forza Medium"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.at_r.setFont(font)
        self.at_r.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\n"
"font: 75 24pt \"Forza Medium\";"))
        self.at_r.setAlignment(QtCore.Qt.AlignCenter)
        self.at_r.setObjectName(_fromUtf8("at_r"))
        self.at_bar_1 = QtGui.QLabel(self.centralwidget)
        self.at_bar_1.setGeometry(QtCore.QRect(1340, 363, 5, 149))
        self.at_bar_1.setStyleSheet(_fromUtf8("background-color: white;"))
        self.at_bar_1.setText(_fromUtf8(""))
        self.at_bar_1.setObjectName(_fromUtf8("at_bar_1"))
        self.layoutWidget_16 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_16.setGeometry(QtCore.QRect(950, 170, 271, 201))
        self.layoutWidget_16.setObjectName(_fromUtf8("layoutWidget_16"))
        self.plot_container_up_r = QtGui.QVBoxLayout(self.layoutWidget_16)
        self.plot_container_up_r.setObjectName(_fromUtf8("plot_container_up_r"))
        self.at_bar_2 = QtGui.QLabel(self.centralwidget)
        self.at_bar_2.setGeometry(QtCore.QRect(1340, 423, 20, 5))
        self.at_bar_2.setStyleSheet(_fromUtf8("background-color: white;"))
        self.at_bar_2.setText(_fromUtf8(""))
        self.at_bar_2.setObjectName(_fromUtf8("at_bar_2"))
        self.layoutWidget_9 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_9.setGeometry(QtCore.QRect(950, 580, 271, 81))
        self.layoutWidget_9.setObjectName(_fromUtf8("layoutWidget_9"))
        self.output_j12 = QtGui.QVBoxLayout(self.layoutWidget_9)
        self.output_j12.setObjectName(_fromUtf8("output_j12"))
        self.j12_name = QtGui.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.j12_name.setFont(font)
        self.j12_name.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.j12_name.setText(_fromUtf8(""))
        self.j12_name.setAlignment(QtCore.Qt.AlignCenter)
        self.j12_name.setObjectName(_fromUtf8("j12_name"))
        self.output_j12.addWidget(self.j12_name)
        self.j12_data = QtGui.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.j12_data.setFont(font)
        self.j12_data.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.j12_data.setText(_fromUtf8(""))
        self.j12_data.setAlignment(QtCore.Qt.AlignCenter)
        self.j12_data.setObjectName(_fromUtf8("j12_data"))
        self.output_j12.addWidget(self.j12_data)
        self.at_p = QtGui.QLabel(self.centralwidget)
        self.at_p.setGeometry(QtCore.QRect(1360, 400, 51, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Forza Medium"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.at_p.setFont(font)
        self.at_p.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\n"
"font: 75 24pt \"Forza Medium\";"))
        self.at_p.setAlignment(QtCore.Qt.AlignCenter)
        self.at_p.setObjectName(_fromUtf8("at_p"))
        self.logo_ece = QtGui.QLabel(self.centralwidget)
        self.logo_ece.setGeometry(QtCore.QRect(1200, 785, 201, 51))
        self.logo_ece.setText(_fromUtf8(""))
        self.logo_ece.setPixmap(QtGui.QPixmap(_fromUtf8("resources/ece_logo_new.png")))
        self.logo_ece.setScaledContents(True)
        self.logo_ece.setObjectName(_fromUtf8("logo_ece"))
        self.at_ev = QtGui.QLabel(self.centralwidget)
        self.at_ev.setGeometry(QtCore.QRect(1220, 401, 71, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Forza Medium"))
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.at_ev.setFont(font)
        self.at_ev.setStyleSheet(_fromUtf8("color: rgba(255, 255, 255, 100);\n"
"font: 75 24pt \"Forza Medium\";"))
        self.at_ev.setAlignment(QtCore.Qt.AlignCenter)
        self.at_ev.setObjectName(_fromUtf8("at_ev"))
        HomePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(_translate("HomePage", "ELEC 391 Final Demo", None))
        self.y_name.setText(_translate("HomePage", "Y", None))
        self.at_n.setText(_translate("HomePage", "N", None))
        self.at_d.setText(_translate("HomePage", "D", None))
        self.date.setText(_translate("HomePage", "March 17, 2017", None))
        self.q2_name.setText(_translate("HomePage", "Q2", None))
        self.q1_name.setText(_translate("HomePage", "Q1", None))
        self.x_name.setText(_translate("HomePage", "X", None))
        self.demo_num.setText(_translate("HomePage", "ELEC 391 Final Project", None))
        self.group_num.setText(_translate("HomePage", "W2016 T2 Team C3", None))
        self.at_r.setText(_translate("HomePage", "R", None))
        self.at_p.setText(_translate("HomePage", "P", None))
        self.at_ev.setText(_translate("HomePage", "EV", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomePage = QtGui.QMainWindow()
    ui = Ui_HomePage()
    ui.setupUi(HomePage)
    HomePage.show()
    sys.exit(app.exec_())

