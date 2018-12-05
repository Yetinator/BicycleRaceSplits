#BicycleRaceSplits
#This is meant to compartmentalizer the Tk window and maybe make it easier
#to reuse code in future projects
from abc import ABC, abstractmethod
from tkinter import *
from tkinter import Tk
import tkinter as tk
import tkinter.filedialog
from writeClass import *
import time

global rando
rando = 1

class AbstractWindow(ABC, tk.Tk):

    @abstractmethod
    def do_something(self):
        pass

    def NewFile(self):
        print ("New File called from super class")
    def OpenFile(self):
        print("OpenFile called from super class")
    def About(self):
        print ("About called from super class")

    def MakeFileMenu(self):
        self.menu = Menu()
        self.config(menu=self.menu)
        filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self.NewFile)
        filemenu.add_command(label="Open...", command=self.OpenFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)

        helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=self.About)

    def MakeScreen(self):
        self.label = tk.Label(text="Hello, world\nThis label was created in the super class")
        self.label.pack(padx=10, pady=10)


    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        ABC.__init__(self, *args, **kwargs)
        self.MakeFileMenu()
        self.MakeScreen()

class MyWindow(AbstractWindow, tk.Tk):

    def do_something(self):
        print("I don't want to do something")

    def MakeScreen(self):
        #this is called in the constructer as part of the superclass
        #it basically calls other aspects of the screen that could probably be frames
        self.MakeButtons()
        self.MakeClock()
        self.MakeGrid()

    def MakeButtons(self):
        #pass this to Makescreen which is called by superclass
        Button(text='Quit', command=self.quit).grid(row=self.position_button_row, column=0, sticky=W, pady=4)
        Button(text='Test something', command=self.do_something).grid(row=self.position_button_row, column=1, sticky=W, pady=4)
        Button(text='Peloton Split', command=self.do_something).grid(row=self.position_button_row, column=2, sticky=W, pady=4)
        Button(text='Start Timer', command=self.do_something).grid(row=self.position_button_row, column=3, sticky=W, pady=4)

    def MakeClock(self):
        #pass this to Makescreen which is called by superclass
        # global rando
        Label(text="Clock").grid(row=self.timer_label_row, column=self.timer_label_column)
        timer_active = Text(height=self.text_box_height, width=self.text_box_width)
        timer_active.grid(row=self.position_timer_row, column=self.position_timer_column)
        timer_active.insert(INSERT, self.time_stamp)
        # rando += 1
        self.after(self.refresh_rate, self.MakeClock)
        # timer_active.insert(INSERT, a_clock.t.get())

    def MakeGrid(self):
        #pass this to Makescreen which is called by superclass
        #This is the grid for lap times exc
        current_length = 10#len(a_clock.split_list_peloton)
        self.seq_start_row_for_grid = self.position_grid_row_start
        lap = 0
        stuff = ["this", "that", "the Other"]
        #A loop that populates the splits grid
        #for j in range(begining row of grid, end row of grid)
        for j in range(self.seq_start_row_for_grid, self.laps_total + self.seq_start_row_for_grid):
            #the input list "Stuff" will have to update with j to reflect the associated lists for time stats
            stuff = self.MakeLapData(lap)
            self.MakeRow(stuff, lap)

            lap += 1

    def MakeLapData(self, lap_lap):
        #this should return a list of cell data for a given row or column_column
        #problem is this probably pulls data from main and locally
        #there are like 4 data columns and a lap lap_counter
        #A for loop should loop through each list and create an entry at the
        #appropriate position.
        return ["Lap " + str(lap_lap), "this", "that", "the other", "hey"]

    def MakeRow(self, input_list, lap_lap):
        #Makes one row. This could be called with MakeGrid or without
        for aColumn in range(len(input_list)):
            input_input = input_list[aColumn]
            self.MakeCell(input_input, lap_lap, aColumn)

    def MakeCell(self, input_input, lap_lap, column_column):
        #called by MakeRow
        cellRow = lap_lap +self.seq_start_row_for_grid
        Label(text = input_input, height=self.grid_row_height, width=self.grid_box_width).grid(row=cellRow, column = column_column)

    def MakeConfigure(self):
        configFile = ReadFile("configGeneral.txt")
        self.position_button_row = configFile.getValueAsInt("positionButtonRow")
        self.timer_label_row = configFile.getValueAsInt("positionTimerLabelRow")
        self.timer_label_column = configFile.getValueAsInt("positionTimerLabelColumn")
        self.lap_label_column = configFile.getValueAsInt("positionLapLabelColumn")
        self.elapsed_time_column = configFile.getValueAsInt("positionElapsedTimeColumn")
        self.split_time_column = configFile.getValueAsInt("positionSplitTimeColumn")
        self.grid_row_height = configFile.getValueAsInt("gridBoxHeight")
        self.grid_box_width = configFile.getValueAsInt("gridBoxWidth")

        self.text_box_width = configFile.getValueAsInt("textBoxWidth")
        self.laps_total = configFile.getValueAsInt("lapsTotal")
        self.position_grid_row_start = configFile.getValueAsInt("positionGridDataRow")
        self.text_box_height = configFile.getValueAsInt("textBoxHeight")
        self.position_timer_row = configFile.getValueAsInt("positionTimerRow")
        self.position_timer_column = configFile.getValueAsInt("positionTimerColumn")
        self.refresh_rate = configFile.getValueAsInt("refreshRate")

        configFileDictionary = configFile.getValuesAsDictionary()
        print("The following are config Keys in the configFile")
        for key in configFileDictionary:
            #TODO Somehow test values to see if they are used in this class
            print("Key Value from Dictionary = " + str(key))

    def update_time_stamp(self, timeStamp):
        #this is desined to accept a timestamp value from the stopwatch by way of mainloop
        self.time_stamp = str(timeStamp)


    def __init__(self, *args, **kwargs):
        # tk.Tk.__init__(self, *args, **kwargs)
        self.time_stamp = ("00:00:00")

        self.MakeConfigure()

        AbstractWindow.__init__(self, *args, **kwargs)
