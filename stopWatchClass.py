from tkinter import *
import tkinter.filedialog
import time
from array import *
from writeClass import *



global count
#count is a yes/no on counter on
count = 0
refresh_rate=100


class SwissWatch:
    #This should only pass values, no actual looping in the SwissWatch
    #looping handled by calling class or method
    def start(self):
        global count
        if count == 1:
            self.start_time = time.time()
        count=0
        self.get_running_time()

    def stop(self):
        pass

    def split_peloton(self):
        #records a split in seconds from start_time for the peloton onto an list
        #total race time, lap time...
        #also must increment lap counte
        if count == 0:
        #if running
            if self.lap_counter > 0:
                #if not first lap (position 0)
                # self.split_list_peloton.append(self.__get_time_int()-self.race_time_list_peloton[-1])
                self.lap_datas[self.lap_counter].button_peloton()
            else:
                pass
                #if it is first lap (or not not first lap)
            #     self.split_list_peloton.append(self.__get_time_int())
            # self.race_time_list_peloton.append(self.__get_time_int())
            #increment lap and lap list
            self.lap_counter += 1
            self.lap_datas.append(self.lap_counter,previouslap,starttime)


    def split_break(self):
        #TODO
        if self.lap_counter > 0:
            self.split_list_break.append(self.__get_time_int()-self.race_time_list_peloton[-1])
        else:
            self.split_list_break.append(self.__get_time_int())

    # Non-Action function
    def get_running_time(self):
        global count
        if(count==0):
            self.time_read = time.time()
            sec = int(self.time_read - self.start_time)
            self.t = self.__get_time_string(sec)
            return self.t
        else:
            return self.t


    # Local functions
    def __get_time_string(self, time_number):
        time_string = str(time_number)
        h = int(time_number)//3600
        time_number = time_number % 3600
        m = int(time_number)//60
        time_number = time_number % 60
        s = int(time_number)
        #convert to string
        if(h<10):
            h = str(0) + str(h)
        else:
            h= str(h)
        if(m<10):
            m = str(0) + str(m)
        else:
            m = str(m)
        if(s<10):
            s=str(0) +str(s)
        else:
            s=str(s)
        #self.d= h + ":" + m + ":" + s
        return str(h) + ":" + str(m) + ":" + str(s)

    def __get_time_int(self):
        global count
        if(count==0):
            self.time_read = time.time()
            sec = int(self.time_read - self.start_time)
            return sec
        else:
            return None

    @property
    def race_time_list_peloton(self, lap_lap):

        this = self.lap_datas[0]
        print(this.time_peloton)
        return 10

    @property
    def split_list_peloton(self, lappy_lap):
        return self.lap_datas[lappy_lap].split_peloton



    def __init__(self):
        #single variables
        global count
        count = 1
        self.time_read = time.time()
        self.start_time = time.time()
        self.lap_counter = 0
        #self.t should represent the string value of the current time at all times
        self.t = ""
        #self.t = string
        self.t = ("00:00:00")
        #split lists may be changed to tuples?
        # self.race_time_list_peloton = []
        # self.split_list_peloton = []
        # self.split_list_break = []

        # self.lap_datas = [LapData(0,0,self.start_time), LapData(1,0,self.start_time)]
        this = LapData(0,0,self.start_time)
        self.lap_datas = [this]
        # print(help(self.lap_datas))

class LapData:

    # @classproperty
    # cls.current_lap = 0


    # @property
    # def time_peloton(self):
    #     if self.time_peloton != 0:
    #         return str(self.time_peloton)
    #     else:
    #         return "Nope"
    # # def get_int_time_peloton(self):
    # #     #this function should only be called when a number is needed
    # #     return self.time_peloton
    #
    # @time_peloton.setter
    # def time_peloton(self,itime):
    #     #This function should be called by peloton split button
    #     self.time_peloton = time.time() - self.start_time
    #     # self.__set_split_peloton()
    #
    # @property
    # def split_peloton(self):
    #     return self.split_peloton
    #
    # @split_peloton.setter
    # def split_peloton(self):
    #     self.split_peloton = self.time_peloton - self.time_previous_lap
    def button_peloton(self):
        #this should record the peloton race time, split time, create a new lap or increment
        if True:
            #Todo, if time_peloton isn't already set
            self.time_peloton = time.time()



    def __init__(self, lap_lap, previousLapTime, start):
        print("starting thingy")
        self.start_time = int(start)
        self.lap_number = int(lap_lap)
        self.time_previous_lap = int(previousLapTime)
        #lap length in meters, but don't refer to this directly. Use a function so meters can be ditched
        self.lap_length = 1600

        #as strings to be updated to cool stuff
        #elapsed time for the lap is: time_peloton
        self.time_peloton = 0 #the time is the race time of the peloton
        self.times_break = [0]
        self.split_peloton = "None" # the split is the difference in lap times
        self.splits_break = ["None"]
        self.speed_peloton = "None"
        self.speeds_break = ["None"]
        self.break_lead_out = ["None"]
        # self.split_peloton = "None"
