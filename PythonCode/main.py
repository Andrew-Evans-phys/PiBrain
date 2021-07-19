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
import datetime
import StateMachine
import os

#import RPi.GPIO as GPIO uncomment for use


#GPIO.setmode(GPIO.BCM) #setting the pin layout style  to be BC #uncomment for use

#Terminal cleared
os.system("cls")

#state machine is created
start_time = datetime.datetime.now()
system = StateMachine.StateMachine("/Users/gk/Documents/PiBrain/PythonCode/outputfile"+str(start_time).translate(str.maketrans({" ":"_"}))+".txt", "/Users/gk/Documents/PiBrain/PythonCode/tasklist.txt")

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
        self.IO_type =  IO_type
        if(IO_type == "input"):
            #GPIO.setup(ras_pin, GPIO.IN) #uncomment for use
            print("")
        else:
            print("")
            #GPIO.setup(ras_pin, GPIO.OUT)  #  
            # print("")    

    def setHigh(self):
        #will set the specific pin high
        if(self.state):
            print(self.name,"maintaining high")
        else:
            print("Setting", self.name,"high...",bcolors.OK+"Done"+bcolors.RESET)
            self.state  = True
            #GPIO.output(self.ras_pin, GPIO.HIGH) #uncomment for use

    def setLow(self):
        #will set the specific pin low
        if(self.IO_type == "output"):
            if(self.state):
                print("Setting", self.name,"low...",bcolors.OK+"Done"+bcolors.RESET)
                self.state  = False
                #GPIO.output(self.ras_pin, GPIO.LOW) #uncomment for use
            else:
                print(self.name,"maintaining low")
        else:
            print(bcolors.WARNING+"Warning"+bcolors.RESET, self.name, "is not a output pin and should not be set")

#system functions 
def manual_start():
    print("Starting manual mode...")
    if(Start.state or On_Reset.state): #Checking to ssee if these are set high, will need to def read GPIO before this
        OUT1.setHigh()
        return (True, True, "Manual mode")
    else:
        print(bcolors.FAIL+"ERROR"+bcolors.RESET, "failed to start manually, exiting startup"+"\n")
        return (True, False, "Manual mode")   

 #starting mechanical pump
def mechanical_pump_start():
    print("Starting mechanical pump...")
    if(OUT1.state and Rough_SW.state):
        OUT9.setHigh();
        return (True, True, "Mechanical pump")
    else:
        print(bcolors.FAIL+"ERROR"+bcolors.RESET, "failed to start mechanical pump, exiting startup"+"\n")
        return (True, False, "Mechanical pump")
    
def roughing_system():
    print("Roughing the system...")
    if(OUT9.state and not HI_VAC_Valve.state and not Vent.state and Rough_S2.state and not Cryo_Rough.state and not Cryo_Purge.state):
        OUT3.setHigh()
        return (True, True, "Roughing system")
    else:
        print(bcolors.FAIL+"ERROR"+bcolors.RESET, "failed to rough system, exiting startup"+"\n")
        return  (True, False, "Roughing system")

def cryo_rough():
    print("Roughing cryo-system...")
    if(OUT9.state and not HI_VAC_Valve.state and not Rough_S2.state and not Vent.state and Cryo_Rough.state):
        OUT5.setHigh()
        return (True, True, "Roughing cryo-system")
    else:
        print(bcolors.FAIL+"ERROR"+bcolors.RESET, "failed to cryo-rough system, exiting startup"+"\n")
        return (True, False, "Roughing cryo-system")

def open_sys_to_cryo_pump():
    print("Opening system to cryo-pump...")
    if(Crossover.state and Vacuum_In.state and not Rough_S2.state and not Vent.state and HI_VAC_Valve.state):
        OUT7.setHigh()
        return (True, True, "Opening system to cryo-pump")
    else:
        print(bcolors.FAIL+"ERROR"+bcolors.RESET, "failed to open system to cryo-pump, exiting startup"+"\n")
        return (True, False, "Opening system to cryo-pump")

def start_water_lock():
    print("Starting water lock...")
    if((Vacuum_In.state or OUT7.state) and not Vent.state and Water_Lock.state):
        OUT8.setHigh()
        return (True, True, "Water lock")
    else:
        print(bcolors.FAIL+"ERROR"+bcolors.RESET, "failed to open water lock, exiting startup"+"\n")
        return (True, False, "Water lock")
        

def readPins():
    print(bcolors.OK+"Reading "+Start.name+" with GPIO"+bcolors.RESET) #read Start
    print(bcolors.OK+"Reading "+Stop.name+" with GPIO"+bcolors.RESET) #read Stop
    print(bcolors.OK+"Reading "+Crossover.name+" with GPIO"+bcolors.RESET) #read Crossover
    print(bcolors.OK+"Reading "+Auto.name+" with GPIO"+bcolors.RESET) #read Auto
    print(bcolors.OK+"Reading "+On_Reset.name+" with GPIO"+bcolors.RESET) #read On/Reset
    print(bcolors.OK+"Reading "+Manual.name+" with GPIO"+bcolors.RESET)  #read Manual
    print(bcolors.OK+"Reading "+Vent.name+" with GPIO"+bcolors.RESET) #read Vent
    print(bcolors.OK+"Reading "+Rough_S2.name+" with GPIO"+bcolors.RESET) #read Rough_S2
    print(bcolors.OK+"Reading "+HI_VAC_Valve.name+" with GPIO"+bcolors.RESET) #read High Vacuum Valve
    print(bcolors.OK+"Reading "+Cryo_Rough.name+" with GPIO"+bcolors.RESET) #read Cryo Rough
    print(bcolors.OK+"Reading "+Cryo_Purge.name+" with GPIO"+bcolors.RESET) #read Cryo Purge
    print(bcolors.OK+"Reading "+Vacuum_In.name+" with GPIO"+bcolors.RESET) #read Vacuum In
    print(bcolors.OK+"Reading "+Rough_SW.name+" with GPIO"+bcolors.RESET) #read Rough_SW
    print(bcolors.OK+"Reading "+Water_Lock.name+" with GPIO"+bcolors.RESET) #read Water Lock


#System shutdown code, always run upon exiting the code
def shutdownSys():
    print("Shutting down...")
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
    system.write_to_log((False, False, "Shutdown"))
    return True

#prints the status of the system, only used when debugging
def system_status():
    print(Start.name, Start.state)
    print(Stop.name, Stop.state)
    print(Crossover.name, Crossover.state) 
    print(Auto.name, Auto.state) 
    print(On_Reset.name, On_Reset.state) 
    print(Manual.name, Manual.state) 
    print(Vent.name, Vent.state) 
    print(Rough_S2.name, Rough_S2.state)
    print(HI_VAC_Valve.name, HI_VAC_Valve.state)
    print(Cryo_Rough.name, Cryo_Rough.state)
    print(Cryo_Purge.name, Cryo_Purge.state)
    print(Vacuum_In.name, Vacuum_In.state)
    print(Rough_SW.name, Rough_SW.state)
    print(Water_Lock.name, Water_Lock.state) 
    print(OUT1.name, OUT1.state) 
    print(OUT2.name, OUT2.state) 
    print(OUT3.name, OUT3.state)
    print(OUT4.name, OUT4.state) 
    print(OUT5.name, OUT5.state) 
    print(OUT6.name, OUT6.state)
    print(OUT7.name, OUT7.state)
    print(OUT8.name, OUT8.state)
    print(OUT9.name, OUT9.state) 


#initialization of the pins 
#inputs
Start = IO_Device("Start", "input", True, "0000",26)#testing should be set to false by  default
Stop = IO_Device("Stop", "input", False, "0001",19)
Crossover = IO_Device("Crossover", "input", False, "0002",13)
Auto = IO_Device("Auto", "input", False, "0003",6)
On_Reset = IO_Device("On_Reset", "input", True, "0004",5) #testing should be set to false by  default
Manual = IO_Device("Manual", "input", True, "0005",0)#testing should be set to false by  default
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
system.write_to_log((True, True, "System init"))

#Below this is where the  actual logic will go!
system.idle_state(manual_start, mechanical_pump_start, roughing_system, cryo_rough, open_sys_to_cryo_pump, start_water_lock, readPins)
shutdownSys()


