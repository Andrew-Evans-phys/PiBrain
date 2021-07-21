import time
import datetime

class StateMachine(): #I think the logic tree will be written here
    def __init__(self, outputfile, inputfile):
        self.outputfile = outputfile
        self.inputfile = inputfile
        self.task = []
    
    def write_to_log(self,job_stat):
        with open(self.outputfile, 'a') as outFile:
            #try:
            if(job_stat[0]):
                if(job_stat[1]):
                    outFile.write(str(datetime.datetime.now()) +" "+job_stat[2]+ " completed, returning to queue"+"\n")#add time stamp here
                else:
                    outFile.write(str(datetime.datetime.now()) +" "+job_stat[2]+ " didn't complete, conditions not met, returning to queue"+"\n")
            else:
                if(job_stat[2]=="Shutdown"):
                    outFile.write(str(datetime.datetime.now())+ " Shutting system down"+"\n")
                else:
                    outFile.write(str(datetime.datetime.now()) +" "+job_stat[2]+ " task failure, shutting system down"+"\n")

    def idleTaskCheck(self, newTask, oldTask):
        newTaskCheck =  newTask()
        if(oldTask != newTaskCheck):
            oldTask = newTaskCheck
            self.write_to_log(oldTask)
        return oldTask

    def idle_state(self, task1, task2, task3, task4, task5, task6, task7, update_pins):
        #Sets machine step wait time
        delay = 1 
        #initializes tasks
        task1_last = (False, False, "Default")
        task2_last = (False, False, "Default")
        task3_last = (False, False, "Default")
        task4_last = (False, False, "Default")
        task5_last = (False, False, "Default")
        task6_last = (False, False, "Default")
        task7_last = (False, False, "Default")
        #Idle loop
        machine_on = True
        while(machine_on):
            #update the pin information
            shutoff_code = update_pins("/Users/gk/Documents/PiBrain/PythonCode/Pin_Settings.txt")
            if(not shutoff_code):
                #Machine logic based on updated pins 
                task1_last = self.idleTaskCheck(task1, task1_last) #manual_start
                time.sleep(delay)
                task2_last = self.idleTaskCheck(task2, task2_last) #mechanical_pump_start
                time.sleep(delay)
                task3_last = self.idleTaskCheck(task3, task3_last) #roughing_system
                time.sleep(delay)
                task4_last = self.idleTaskCheck(task4, task4_last) #cryo_rough
                time.sleep(delay)
                task5_last = self.idleTaskCheck(task5, task5_last) #open_sys_to_cryo_pump
                time.sleep(delay)
                task6_last = self.idleTaskCheck(task6, task6_last) #start_water_lock
                time.sleep(delay)
                task7_last = self.idleTaskCheck(task7, task7_last) #start vent
                time.sleep(delay)
                #Checking to make sure no task has thrown a shutdown code
                if(not task1_last[0] or not task2_last[0] or not task3_last[0] or not task4_last[0] or not task5_last[0] or not task6_last[0] or not task7_last[0]): 
                    print("Unexpected error, exiting idle")
                    machine_on = False
            else:
                print("Stop code called")
                machine_on = False



