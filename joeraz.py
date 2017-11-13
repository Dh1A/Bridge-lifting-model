# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Dhia\Desktop\Dev\joe3raz.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 480)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 101, 81))
        self.pushButton.setStyleSheet(_fromUtf8(""))
        self.pushButton.setText(_fromUtf8(""))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 80, 101, 81))
        self.pushButton_2.setStyleSheet(_fromUtf8(""))
        self.pushButton_2.setText(_fromUtf8(""))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(40, 285, 16, 17))
        self.checkBox.setText(_fromUtf8(""))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(300, 285, 16, 17))
        self.checkBox_2.setText(_fromUtf8(""))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(570, 285, 16, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setText(_fromUtf8(""))
        self.checkBox_3.setIconSize(QtCore.QSize(30, 30))
        self.checkBox_3.setShortcut(_fromUtf8(""))
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setAutoRepeat(False)
        self.checkBox_3.setTristate(False)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 420, 16, 17))
        self.checkBox_4.setText(_fromUtf8(""))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(300, 420, 16, 17))
        self.checkBox_5.setText(_fromUtf8(""))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(570, 420, 16, 17))
        self.checkBox_6.setText(_fromUtf8(""))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("GUIrAz.jpg")))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName(_fromUtf8("label"))
        self.UPcheck = QtGui.QCheckBox(self.centralwidget)
        self.UPcheck.setGeometry(QtCore.QRect(541, 43, 16, 21))
        self.UPcheck.setAutoFillBackground(False)
        self.UPcheck.setStyleSheet(_fromUtf8(""))
        self.UPcheck.setText(_fromUtf8(""))
        self.UPcheck.setTristate(False)
        self.UPcheck.setObjectName(_fromUtf8("UPcheck"))
        self.buttonGroup = QtGui.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.UPcheck)
        self.DOWNcheck = QtGui.QCheckBox(self.centralwidget)
        self.DOWNcheck.setGeometry(QtCore.QRect(541, 106, 16, 21))
        self.DOWNcheck.setAutoFillBackground(False)
        self.DOWNcheck.setStyleSheet(_fromUtf8(""))
        self.DOWNcheck.setText(_fromUtf8(""))
        self.DOWNcheck.setTristate(False)
        self.DOWNcheck.setObjectName(_fromUtf8("DOWNcheck"))
        self.buttonGroup.addButton(self.DOWNcheck)
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.UPcheck.raise_()
        self.DOWNcheck.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

