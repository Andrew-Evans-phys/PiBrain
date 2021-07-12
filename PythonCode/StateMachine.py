

class StateMachine(): #I think the logic tree will be written here
    def __init__(self, outputfile):
        self.outputfile = outputfile

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR