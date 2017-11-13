import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import joe
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

flag = 0
tolerance = 10

Val_v1 = 0

Val_v2 = 0

Val_v3 = 0

Val_v4 = 0

Val_v5 = 0

Val_v6 = 0


class MainG(QtGui.QMainWindow, joe.Ui_MainWindow):
    def __init__(self, parent=None):

        super(MainG, self).__init__(parent)
        self.setupUi(self)
        self.threadclass = ThreadClass()
        self.threadclass.start()
        self.Stop()
        self.threadclass.init()
        ser.write('S')
        ser.write('S')
        ser.write('S')

        self.pushButton.clicked.connect(self.Start)
        self.pushButton_2.clicked.connect(self.Stopb)
        self.DOWNcheck.stateChanged.connect(self.Down)

        self.connect(self.threadclass, QtCore.SIGNAL('Val1'), self.update_progress_bar1)
        self.connect(self.threadclass, QtCore.SIGNAL('Val2'), self.update_progress_bar2)
        self.connect(self.threadclass, QtCore.SIGNAL('Val3'), self.update_progress_bar3)
        self.connect(self.threadclass, QtCore.SIGNAL('Val4'), self.update_progress_bar4)
        self.connect(self.threadclass, QtCore.SIGNAL('Val5'), self.update_progress_bar5)
        self.connect(self.threadclass, QtCore.SIGNAL('Val6'), self.update_progress_bar6)

    def Down(self):
        if (self.DOWNcheck.isChecked()):
            ser.write('B')
            ser.write('D')
            ser.write('F')
            ser.write('H')
            ser.write('J')
            ser.write('L')

    def AvantV1(self):
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        ser.write('A')
        ser.write('A')
        ser.write('A')
        ser.write('A')
        ser.write('A')

    def AvantV2(self):
        GPIO.output(25, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
        ser.write('C')
        ser.write('C')
        ser.write('C')
        ser.write('C')
        ser.write('C')

    def AvantV3(self):
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(12, GPIO.LOW)
        ser.write('E')
        ser.write('E')
        ser.write('E')
        ser.write('E')
        ser.write('E')

    def AvantV4(self):
        GPIO.output(16, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        ser.write('G')
        ser.write('G')
        ser.write('G')
        ser.write('G')
        ser.write('G')

    def AvantV5(self):
        GPIO.output(21, GPIO.HIGH)
        GPIO.output(2, GPIO.LOW)
        ser.write('I')
        ser.write('I')
        ser.write('I')
        ser.write('I')
        ser.write('I')

    def AvantV6(self):
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(4, GPIO.LOW)
        ser.write('K')
        ser.write('K')
        ser.write('K')
        ser.write('K')
        ser.write('K')

    def ArriereV1(self):
        GPIO.output(24, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        ser.write('B')
        ser.write('B')
        ser.write('B')
        ser.write('B')
        ser.write('B')

    def ArriereV2(self):
        GPIO.output(25, GPIO.LOW)
        GPIO.output(8, GPIO.HIGH)
        ser.write('D')
        ser.write('D')
        ser.write('D')
        ser.write('D')
        ser.write('D')

    def ArriereV3(self):
        GPIO.output(7, GPIO.LOW)
        GPIO.output(12, GPIO.HIGH)
        ser.write('F')
        ser.write('F')
        ser.write('F')
        ser.write('F')
        ser.write('F')

    def ArriereV4(self):
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        ser.write('H')
        ser.write('H')
        ser.write('H')
        ser.write('H')
        ser.write('H')

    def ArriereV5(self):
        GPIO.output(21, GPIO.LOW)
        GPIO.output(2, GPIO.HIGH)
        ser.write('I')
        ser.write('I')
        ser.write('I')
        ser.write('I')
        ser.write('I')

    def ArriereV6(self):
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.HIGH)
        ser.write('L')
        ser.write('L')
        ser.write('L')
        ser.write('L')
        ser.write('L')

    def StopV1(self):
        GPIO.output(24, GPIO.LOW)
        GPIO.output(23, GPIO.LOW)
        ser.write('M')

    def StopV2(self):
        GPIO.output(25, GPIO.LOW)
        GPIO.output(8, GPIO.LOW)
        ser.write('N')

    def StopV3(self):
        GPIO.output(7, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        ser.write('O')

    def StopV4(self):
        GPIO.output(16, GPIO.LOW)
        GPIO.output(20, GPIO.LOW)
        ser.write('P')

    def StopV5(self):
        GPIO.output(21, GPIO.LOW)
        GPIO.output(2, GPIO.LOW)
        ser.write('Q')

    def StopV6(self):
        GPIO.output(3, GPIO.LOW)
        GPIO.output(4, GPIO.LOW)
        ser.write('R')

    def Start(self):
        if (self.DOWNcheck.isChecked()):
            if (self.checkBox.isChecked()):
                self.ArriereV1()

            if (self.checkBox_2.isChecked()):
                self.ArriereV2()
            if (self.checkBox_3.isChecked()):
                self.ArriereV3()
            if (self.checkBox_4.isChecked()):
                self.ArriereV4()

            if (self.checkBox_5.isChecked()):
                self.ArriereV5()

            if (self.checkBox_6.isChecked()):
                self.ArriereV6()

        if (self.UPcheck.isChecked()):

            if (self.checkBox.isChecked()):
                self.AvantV1()

            if (self.checkBox_2.isChecked()):
                self.AvantV2()

            if (self.checkBox_3.isChecked()):
                self.AvantV3()

            if (self.checkBox_4.isChecked()):
                self.AvantV4()

            if (self.checkBox_5.isChecked()):
                self.AvantV5()

            if (self.checkBox_6.isChecked()):
                self.AvantV6()

    def Stopb(self):

        self.Stop()
        self.Cons.display(0)
        self.dialC.setValue(0)
        self.lcd1.display(0)
        self.pb1.setValue(0)
        self.lcd2.display(0)
        self.pb2.setValue(0)
        self.lcd3.display(0)
        self.pb3.setValue(0)
        self.lcd4.display(0)
        self.pb4.setValue(0)
        self.lcd5.display(0)
        self.pb5.setValue(0)
        self.lcd6.display(0)
        self.pb6.setValue(0)
        ser.write('S')
        ser.write('S')
        ser.write('S')

    def Avant(self):
        self.AvantV1()
        self.AvantV2()
        self.AvantV3()
        self.AvantV4()
        self.AvantV5()
        self.AvantV6()

    def Stop(self):
        self.StopV1()
        self.StopV2()
        self.StopV3()
        self.StopV4()
        self.StopV5()
        self.StopV6()

    def Arriere(self):
        self.ArriereV1()
        self.ArriereV2()
        self.ArriereV3()
        self.ArriereV4()
        self.ArriereV5()
        self.ArriereV6()

    def update_progress_bar1(self, val):
        global Val_v1, Val_v2, Val_v3, Val_v4, Val_v5, Val_v6

        if (self.checkBox.isChecked()):
            Val_v1 = val
            print("V1")
            print(Val_v1)

            if (self.UPcheck.isChecked()):

                cons1 = self.Cons.intValue()
                cons = 6 * cons1
                self.pb1.setMaximum(cons)

                self.lcd1.display(val / 6)

                self.pb1.setValue(val)

                if val > cons:
                    self.ArriereV1()

                if val < cons:
                    if Val_v1 > Val_v2:
                        self.AvantV2()
                        self.StopV1()

                    if Val_v1 > Val_v3:
                        self.AvantV3()

                    if Val_v1 > Val_v4:
                        self.AvantV4()

                    if Val_v1 > Val_v5:
                        self.AvantV5()

                    if Val_v1 > Val_v6:
                        self.AvantV6()



                    else:
                        self.AvantV1()




                else:
                    self.StopV1()
                    self.pb1.setValue(cons)

            if (self.DOWNcheck.isChecked()):

                if Val_v1 < Val_v2:
                    self.ArriereV2()
                    self.StopV1()
                if Val_v1 < Val_v3:
                    self.ArriereV3()
                if Val_v1 < Val_v4:
                    self.ArriereV4()
                if Val_v1 < Val_v5:
                    self.ArriereV5()

                else:

                    if val == 1:
                        self.StopV1()

                    if val <= 1:
                        self.StopV1()

                    else:

                        self.ArriereV1()

                self.lcd1.display(val / 6)

                self.pb1.setValue(val)
                self.Cons.display(0)
                self.dialC.setValue(0)
                if val == 1:
                    self.StopV1()

                if val <= 1:
                    self.StopV1()

    def update_progress_bar2(self, val):
        global Val_v1, Val_v2, Val_v3, Val_v4, Val_v5, Val_v6, tolerance

        if (self.checkBox_2.isChecked()):
            Val_v2 = val
            print("V2")
            print(Val_v2)

            if (self.UPcheck.isChecked()):

                cons1 = self.Cons.intValue()
                cons = 6 * cons1
                self.pb2.setMaximum(cons)

                self.lcd2.display(val / 6)

                self.pb2.setValue(val)

                if val > cons:
                    self.ArriereV2()

                if val < cons:
                    if (Val_v2 > Val_v1):
                        self.StopV2()
                        self.AvantV1()
                    else:

                        self.AvantV2()


                else:
                    self.StopV2()
                    self.pb2.setValue(cons)

            if (self.DOWNcheck.isChecked()):

                if (Val_v2 < Val_v1 - 5):

                    self.StopV2()
                    self.ArriereV1()

                else:

                    if val <= 0:
                        self.StopV2()

                    self.ArriereV2()

                self.lcd2.display(val / 6)

                self.pb2.setValue(val)
                self.Cons.display(0)
                self.dialC.setValue(0)
                if val <= 0:
                    self.StopV2()

    def update_progress_bar3(self, val):
        global Val_v1, Val_v2, Val_v3, Val_v4, Val_v5, Val_v6

        if (self.checkBox_3.isChecked()):
            Val_v3 = val

            print("V3")
            print(Val_v3)

            if (self.UPcheck.isChecked()):

                cons1 = self.Cons.intValue()
                cons = 6 * cons1
                self.pb3.setMaximum(cons)

                self.lcd3.display(val / 6)

                self.pb3.setValue(val)

                if val > cons:
                    self.ArriereV3()

                if val < cons:
                    if (Val_v3 > Val_v1 + 80):
                        self.StopV3()

                    else:

                        self.AvantV3()


                else:
                    self.StopV3()
                    self.pb3.setValue(cons)

            if (self.DOWNcheck.isChecked()):

                if (Val_v3 < Val_v1 - 70):

                    self.StopV3()
                    self.ArriereV1()

                else:

                    if val <= 0:
                        self.StopV3()

                    self.ArriereV3()

                self.lcd3.display(val / 6)

                self.pb3.setValue(val)
                self.Cons.display(0)
                self.dialC.setValue(0)
                if val <= 0:
                    self.StopV3()
                    ser.write('F')
                    ser.write('F')
                    ser.write('F')
                    ser.write('F')
                    ser.write('F')

    def update_progress_bar4(self, val):
        global Val_v1, Val_v2, Val_v3, Val_v4, Val_v5, Val_v6

        if (self.checkBox_4.isChecked()):
            Val_v4 = Val_v2
            val = Val_v2

            if (self.UPcheck.isChecked()):

                cons1 = self.Cons.intValue()
                cons = 6 * cons1
                self.pb4.setMaximum(cons)

                self.lcd4.display(val / 6)

                self.pb4.setValue(val)

                if val > cons:
                    self.ArriereV4()

                if val < cons:
                    if (Val_v4 > Val_v1):

                        self.StopV4()
                    else:

                        self.AvantV4()

                else:
                    self.StopV4()
                    self.pb4.setValue(cons)

            if (self.DOWNcheck.isChecked()):

                if (Val_v4 < Val_v1 - 10):
                    self.StopV4()

                else:
                    self.ArriereV4()

                self.lcd4.display(val / 6)

                self.pb4.setValue(val)
                self.Cons.display(0)
                self.dialC.setValue(0)
                if val <= 0:
                    self.StopV4()

    def update_progress_bar5(self, val):
        global Val_v1, Val_v2, Val_v3, Val_v4, Val_v5, Val_v6

        if (self.checkBox_5.isChecked()):
            Val_v5 = Val_v4
            val = Val_v4

            if (self.UPcheck.isChecked()):

                cons1 = self.Cons.intValue()

                cons = 6 * cons1
                self.pb5.setMaximum(cons)

                self.lcd5.display(val / 6)

                self.pb5.setValue(val)

                if val > cons:
                    self.ArriereV5()

                if val < cons:
                    if (Val_v5 > Val_v1):

                        self.StopV5()
                    else:

                        self.AvantV5()

                else:
                    self.StopV5()
                    self.pb5.setValue(cons)

            if (self.DOWNcheck.isChecked()):

                if (Val_v5 < Val_v1 - 10):
                    self.StopV5()

                else:
                    self.ArriereV5()

                self.lcd5.display(val / 6)

                self.pb5.setValue(val)
                self.Cons.display(0)
                self.dialC.setValue(0)
                if val <= 0:
                    self.StopV5()

    def update_progress_bar6(self, val):
        global Val_v1, Val_v2, Val_v3, Val_v4, Val_v5, Val_v6

        if (self.checkBox_6.isChecked()):
            Val_v6 = Val_v4
            val = Val_v4

            if (self.UPcheck.isChecked()):

                cons1 = self.Cons.intValue()
                cons = 6 * cons1
                self.pb6.setMaximum(cons)

                self.lcd6.display(val / 6)

                self.pb6.setValue(val)

                if val > cons:
                    self.ArriereV6()

                if val < cons:

                    if (Val_v6 > Val_v1):

                        self.StopV6()
                    else:

                        self.AvantV6()

                else:
                    self.StopV6()
                    self.pb6.setValue(cons)

            if (self.DOWNcheck.isChecked()):
                if (Val_v6 < Val_v1 - 10):
                    self.StopV6()

                else:
                    self.ArriereV6()

                

                self.lcd6.display(val)

                self.pb6.setValue(val)
                self.Cons.display(0)
                self.dialC.setValue(0)
                if val <= 0:
                    self.StopV6()


class ThreadClass(QtCore.QThread):
    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def init(self):

        self.emit(QtCore.SIGNAL('Val1'), 0)
        self.emit(QtCore.SIGNAL('Val2'), 0)
        self.emit(QtCore.SIGNAL('Val3'), 0)
        self.emit(QtCore.SIGNAL('Val4'), 0)
        self.emit(QtCore.SIGNAL('Val5'), 0)
        self.emit(QtCore.SIGNAL('Val6'), 0)

    def run(self):

        while 1:

            read = int(float(ser.readline()))

            if read < 1000 and read > 0:
                self.emit(QtCore.SIGNAL('Val1'), read)

            if read < 2000 and read >= 1000:
                read = read - 1000
                self.emit(QtCore.SIGNAL('Val2'), read)

            if read < 3000 and read >= 2000:
                read = read - 2000

                self.emit(QtCore.SIGNAL('Val3'), read)

            if read < 4000 and read >= 3000:
                read = read - 3000
                self.emit(QtCore.SIGNAL('Val4'), read)

            if read < 5000 and read >= 4000:
                read = read - 4000
                self.emit(QtCore.SIGNAL('Val5'), read)

            if read < 6000 and read >= 5000:
                read = read - 5000
                self.emit(QtCore.SIGNAL('Val6'), read)


a = QtGui.QApplication(sys.argv)

app = MainG()
app.show()

a.exec_()
