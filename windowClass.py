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
from stopWatchClass import SwissWatch

global rando
rando = 1

class AbstractWindow(ABC, tk.Tk):

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
    #MakeScreen > MakeButtons, MakeGrid, MakeClock (LOOP MakeClock?)
    #update_time_stamp > MakeClock (loop timestamp in main)

    def ExitProgram(self):
        self.quit()

    def MakeScreen(self):
        #this is called in the constructer as part of the superclass
        #it basically calls other aspects of the screen that could probably be frames
        self.MakeButtons()
        self.MakeClock()
        self.MakeGrid()

    def MakeButtons(self):
        #pass this to Makescreen which is called by superclass
        Button(text='Quit', command=self.ExitProgram).grid(row=self.position_button_row, column=0, sticky=W, pady=4)
        Button(text='Test something', command=self.test_button).grid(row=self.position_button_row, column=1, sticky=W, pady=4)
        Button(text='Peloton Split', command=self.peloton_split_button).grid(row=self.position_button_row, column=2, sticky=W, pady=4)
        Button(text='Start Timer', command=self.start_button).grid(row=self.position_button_row, column=3, sticky=W, pady=4)

    def MakeClock(self):
        #pass this to Makescreen which is called by superclass
        # global rando
        Label(text="Clock").grid(row=self.timer_label_row, column=self.timer_label_column)
        self.timer_active = Text(height=self.text_box_height, width=self.text_box_width)
        self.timer_active.grid(row=self.position_timer_row, column=self.position_timer_column)
        self.timer_active.insert(INSERT, self.time_stamp)
        # self.after(self.refresh_rate, self.MakeClock)
        # self.timer_active.configure(text=str(self.time_stamp))

    def RefreshClock(self):
        #don't forget to clear the clock
        self.timer_active.delete(1.0, 2.0)
        self.timer_active.insert(INSERT, self.time_stamp)

    def MakeGrid(self):
        #pass this to Makescreen which is called by superclass
        #This is the grid for lap times exc
        #todo, this function refreshes only to the laps written into config file
        current_length = self.laps_total#len(a_clock.split_list_peloton)
        #todo makegrid currently does not refresh past laps total
        self.seq_start_row_for_grid = self.position_grid_row_start
        lap_index = 0
        stuff = ["this", "that", "the Other"]
        #A loop that populates the splits grid
        #for j in range(begining row of grid, end row of grid)
        for j in range(self.seq_start_row_for_grid, self.laps_total + self.seq_start_row_for_grid):
            #the input list "Stuff" will have to update with j to reflect the associated lists for time stats
            # stuff = self.MakeLapData(lap)
            stuff = self.clockers.get_lap_data(lap_index)
            self.MakeRow(stuff, lap_index)

            lap_index += 1

    #
    # def MakeLapData(self, lap_lap):
    #     #depreciated
    #     #this should return a list of cell data for a given row or column_column
    #     #problem is this probably pulls data from main and locally
    #     #there are like 4 data columns and a lap lap_counter
    #     #A for loop should loop through each list and create an entry at the
    #     #appropriate position.
    #     #I probablyshould move this function to StopwatchClass
    #     if (lap_lap < len(self.clockers.lap_datas)):
    #     # if True:
    #         # pelotonTime = "didn't pass"
    #         print(lap_lap)
    #         pelotonTime = self.clockers.race_time_list_peloton
    #         pelotonSplit = self.clockers.split_list_peloton(lap_lap)
    #         #breakSplit = self.clockers.split_list_break[lap_lap]
    #         breakSplit = "OK"
    #     else:
    #         pelotonTime = "Nope1"
    #         pelotonSplit = "Nope2"
    #         breakSplit = "Nope3"
    #     return ["Lap " + str(lap_lap + 1), str(pelotonTime), str(pelotonSplit), str(breakSplit), "hey"]

    def MakeRow(self, input_list, lap_lap = None):
        #Makes one row. This could be called with MakeGrid or without
        if lap_lap == None:
            lap_lap = self.clockers.current_lap_index
        for aColumn in range(len(input_list)):
            input_input = input_list[aColumn]
            self.MakeCell(input_input, lap_lap, aColumn)

    def MakeCell(self, input_input, lap_lap, column_column):
        #called by MakeRow
        cellRow = lap_lap + self.seq_start_row_for_grid
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
        self.time_stamp = (timeStamp)
        self.RefreshClock()


    def looptie_loop(self):
        #any potential looping in this class should be limited to here, or mainloop
        #timers = self.clockers.bazinga()
        timers = self.clockers.get_running_time()
        self.update_time_stamp(timers)
        # self.update_idletasks()
        # self.update()
        self.after(1, self.looptie_loop)
        #self.looptie_loop()

    def start_button(self):
        self.clockers.start()

    def peloton_split_button(self):
        self.clockers.split_peloton()
        # lap = self.clockers.LapData.current_lap
        stuff = self.clockers.get_lap_data()
        # self.MakeRow(stuff, lap)
        self.MakeRow(stuff, self.clockers.current_lap_index - 1)
        #this needs to be current_lap_index - 1 because the lap increments just before makerow is called.
        #because the next lap is made before we are even saving information to it, this makes us ahead of the index

    def test_button(self):
        # self.clockers.test_button()
        self.MakeGrid()


    def __init__(self, *args, **kwargs):
        # tk.Tk.__init__(self, *args, **kwargs)
        self.time_stamp = ("00:00:00")
        self.clockers = SwissWatch()

        # self.time_stamp = StringVar()
        # self.time_stamp = ("00:00:00")

        #makeConfigure is just my configuration file
        self.MakeConfigure()

        #MakeFileMenu
        #Makescreen
        AbstractWindow.__init__(self, *args, **kwargs)
        self.looptie_loop()
