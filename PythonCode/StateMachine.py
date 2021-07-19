
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



    def setTask(self):
        with open(self.inputfile, 'r') as inFile:
            for line in inFile:
                try:
                    self.task.append(int(line[:-1]))
                except(ValueError):
                    pass

    def idleTaskCheck(self, newTask, oldTask):
        if(oldTask != newTask()):
            oldTask = newTask()
            self.write_to_log(oldTask)
        return oldTask

    def idle_state(self, task1, task2, task3, task4, task5, task6):
        #self.write_to_log()
        delay = 1
        self.setTask()
        i = 0
        read_condition =  True
        task1_last = (False, False, "Default")
        task2_last = (False, False, "Default")
        task3_last = (False, False, "Default")
        task4_last = (False, False, "Default")
        task5_last = (False, False, "Default")
        task6_last = (False, False, "Default")
        while(read_condition):
            task1_old = self.idleTaskCheck(task1, task1_last)
            time.sleep(delay)
            task2_old = self.idleTaskCheck(task2, task2_last)
            time.sleep(delay)
            task3_old = self.idleTaskCheck(task3, task3_last)
            time.sleep(delay)
            task4_old = self.idleTaskCheck(task4, task4_last)
            time.sleep(delay)
            task5_old = self.idleTaskCheck(task5, task5_last)
            time.sleep(delay)
            task6_old = self.idleTaskCheck(task6, task6_last)
            time.sleep(delay)
            if(bool(self.task[i%len(self.task)])):
                print("Exting idle")
                read_condition = False
            else:
                print("Looping idle")
            time.sleep(delay)
            i += 1
            if(len(self.task)%i == 0):
                self.setTask()

#system = StateMachine("misc", "/Users/gk/Documents/PiBrain/PythonCode/tasklist.txt")