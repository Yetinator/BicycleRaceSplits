#BicycleRaceSplits
#This is meant to compartmentalizer the Tk window and maybe make it easier
#to reuse code in future projects
from abc import ABC, abstractmethod
from tkinter import *
from tkinter import Tk
import tkinter as tk
import tkinter.filedialog
from writeClass import *
from stopWatchClass import SwissWatch
from buttonClass import piButtons

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


    def ExitProgram(self):
        self.myButtons.buttonEnd()
        self.quit()

    def MakeScreen(self):
        #this is called in the constructer as part of the superclass
        #it basically calls other aspects of the screen that could probably be frames
        self.MakeInputBoxes()
        self.MakeButtons()
        self.MakeClock()
        self.MakeGrid()

    def MakeButtons(self):
        #pass this to Makescreen which is called by superclass

        # butts = {"Quit":"self.ExitProgram",
        #     "Test Something":"self.test_button",
        #     "Peloton Split":"self.test_button",
        #     "Breakaway Split":"self.test_button",
        #     "Start Timer":"self.test_button"}
        # item_index = 0
        # for butt in butts:
        #     Button(text=butt, command=butts[butt]).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        #     item_index += 1

        item_index = 0
        Button(text='Quit', command=self.ExitProgram).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Log Inputs', command=self.GetInputs).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Test something', command=self.test_button).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Peloton Split', command=self.peloton_split_button).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Breakaway Split', command=self.breakaway_split_button).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)
        item_index += 1
        Button(text='Start Timer', command=self.start_button).grid(row=self.position_button_row, column=item_index, sticky=W, pady=4)

    def MakeClock(self):
        #pass this to Makescreen which is called by superclass
        # global rando
        Label(text="Clock").grid(row=self.timer_label_row, column=self.timer_label_column)
        self.timer_active = Text(height=self.text_box_height, width=self.text_box_width)
        self.timer_active.grid(row=self.position_timer_row, column=self.position_timer_column)
        self.timer_active.insert(INSERT, self.clockers.get_running_time())

    def MakeInputBoxes(self):
        # position_input_box_row
        # inputs = ["Course", "Lap Distance", "Duration in minutes"]
        # self.inputBoxes = []
        for input in self.inputBoxLabels:
            item_index =  self.inputBoxLabels.index(input)
            self.inputLabel = Label(text=input).grid(row=self.position_input_box_label_row, column=item_index)
            # self.inputBoxes[item_index] = Text(height=self.text_box_height, width=self.text_box_width)
            # self.inputBoxes.append(Text(height=self.text_box_height, width=self.text_box_width))
            self.inputBoxOutput.append(Entry(width=self.text_box_width))
            self.inputBoxOutput[item_index].grid(row=self.position_input_box_row, column=item_index)

    #Todo - move to stopwatchclass
    inputBoxLabels = ["Course", "Lap Distance", "Duration in minutes"]
    inputBoxOutput = []

    def GetInputs(self):
        #This retrieves inputs from user and can happen during or before the race
        # for input in self.inputBoxOutput:
        #     # temp = input.get("1.0",'end-1c')
        #     temp = input.get()
        #     print(temp)
        lapDistance = int(self.inputBoxOutput[1].get())
        self.clockers.set_inputs(lapDistance)

    def MakeGrid(self):
        #pass this to Makescreen which is called by superclass
        #This is the grid for lap times exc
        #todo - this seems more convaluted than it should be?
        #todo, this function refreshes only to the laps written into config file
        current_length = self.laps_total#len(a_clock.split_list_peloton)
        #todo makegrid currently does not refresh past laps total
        self.seq_start_row_for_grid = self.position_grid_row_start
        # self.position_grid_row_label
        #makes the Label row
        self.MakeGridLabels()
        lap_index = 0
        stuff = ["something", "went", "wrong"]
        #A loop that populates the splits grid
        for j in range(self.seq_start_row_for_grid, self.laps_total + self.seq_start_row_for_grid):
            #the input list "Stuff" will have to update with j to reflect the associated lists for time stats
            stuff = self.clockers.get_lap_data(lap_index)
            self.MakeRow(stuff, lap_index)
            lap_index += 1

    def MakeGridLabels(self):
        # get a list of labels
        labels = self.clockers.get_lap_labels()

        # find where they go
        this_label_row = self.position_grid_row_label

        # write the row of labels similar to MakeRow > MakeCell
        for label in labels:
            column_column = labels.index(label)
            Label(text = label, height=self.grid_row_height, width=self.grid_box_width).grid(row=this_label_row, column = column_column)
        # self.MakeRow(labels, self.position_grid_row_label)

    def MakeRow(self, input_list, lap_lap = None):
        #Makes one row. This could be called with MakeGrid or without
        if lap_lap == None:
            lap_lap = self.clockers.current_lap_index
        #a_column represents one data item in a list of strings
        for aColumn in range(len(input_list)):
            # this loop creates a cell for each item in the list
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
        self.position_grid_row_label = configFile.getValueAsInt("positionGridLabelRow")
        self.text_box_height = configFile.getValueAsInt("textBoxHeight")
        self.position_timer_row = configFile.getValueAsInt("positionTimerRow")
        self.position_timer_column = configFile.getValueAsInt("positionTimerColumn")
        self.refresh_rate = configFile.getValueAsInt("refreshRate")
        self.position_input_box_row = configFile.getValueAsInt("positionInputBoxRow")
        self.position_input_box_label_row = configFile.getValueAsInt("positionInputBoxLabelRow")

        # configFileDictionary = configFile.getValuesAsDictionary()
        # print("The following are config Keys in the configFile")
        # for key in configFileDictionary:
        #     #TODO Somehow test values to see if they are used in this class
        #     print("Key Value from Dictionary = " + str(key))

    def RefreshClock(self):
        #don't forget to clear the clock
        self.timer_active.delete(1.0, 2.0)
        self.timer_active.insert(INSERT, self.clockers.get_running_time())

    def looptie_loop(self):
        #any potential looping in this class should be limited to here, or mainloop
        self.RefreshClock()
        print(str(self.myButtons.get()))
        self.after(.5, self.looptie_loop)

    def start_button(self):
        self.clockers.start()

    def peloton_split_button(self):
        self.clockers.split_peloton()
        #todo not calling get_lap_data for a given lap is less than straitforward, although it aims for the most recently completed lap
        stuff = self.clockers.get_lap_data()
        self.MakeRow(stuff, self.clockers.current_lap_index - 1)
        #this needs to be current_lap_index - 1 because the lap increments just before makerow is called.
        #because the next lap is made before we are even saving information to it, this makes us ahead of the index
        #todo, make this more straitforward to access in case of change in front end

    def breakaway_split_button(self):
        self.clockers.split_break()
        stuff = self.clockers.get_lap_data()
        self.MakeRow(stuff, self.clockers.current_lap_index - 1)
        #this needs to be current_lap_index - 1 because the lap increments just before makerow is called.
        #because the next lap is made before we are even saving information to it, this makes us ahead of the index

    def test_button(self):
        # self.clockers.test_button()
        self.MakeGrid()

    def __init__(self, *args, **kwargs):
        self.clockers = SwissWatch()
        #makeConfigure is just my configuration file
        self.MakeConfigure()
        AbstractWindow.__init__(self, *args, **kwargs)
        self.myButtons = piButtons()
        self.looptie_loop()
