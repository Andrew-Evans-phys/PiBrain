###########################################################
# This code is acting as the replacement to the  original
# c/c++ script after it was discovered that the lib was
# no longer supported
#
#This code is for use on raspbian
#
#Contact:  evansa@sonoma.edu
###########################################################

import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM) #setting the pin layout style  to be BC

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

class IO_Device:
    def __init__(self, name, IO_type, state, pin, ras_pin):
        self.name = name  #name of action
        self.state = state #High or low
        self.pin = pin #pin #
        self.ras_pin = ras_pin
        if(IO_type == "input"):
            GPIO.setup(ras_pin, GPIO.IN)
        else:
            GPIO.setup(ras_pin, GPIO.OUT)        

    def setHigh(self):
        #will set the specific pin high
        print("Setting", self.name,"high...")
        self.state  = True
        GPIO.output(self.ras_pin, GPIO.HIGH)
        print(bcolors.OK+"Done"+bcolors.RESET)

    def setLow(self):
        #will set the specific pin low
        print("Setting", self.name,"low...")
        self.state  = False
        GPIO.output(self.ras_pin, GPIO.LOW)
        print(bcolors.OK+"Done"+bcolors.RESET)


#system functions 
def manual_start():
    print("Starting manual mode...")
    if(Start.state or On_Reset.state):
        OUT1.setHigh()
        return True
    else:
        print(bcolors.FAIL+"ERROR"+bcolors.RESET, "failed to start manually, exiting startup")
        return False


def shutdownSys():
    print("Shutting down...")
    Start.setLow()
    Stop.setLow()
    Crossover.setLow()
    Auto.setLow()
    On_Reset.setLow()
    Manual.setLow()
    Vent.setLow()
    Rough_S2.setLow()
    HI_VAC_Valve.setLow()
    Cryo_Rough.setLow()
    Cryo_Purge.setLow()
    Vacuum_In.setLow()
    Rough_SW.setLow()
    Water_Lock.setLow()
    Vent_Auto.setLow()
    OUT1.setLow()
    OUT2.setLow()
    OUT3.setLow()
    OUT4.setLow()
    OUT5.setLow()
    OUT6.setLow()
    OUT7.setLow()
    OUT8.setLow()
    OUT9.setLow()
    print("Shutdown complete")


#initialization of the pins 

#inputs
Start = IO_Device("Start", "input", False, "0000",26)
Stop = IO_Device("Stop", "input", False, "0001",19)
Crossover = IO_Device("Crossover", "input", False, "0002",13)
Auto = IO_Device("Auto", "input", False, "0003",6)
On_Reset = IO_Device("On_Reset", "input", False, "0004",5) 
Manual = IO_Device("Manual", "input", False, "0005",0)
Vent = IO_Device("Vent", "input", False, "0006",11)
Rough_S2 = IO_Device("Rough_S2", "input", False, "0007",9)
HI_VAC_Valve = IO_Device("HI_VAC_Valve", "input", False, "0008",10)
Cryo_Rough = IO_Device("Cryo_Rough", "input", False, "0009",22)
Cryo_Purge = IO_Device("Cryo_Purge", "input", False, "0010",27)
Vacuum_In = IO_Device("Vacuum_In", "input", False,"0011",17)
Rough_SW = IO_Device("Rough_SW", "input", False, "0012",4)
Water_Lock = IO_Device("Water_Lock", "input", False, "0013",3) 
Vent_Auto = IO_Device("Vent_Auto", "input", False, "0014",2)

#outputs (the raspiout will be changed later!)
OUT1 = IO_Device("OUT1", "output", False, "0501",15)
OUT2 = IO_Device("OUT2", "output", False, "0502",18)
OUT3 = IO_Device("OUT3", "output", False, "0503",23)
OUT4 = IO_Device("OUT4", "output", False, "0504",24)
OUT5 = IO_Device("OUT5", "output", False, "0505",25)
OUT6 = IO_Device("OUT6", "output", False, "0506",8)
OUT7 = IO_Device("OUT7", "output", False, "0507",7)
OUT8 = IO_Device("OUT8", "output", False, "0508",1)
OUT9 = IO_Device("OUT9", "output", False, "0509",12)
print("Initializtion complete!")

    
#Below this is where the  actual logic will go!
manual_start()
time.sleep(5)
print("TESTING: setting OUT1  high!")
OUT1.setHigh()
input(bcolors.OK+"Press any key to set OUT1 low"+bcolors.RESET)
OUT1.setLow
input(bcolors.OK+"Complete"+bcolors.RESET,"begining shutdown")
shutdownSys()


