from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
import time
import settings

#SHIFTPI setup
#import shiftpi.shiftpi as shiftpi
#shiftpi.shiftRegisters(4) # if you use 4 shift registers
#shiftpi.digitalWrite(shiftpi.ALL, shiftpi.HIGH)

class Workers(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(int)


    @pyqtSlot()
    def WigWag(self): # A slot takes no params

          while settings.WIGWAG == "ON":
            shiftpi.digitalWrite(10, shiftpi.LOW)
            shiftpi.digitalWrite(11, shiftpi.HIGH)
            time.sleep(1)
            shiftpi.digitalWrite(10, shiftpi.HIGH)
            shiftpi.digitalWrite(11, shiftpi.LOW)
            time.sleep(1)

