from tkinter import *
import tkinter.filedialog
import time
from array import *
from writeClass import *



global count
count = 0
refresh_rate=100

class Watch:
    def reset(self):
        #This probably shouldn't work?
        #similar conscepts include, start new watch instance,
        #false start, create new start point
        #end the race - covered by stop function
        global count
        count=1
#orginal
    def start(self):
        global count
        if count == 0:
            self.start_time = time.time()
        count=0
        self.start_timer()
#orginal
    def start_timer(self):
        global count
        self.timer()

        #orginal
    def stop(self):
        global count
        count=1

    def timer(self):
        #This is going to go away
        #this timer stores as a string, but should store as a number
        global count
        if(count==0):
            self.time_read = time.time()
            sec = int(self.time_read - self.start_time)
            self.t.set(self.get_time_string(sec))
            #loop the timer
            if(count==0):
                self.root.after(refresh_rate, self.start_timer)

    def split_peloton(self):
        #records a split in seconds from start_time for the peloton onto an list
        #total race time, lap time...
        #also must increment lap counter
        if self.lap_counter > 0:
            self.split_list_peloton.append(self.get_race_time_current()-self.race_time_list_peloton[-1])
        else:
            self.split_list_peloton.append(self.get_race_time_current())
        self.race_time_list_peloton.append(self.get_race_time_current())
        self.lap_counter += 1

    def get_time_string(self, time_number):
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

    def get_time_int(self):
        return(1000)

    def get_race_time_current(self):
        now = time.time()
        then = self.start_time
        return(int(now - then))

    #def get_lap_time(self):
        #needs to handle peloton or break away
        #this lap minus last lap

#orginal
    def split_break(self):
        #records a split of a break onto an array for breaks
        #assigns lap based on lap counter
        pass

    def get_t_time(self):
        #this is designed to be called by main to be passed into the view
        return str(self.t)

    def __init__(self, root):
        self.root=root

        #single variables
        self.time_read = time.time()
        self.start_time = time.time()
        self.lap_counter = 0
        #self.t should represent the string value of the current time at all times
        self.t = StringVar()
        self.t.set("00:00:00")

        #split lists may be changed to tuples?
        self.race_time_list_peloton = []
        self.split_list_peloton = []
        self.split_list_break = []


            #continue
class SwissWatch:
    #This should only pass values, no actual looping in the SwissWatch
    #looping handled by calling class or method
    def bazinga(self):
        self.bazingaCounter = self.bazingaCounter + 1
        return str(self.bazingaCounter)

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
                self.split_list_peloton.append(self.__get_time_int()-self.race_time_list_peloton[-1])
            else:
                #if it is first lap (or not not first lap)
                self.split_list_peloton.append(self.__get_time_int())
            self.race_time_list_peloton.append(self.__get_time_int())
            self.lap_counter += 1


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



    def __init__(self):
        #single variables
        global count
        count = 1
        self.time_read = time.time()
        self.start_time = time.time()
        self.lap_counter = 0
        self.bazingaCounter = 0
        #self.t should represent the string value of the current time at all times
        self.t = ""
        #self.t = string
        self.t = ("00:00:00")
        #split lists may be changed to tuples?
        self.race_time_list_peloton = []
        self.split_list_peloton = []
        self.split_list_break = []
