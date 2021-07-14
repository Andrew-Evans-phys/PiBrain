
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
                    if(job_stat[2] == "ID CHECK"):
                        outFile.write("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n") #this will need to be change to show status
                    else:
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
        
    def idle_state(self, task1, task2, task3, task4, task5, task6):
        #self.write_to_log()
        delay = 1
        self.setTask()
        i = 0
        read_condition =  True
        while(read_condition):
            job_stat =  task1()
            self.write_to_log(job_stat)
            time.sleep(delay)
            job_stat =  task2()
            self.write_to_log(job_stat)
            time.sleep(delay)
            job_stat =  task3()
            self.write_to_log(job_stat)
            time.sleep(delay)
            job_stat =  task4()
            self.write_to_log(job_stat)
            time.sleep(delay)
            job_stat =  task5()
            self.write_to_log(job_stat)
            time.sleep(delay)
            job_stat =  task6()
            self.write_to_log(job_stat)
            time.sleep(delay)
            self.write_to_log((True, True, "ID CHECK"))
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