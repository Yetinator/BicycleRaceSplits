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
            if LapData.current_lap > 0:
                #if not first lap (position 0)
                # self.split_list_peloton.append(self.__get_time_int()-self.race_time_list_peloton[-1])
                self.lap_datas[LapData.current_lap-1].button_peloton()
            else:
                print("split_peloton - shouldn't be here")

            self.lap_datas.append(LapData())

    def split_break(self):
        #TODO
        if LapData.current_lap > 0:
            pass
            # self.split_list_break.append(self.__get_time_int()-self.race_time_list_peloton[-1])

        else:
            pass
            # self.split_list_break.append(self.__get_time_int())

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

    # def get_lap_data(self):
    #     lap = LapData.current_lap
    #     return get_lap_data(lap)

    def get_lap_data(self, lap = None):
        if lap == None:
            lap = LapData.current_lap
            print("Getting lap data current lap?")
        #This feeds a row of data to the frontend
        #some of requested laps will be beyond the list
        # return ["Lap " + str(lap_lap + 1), str(pelotonTime), str(pelotonSplit), str(breakSplit), "hey"]
        if lap < LapData.current_lap:
            return ["Lap " + str(lap + 1), str(LapData.time_peloton[lap]), str("there"), str("what"), "hey"]
        else:
            return ["Lap " + str(lap + 1), str("or else"), str("there"), str("what"), "hey"]

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

    @property
    def current_lap(self):
        return LapData.current_lap

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

    def test_button(self):
        print("Stopwatchclass test function:::")
        print(self.t)
        print(self.lap_datas[0].time_peloton)
        for i in self.lap_datas:
            print(i.lap_number)

    def __init__(self):
        #single variables
        global count
        count = 1
        self.time_read = time.time()
        self.start_time = time.time()

        #lap_counter becomes LapData.current_lap?
        # LapData.current_lap = 0
        #self.t should represent the string value of the current time at all times
        self.t = ""
        #self.t = string
        self.t = ("00:00:00")
        self.lap_datas = [LapData(self.start_time)]
        #split lists may be changed to tuples?
        # self.race_time_list_peloton = []
        # self.split_list_peloton = []
        # self.split_list_break = []

        # self.lap_datas = [LapData(0,0,self.start_time), LapData(1,0,self.start_time)]
        # this = LapData(0,0,self.start_time)
        # self.lap_datas = [this]
        # print(help(self.lap_datas))

class LapData:

    # @classproperty
    #accessed LapData.current_lap
    current_lap = 0
    #lap length in meters, but don't refer to this directly. Use a function so meters can be ditched
    lap_length = 1600
    time_peloton = []
    start_time = 0

    def button_peloton(self):
        #this should record the peloton race time, split time, create a new lap or increment
        if True:
            #Todo, if time_peloton isn't already set
            print(str(time.time()-LapData.start_time)+" is the running time?")
            LapData.time_peloton[LapData.current_lap - 1] = time.time()-LapData.start_time

    # @classmethod
    # def laps_init(cls ,start):
    #     #This should behave as an alternate constructer
    #     LapData.start_time = int(start)
    #     cls.__init__()

    def __init__(self, start=None):
        #todo - make certain things a class variable.  LapData.Time_peloton[]
        #gives better access to all of that than having a single instance listed under
        #a particular lap
        #other Class Variables lap_length, current lap, start_time
        if start is not None:
            if LapData.start_time == 0:
                LapData.start_time = start
        elif  LapData.start_time == 0:
            LapData.start_time = time.time()
        # print("starting thingy")
        # print("start time is " + str(LapData.start_time))
        self.lap_number = int(LapData.current_lap)
        print("current_lap = " + str(LapData.current_lap))

        #in the constructor, previous lap is always the last lap created
        # if LapData.current_lap > 1:
        #     self.time_previous_lap = LapData.time_peloton[self.lap_number - 1]


        #as strings to be updated to cool stuff
        #elapsed time for the lap is: time_peloton
        # self.time_peloton = 0 #the time is the race time of the peloton
        LapData.time_peloton.append("Inti append " + str(LapData.current_lap))
        # LapData.time_peloton.append("None2")
        self.times_break = [0]
        self.split_peloton = "None" # the split is the difference in lap times
        self.splits_break = ["None"]
        self.speed_peloton = "None"
        self.speeds_break = ["None"]
        self.break_lead_out = ["None"]
        # self.split_peloton = "None"
        LapData.current_lap = LapData.current_lap + 1
