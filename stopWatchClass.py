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
        print(type(str(self.t)))
        print(str(self.t))
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
