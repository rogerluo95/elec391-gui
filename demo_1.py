# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8i
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
        HomePage.resize(800, 480)
        HomePage.setMinimumSize(QtCore.QSize(800, 480))
        HomePage.setMaximumSize(QtCore.QSize(800, 480))
        HomePage.setStyleSheet(_fromUtf8("QMainWindow {\n"
"background-color: black;\n"
"}\n"
"\n"
""))
        self.centralwidget = QtGui.QWidget(HomePage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.date = QtGui.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(30, 50, 271, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.date.setFont(font)
        self.date.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.date.setObjectName(_fromUtf8("date"))
        self.logo_ubc = QtGui.QLabel(self.centralwidget)
        self.logo_ubc.setGeometry(QtCore.QRect(30, 400, 423, 57))
        self.logo_ubc.setText(_fromUtf8(""))
        self.logo_ubc.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Roger Luo/Documents/01_Projects/01_elec391/resources/1_2016_UBCStandard_Signature_ReverseRGB72.png")))
        self.logo_ubc.setScaledContents(True)
        self.logo_ubc.setObjectName(_fromUtf8("logo_ubc"))
        self.logo_ece = QtGui.QLabel(self.centralwidget)
        self.logo_ece.setGeometry(QtCore.QRect(570, 340, 231, 151))
        self.logo_ece.setText(_fromUtf8(""))
        self.logo_ece.setPixmap(QtGui.QPixmap(_fromUtf8("C:/Users/Roger Luo/Documents/01_Projects/01_elec391/resources/ot5du1.png")))
        self.logo_ece.setScaledContents(True)
        self.logo_ece.setObjectName(_fromUtf8("logo_ece"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(520, 50, 241, 56))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.demo_num = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.demo_num.setFont(font)
        self.demo_num.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.demo_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.demo_num.setObjectName(_fromUtf8("demo_num"))
        self.verticalLayout.addWidget(self.demo_num)
        self.group_num = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.group_num.setFont(font)
        self.group_num.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);"))
        self.group_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.group_num.setObjectName(_fromUtf8("group_num"))
        self.verticalLayout.addWidget(self.group_num)
        self.layoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(30, 250, 731, 91))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.name_3 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_3.setFont(font)
        self.name_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.name_3.setText(_fromUtf8(""))
        self.name_3.setAlignment(QtCore.Qt.AlignCenter)
        self.name_3.setObjectName(_fromUtf8("name_3"))
        self.verticalLayout_8.addWidget(self.name_3)
        self.data_3 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.data_3.setFont(font)
        self.data_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.data_3.setText(_fromUtf8(""))
        self.data_3.setAlignment(QtCore.Qt.AlignCenter)
        self.data_3.setObjectName(_fromUtf8("data_3"))
        self.verticalLayout_8.addWidget(self.data_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.name_4 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_4.setFont(font)
        self.name_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.name_4.setText(_fromUtf8(""))
        self.name_4.setAlignment(QtCore.Qt.AlignCenter)
        self.name_4.setObjectName(_fromUtf8("name_4"))
        self.verticalLayout_9.addWidget(self.name_4)
        self.data_4 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.data_4.setFont(font)
        self.data_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.data_4.setText(_fromUtf8(""))
        self.data_4.setAlignment(QtCore.Qt.AlignCenter)
        self.data_4.setObjectName(_fromUtf8("data_4"))
        self.verticalLayout_9.addWidget(self.data_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.name_5 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_5.setFont(font)
        self.name_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.name_5.setText(_fromUtf8(""))
        self.name_5.setAlignment(QtCore.Qt.AlignCenter)
        self.name_5.setObjectName(_fromUtf8("name_5"))
        self.verticalLayout_10.addWidget(self.name_5)
        self.data_5 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.data_5.setFont(font)
        self.data_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.data_5.setText(_fromUtf8(""))
        self.data_5.setAlignment(QtCore.Qt.AlignCenter)
        self.data_5.setObjectName(_fromUtf8("data_5"))
        self.verticalLayout_10.addWidget(self.data_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 130, 731, 91))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.name_0 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_0.setFont(font)
        self.name_0.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.name_0.setText(_fromUtf8(""))
        self.name_0.setAlignment(QtCore.Qt.AlignCenter)
        self.name_0.setObjectName(_fromUtf8("name_0"))
        self.verticalLayout_2.addWidget(self.name_0)
        self.data_0 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.data_0.setFont(font)
        self.data_0.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.data_0.setText(_fromUtf8(""))
        self.data_0.setAlignment(QtCore.Qt.AlignCenter)
        self.data_0.setObjectName(_fromUtf8("data_0"))
        self.verticalLayout_2.addWidget(self.data_0)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.name_1 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_1.setFont(font)
        self.name_1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.name_1.setText(_fromUtf8(""))
        self.name_1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_1.setObjectName(_fromUtf8("name_1"))
        self.verticalLayout_3.addWidget(self.name_1)
        self.data_1 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.data_1.setFont(font)
        self.data_1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.data_1.setText(_fromUtf8(""))
        self.data_1.setAlignment(QtCore.Qt.AlignCenter)
        self.data_1.setObjectName(_fromUtf8("data_1"))
        self.verticalLayout_3.addWidget(self.data_1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.name_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.name_2.setFont(font)
        self.name_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
""))
        self.name_2.setText(_fromUtf8(""))
        self.name_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_2.setObjectName(_fromUtf8("name_2"))
        self.verticalLayout_4.addWidget(self.name_2)
        self.data_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.data_2.setFont(font)
        self.data_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255,255,255,60);"))
        self.data_2.setText(_fromUtf8(""))
        self.data_2.setAlignment(QtCore.Qt.AlignCenter)
        self.data_2.setObjectName(_fromUtf8("data_2"))
        self.verticalLayout_4.addWidget(self.data_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.layoutWidget.raise_()
        self.logo_ubc.raise_()
        self.logo_ece.raise_()
        self.date.raise_()
        self.name_0.raise_()
        self.data_0.raise_()
        self.layoutWidget_4.raise_()
        HomePage.setCentralWidget(self.centralwidget)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(_translate("HomePage", "ELEC 391 Demo 1", None))
        self.date.setText(_translate("HomePage", "Janurary 16, 2017", None))
        self.demo_num.setText(_translate("HomePage", "ELEC 391 Demo I", None))
        self.group_num.setText(_translate("HomePage", "W2016 T2 Team C3", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomePage = QtGui.QMainWindow()
    ui = Ui_HomePage()
    ui.setupUi(HomePage)
    HomePage.show()
    sys.exit(app.exec_())