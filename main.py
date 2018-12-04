#/usr/bin/python3 menu01.py
#came from menu01
#Main from BicycleRaceSplits

from tkinter import *
import tkinter.filedialog
import time
from array import *
#from filedialog   import askopenfilename
#class Stopwatch
#https://www.youtube.com/watch?v=pPvmC0Srdeo
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
position_button_row = 4
position_grid_label_row = 6
position_grid_row_start = 9
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
    t1 = Text(root, height=2, width=30)
    t1.grid(row=5, column=2)
    t1.insert(INSERT, a_clock.t.get())


def refresh_screen():
    text_box_width = 15
    #refreshes changing components of software
    #refreshes at time of mouse click, not per second
    #root.after(1000, refresh_screen)
    #timer component
    # t1 = Text(root, height=2, width=30)
    # t1.grid(row=position_clock_label[0], column=position_clock_label[1])
    # t1.insert(INSERT, a_clock.t.get())
    #peloton split grid
    label_elapsed_time = Text(root, height=2, width=30)
    label_elapsed_time.grid(row=position_lap_label[1], column=position_lap_label[0])
    label_elapsed_time.insert(INSERT, "Elapsed Time")
    current_length = len(a_clock.split_list_peloton)
    seq_start_row_for_grid = position_grid_row_start
    lap = 0
    for j in range(seq_start_row_for_grid, 35 + seq_start_row_for_grid):
        Label(root, text="Lap " + str(lap) + ":   ").grid(row=j, column = 1)
        elapsed_time = Text(root, height=1, width=text_box_width)
        elapsed_time.grid(row=j, column = 2)
        split_time = Text(root, height=1, width=text_box_width)
        split_time.grid(row=j, column = 3)

        if(current_length >= lap+1):
            elapsed_time.insert(INSERT, a_clock.race_time_list_peloton[lap])
            split_time.insert(INSERT, a_clock.split_list_peloton[lap])
            #print(a_clock.split_list_peloton[lap])
            #trying to create a split_time list, should this be local or part of the clock function?
            #this_split = a_clock.split_list_peloton[int(lap)] - a_clock.split_list_peloton[int(lap) - 1]
            #split_time.insert(INSERT, this_split)
        else:
            #fill out some null values for remaining cells
            elapsed_time.insert(INSERT, "Null")
            split_time.insert(INSERT, "Null")
        lap += 1

def make_screen():
    refresh_screen()

def split_button():
    a_clock.split_peloton()
    refresh_screen()

def test():
    a_clock.get_time_string(100000)

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
Label(root, text="hey").grid(row=0)
Label(root, text="you").grid(row=1)
Label(root, text="there").grid(row=2)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

#output Grid



#text
#time counter is t1
# t1 = Text(root, height=2, width=30)
# t1.grid(row=position_clock_timer[1], column=position_clock_timer[0])
# t1.insert(INSERT, a_clock.t.get())
Label(root, text="Clock").grid(row=5)

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
