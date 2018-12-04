#/usr/bin/python3 menu01.py
#came from menu01
#Main from BicycleRaceSplits

from tkinter import *
import tkinter.filedialog
import time
from array import *
from writeClass import *
#from filedialog   import askopenfilename
#class Stopwatch
#https://www.youtube.com/watch?v=pPvmC0Srdeo
configFile = ReadFile("configGeneral.txt")
# global configGeneral
# configGeneral = configFile.getValuesAsDictionary()

global count
global refresh_rate
count = 0 #1 is counter off, 0 is counter on
refresh_rate = 100
#grid numbers [column, row]
global position_clock_label
global position_clock_timer
global position_grid_row_start
global position_lap_label
global position_race_time_peloton
global position_peloton_split
global position_break_split
global position_button_row
global position_grid_label_row
position_clock_label= [3, 1]
position_clock_timer = [3,2]
position_button_row = configFile.getValueAsInt("positionButtonRow")
position_grid_label_row = configFile.getValueAsInt("positionGridLabelRow")
position_grid_row_start = configFile.getValueAsInt("positionGridDataRow")
position_lap_label= [2,position_grid_label_row]
position_race_time_peloton =[2, position_grid_row_start]
position_peloton_split = [3, position_grid_row_start ]
position_break_split = [4, position_grid_row_start]

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
        print("waldo")

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
class My_grid_box(Text):
    # elapsed_time = Text(root, height=grid_row_height, width=grid_box_width)
    # elapsed_time.grid(row=j, column = elapsed_time_column)

    lap_label_column = configFile.getValueAsInt("positionLapLabelColumn")
    elapsed_time_column = configFile.getValueAsInt("positionElapsedTimeColumn")
    split_time_column = configFile.getValueAsInt("positionSplitTimeColumn")
    grid_row_height = configFile.getValueAsInt("gridBoxHeight")
    grid_box_width = configFile.getValueAsInt("gridBoxWidth")
    def __init__(self, root, this_row, this_column):
        Text.__init__(root, height=configFile.getValueAsInt("gridBoxHeight"), width=configFile.getValueAsInt("gridBoxWidth")).grid(row=this_row, column = this_column)
        # Text(root, height=configFile.getValueAsInt("gridBoxHeight"), width=configFile.getValueAsInt("gridBoxWidth")).grid(row=this_row, column = this_column)




#start menu and tkinter stuff
#this is the upper menu bar in the window
def NewFile():
    print ("New File!")
def OpenFile():
    name = askopenfilename()
    print (name)
def About():
    print ("This is a simple example of a menu")


def refreshloop():
    #refreshes timer loop (actual time kept elsewhere)
    #this is actually the second instance of the refresh rate, hope they don't overlap
    #I think this only refreshes the grid, and the other refreshes the timer?
    root.after(refresh_rate, refreshloop)
    timer_active = Text(root, height=configFile.getValueAsInt("textBoxHeight"), width=configFile.getValueAsInt("textBoxWidth"))
    timer_active.grid(row=configFile.getValueAsInt("positionTimerRow"), column=configFile.getValueAsInt("positionTimerColumn"))
    timer_active.insert(INSERT, a_clock.t.get())


def refresh_screen():
    text_box_width = configFile.getValueAsInt("textBoxWidth")
    lap_label_column = configFile.getValueAsInt("positionLapLabelColumn")
    elapsed_time_column = configFile.getValueAsInt("positionElapsedTimeColumn")
    split_time_column = configFile.getValueAsInt("positionSplitTimeColumn")
    grid_row_height = configFile.getValueAsInt("gridBoxHeight")
    grid_box_width = configFile.getValueAsInt("gridBoxWidth")
    #refreshes changing components of software
    #refreshes at time of mouse click, not per second
    #root.after(1000, refresh_screen)
    #timer component not welcome here
    #peloton split grid
    current_length = len(a_clock.split_list_peloton)
    seq_start_row_for_grid = position_grid_row_start
    lap = 0
    #A loop that populates the splits grid
    for j in range(seq_start_row_for_grid, configFile.getValueAsInt("lapsTotal") + seq_start_row_for_grid):
        #a grid box should probably be a class object
        Label(root, text="Lap " + str(lap + 1) + ":   ").grid(row=j, column = lap_label_column)
        elapsed_time = Text(root, height=grid_row_height, width=grid_box_width)
        elapsed_time.grid(row=j, column = elapsed_time_column)
        split_time = Text(root, height=grid_row_height, width=grid_box_width)
        split_time.grid(row=j, column = split_time_column)
        next = My_grid_box(root,j,4)

        if(current_length >= lap+1):
            #testing length againts a_clock.split_list_peloton
            elapsed_time.insert(INSERT, a_clock.race_time_list_peloton[lap])
            split_time.insert(INSERT, a_clock.split_list_peloton[lap])
            next.insert(INSERT, "Test")
            #trying to create a split_time list, should this be local or part of the clock function?
            #this_split = a_clock.split_list_peloton[int(lap)] - a_clock.split_list_peloton[int(lap) - 1]
            #split_time.insert(INSERT, this_split)
        else:
            #fill out some null values for remaining cells
            elapsed_time.insert(INSERT, "Null")
            split_time.insert(INSERT, "Null")
            next.insert(INSERT, "Test")
        lap += 1

def make_screen():
    refresh_screen()

def split_button():
    a_clock.split_peloton()
    refresh_screen()

def test():
    print(a_clock.get_time_string(100000))

 #Menu bar
root = Tk()
a_clock = Watch(root)
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

#Grid spreadsheet


#output Grid



#text
#time counter is timer_active
# timer_active = Text(root, height=2, width=30)
# timer_active.grid(row=position_clock_timer[1], column=position_clock_timer[0])
# timer_active.insert(INSERT, a_clock.t.get())
timer_label_row = configFile.getValueAsInt("positionTimerLabelRow")
timer_label_column = configFile.getValueAsInt("positionTimerLabelColumn")
Label(root, text="Clock").grid(row=timer_label_row, column=timer_label_column)

#buttons
Button(root, text='Quit', command=root.quit).grid(row=position_button_row, column=0, sticky=W, pady=4)
Button(root, text='Test something', command=test).grid(row=position_button_row, column=1, sticky=W, pady=4)
Button(root, text='Peloton Split', command=split_button).grid(row=position_button_row, column=2, sticky=W, pady=4)
Button(root, text='Start Timer', command=a_clock.start).grid(row=position_button_row, column=3, sticky=W, pady=4)

root.after(refresh_rate, refreshloop)
mainloop()
#end function

#get and set functions for number output to include number access vs charactor access
#Make array instead of list for split times
#make lap splits
#make same for break
#make handling for multiple breaks
#lead times for breaks
#store results
