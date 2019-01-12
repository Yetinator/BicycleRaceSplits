import tkinter as tk
from tkinter import *
from tkinter import Tk
import tkinter.filedialog
from stopWatchClass import SwissWatch
import time
#from buttonClass import piButtons
#import RPi.GPIO as GPIO
#GPIO exists here, at the end of this file, and in the buttonclass
# from tkinter import ttk
clockers = SwissWatch()


#this codebox represents a "baseline" future "StartPage" will be defined later
class FancyWatchApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)

        container.grid(row=8, column=8, sticky=N+S+W+E)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(1, weight=1)

        container.grid_rowconfigure(2, weight=1)
        container.grid_columnconfigure(2, weight=1)

        container.grid_rowconfigure(3, weight=1)
        container.grid_columnconfigure(3, weight=1)

        container.grid_rowconfigure(4, weight=1)
        container.grid_columnconfigure(4, weight=1)

        container.grid_rowconfigure(5, weight=1)
        container.grid_columnconfigure(5, weight=1)

        container.grid_rowconfigure(6, weight=1)
        container.grid_columnconfigure(6, weight=1)

        container.grid_rowconfigure(7, weight=5)
        container.grid_columnconfigure(7, weight=5)

        self.current_time = tkinter.StringVar()
        self.current_spl_time = tkinter.StringVar()
        self.current_time.set(clockers.get_running_time())
        self.current_spl_time.set(clockers.get_running_split_time())
        # self.myButtons = piButtons()
        self.frames = {}

        #StartPage is a page we are about to make a class for
        for F in (StartPage, TimerPage, PageTwo, RaceInputPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0,  columnspan=8, rowspan=8,sticky=N+S+W+E)

            # frame.grid_rowconfigure()
            # frame.grid_columnconfigure()
            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

            frame.grid_rowconfigure(1, weight=1)
            frame.grid_columnconfigure(1, weight=1)

            frame.grid_rowconfigure(2, weight=1)
            frame.grid_columnconfigure(2, weight=1)

            frame.grid_rowconfigure(3, weight=1)
            frame.grid_columnconfigure(3, weight=1)

            frame.grid_rowconfigure(4, weight=1)
            frame.grid_columnconfigure(4, weight=1)

            frame.grid_rowconfigure(5, weight=1)
            frame.grid_columnconfigure(5, weight=1)

            frame.grid_rowconfigure(6, weight=1)
            frame.grid_columnconfigure(6, weight=1)

            frame.grid_rowconfigure(7, weight=1)
            frame.grid_columnconfigure(7, weight=1)

        #fancy watch app __init__ continued


        #self.myButtons = piButtons()
        print('myButtons line 81 needs to be turned on')
        self.looptie_loop()

        self.show_frame(StartPage)

    def show_frame(self, cont):
        #looking at the frames list at position cont
        for gone in self.frames:
            gone.grid_remove(self)
        frame = self.frames[cont]
        frame.tkraise()
        # frame.grid()

    def ExitProgram(self):
        #myButtons relates to the pi actuated buttons only
        # self.myButtons.buttonEnd()
        self.quit()

    def GetInputs(self):
        #This retrieves inputs from user and can happen during or before the race
        # for input in self.inputBoxOutput:
        #     # temp = input.get("1.0",'end-1c')
        #     temp = input.get()
        #     print(temp)

        #None of this exists yet
        print("Get Inputs function in progress")
        # lapDistance = int(self.inputBoxOutput[1].get())
        # self.clockers.set_inputs(lapDistance)

    def test_button(self):
        # self.clockers.test_button()
        print("test_button not configured")
        #self.MakeGrid()

    def peloton_split_button(self):
        self.frames[TimerPage].PelotonSplitFunction()
        # self.clockers.split_peloton()
        # #todo not calling get_lap_data for a given lap is less than straitforward, although it aims for the most recently completed lap
        # stuff = self.clockers.get_lap_data()

        #self.MakeRow(stuff, self.clockers.current_lap_index - 1)
        print("MakeRow is null in this version and needs to be replaced")
        #this needs to be current_lap_index - 1 because the lap increments just before makerow is called.
        #because the next lap is made before we are even saving information to it, this makes us ahead of the index
        #todo, make this more straitforward to access in case of change in front end

    def breakaway_split_button(self):
        self.clockers.split_break()
        stuff = self.clockers.get_lap_data()

        print("MakeRow is null in this version and needs to be replaced")
        # self.MakeRow(stuff, self.clockers.current_lap_index - 1)
        #this needs to be current_lap_index - 1 because the lap increments just before makerow is called.
        #because the next lap is made before we are even saving information to it, this makes us ahead of the index

    def RefreshClock(self):
        #don't forget to clear the clock
        pass
        # self.timer_active.delete(1.0, 2.0)
        # self.timer_active.insert(INSERT, self.clockers.get_running_time())

    def get_this_lap_data(self, lap_lap):
        # if lap_lap == None:
        #     lap_lap = clockers.current_lap_index - 1
        print(clockers.get_lap_data(lap_lap))
        return clockers.get_lap_data(lap_lap)

    def HardButtons(self, aButton):
        if aButton == False:
            pass

        if aButton ==  'a':
            self.peloton_split_button()

        if aButton == 'b':
            self.breakaway_split_button()

        if aButton == 'c':
            self.start_button()



    def looptie_loop(self):
        #any potential looping in this class should be limited to here, or mainloop
        self.RefreshClock()
        self.current_time.set(clockers.get_running_time())
        self.current_spl_time.set(clockers.get_running_split_time())
        # out = False
        # out = self.myButtons.get()
        # self.HardButtons(out)
        # print("hard buttons need to be turned on")
        # out = False
        # out = self.myButtons.get()
        #self.HardButtons(out)

        #if out != False:
        #    print(str(out))
        #    time.sleep(0.2)
        self.after(1, self.looptie_loop)

#startPage class from the codebox above

LARGE_FONT = ("Verdana" ,44)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GENERIC_X = 1
GENERIC_Y = 0
DATA_COLUMN = 1
#Grid will be 8 x 8
DATA_FONT = ("Verdana", 24, 'bold')
DATA_LABEL_FONT = ("Verdana" ,24)
INPUT_FONT = ("Verdana" ,16)
CLOCK_FONT = ("Verdana" ,54)
BUTTON_FONT = ("Verdana" ,44)
BUTTON_FONT_MENU = ("Verdana" ,24)
BUTTON_MENU_ROW1 = 0
BUTTON_MENU_ROW2 = 2
BUTTON_MENU_ROW3 = 4
BUTTON_MENU_ROW4 = 6
BUTTON_MENU_COLUMN1 = 0
BUTTON_MENU_COLUMN2 = 2
BUTTON_MENU_COLUMN3 = 4
BUTTON_MENU_COLUMN4 = 6
#FOR RACE INPUT DATA
INPUT_BOX_ROW1 = 0
INPUT_BOX_ROW2 = 2
INPUT_BOX_ROW3 = 4
INPUT_BOX_ROW4 = 6
INPUT_BOX_COLUMN = 2


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #LARGE_FONT defined above
        self.controller = controller
        label = tk.Label(self, text = "Menu", font=LARGE_FONT)
        label.grid(row=GENERIC_Y, column=GENERIC_X, columnspan=2, rowspan=2)

        # button1 = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(TimerPage))
        # button1.grid(row=GENERIC_Y + 1, column=GENERIC_X, columnspan=2, rowspan=2)
        self.buttonMenu()
        self.buttonMe()

    def buttonMenu(self, buttons = ["START","FIXME","RACEINPUT","FULLSREEN","EXIT","SAVE/EXIT","blk","blk","blk","blk","blk","blk"]):
        menuButton1 = tk.Button(self, text=buttons[0], command=self.funcMenuButton1, font = BUTTON_FONT_MENU)
        #note functionmenubutton1 has been disabled
        #menuButton1 = tk.Button(self, text=buttons[0], command=lambda: controller.show_frame(TimerPage), font = BUTTON_FONT_MENU)
        menuButton1.grid(row=BUTTON_MENU_ROW1, column=BUTTON_MENU_COLUMN1, columnspan=1, rowspan=2, sticky="nsew")

        menuButton2 = tk.Button(self, text=buttons[1], command=self.funcMenuButton2, font = BUTTON_FONT_MENU)
        menuButton2.grid(row=BUTTON_MENU_ROW2, column=BUTTON_MENU_COLUMN1, columnspan=1, rowspan=2, sticky="nsew")

        menuButton3 = tk.Button(self, text=buttons[2], command=self.funcMenuButton3, font = BUTTON_FONT_MENU)
        menuButton3.grid(row=BUTTON_MENU_COLUMN3, column=BUTTON_MENU_COLUMN1, columnspan=1, rowspan=2, sticky="nsew")

        menuButton4 = tk.Button(self, text=buttons[3], command=self.funcMenuButton4, font = BUTTON_FONT_MENU)
        menuButton4.grid(row=BUTTON_MENU_ROW4, column=BUTTON_MENU_COLUMN1, columnspan=1, rowspan=2, sticky="nsew")

        menuButton5 = tk.Button(self, text=buttons[4], command=self.funcMenuButton5, font = BUTTON_FONT_MENU)
        menuButton5.grid(row=BUTTON_MENU_ROW1, column=BUTTON_MENU_COLUMN2, columnspan=1, rowspan=2, sticky="nsew")

        menuButton6 = tk.Button(self, text=buttons[5], command=self.funcMenuButton6, font = BUTTON_FONT_MENU)
        menuButton6.grid(row=BUTTON_MENU_ROW2, column=BUTTON_MENU_COLUMN2, columnspan=1, rowspan=2, sticky="nsew")

        menuButton7 = tk.Button(self, text=buttons[6], command=self.funcMenuButton7, font = BUTTON_FONT_MENU)
        menuButton7.grid(row=BUTTON_MENU_COLUMN3, column=BUTTON_MENU_COLUMN2, columnspan=1, rowspan=2, sticky="nsew")

        menuButton8 = tk.Button(self, text=buttons[7], command=self.funcMenuButton8, font = BUTTON_FONT_MENU)
        menuButton8.grid(row=BUTTON_MENU_ROW4, column=BUTTON_MENU_COLUMN2, columnspan=1, rowspan=2, sticky="nsew")

        # menuButton9 = tk.Button(self, text=buttons[8], command=self.funcMenuButton9, font = BUTTON_FONT_MENU)
        # menuButton9.grid(row=BUTTON_MENU_ROW1, column=BUTTON_MENU_COLUMN3, columnspan=1, rowspan=2, sticky="nsew")
        #
        # menuButton10 = tk.Button(self, text=buttons[9], command=self.funcMenuButton10, font = BUTTON_FONT_MENU)
        # menuButton10.grid(row=BUTTON_MENU_ROW2, column=BUTTON_MENU_COLUMN3, columnspan=1, rowspan=2, sticky="nsew")
        #
        # menuButton11 = tk.Button(self, text=buttons[10], command=self.funcMenuButton11, font = BUTTON_FONT_MENU)
        # menuButton11.grid(row=BUTTON_MENU_ROW3, column=BUTTON_MENU_COLUMN3, columnspan=1, rowspan=2, sticky="nsew")
        #
        # menuButton12 = tk.Button(self, text=buttons[11], command=self.funcMenuButton12, font = BUTTON_FONT_MENU)
        # menuButton12.grid(row=BUTTON_MENU_ROW4, column=BUTTON_MENU_COLUMN3, columnspan=1, rowspan=2, sticky="nsew")

    def funcMenuButton1(self):
        self.controller.show_frame(TimerPage)

    def funcMenuButton2(self):
        print("Fix this broken thing")

    def funcMenuButton3(self):
        self.controller.show_frame(RaceInputPage)

    def funcMenuButton4(self):
        print("Fix this broken thing")

    def funcMenuButton5(self):
        print("Fix this broken thing")

    def funcMenuButton6(self):
        print("Fix this broken thing")

    def funcMenuButton7(self):
        print("Fix this broken thing")

    def funcMenuButton8(self):
        print("Fix this broken thing")

    def funcMenuButton9(self):
        print("Fix this broken thing")

    def funcMenuButton10(self):
        print("Fix this broken thing")

    def funcMenuButton11(self):
        print("Fix this broken thing")

    def funcMenuButton12(self):
        print("Fix this broken thing")



    def buttonMe(self, buttons = ["blk","blk","lp>","lp<"]):
        button1 = tk.Button(self, text=buttons[0], command=self.funcButton1, font = BUTTON_FONT)
        button1.grid(row=0, column=8, columnspan=1, rowspan=2, sticky="nsew")

        button2 = tk.Button(self, text=buttons[1], command=self.funcButton2, font = BUTTON_FONT)
        button2.grid(row=2, column=8, columnspan=1, rowspan=2, sticky="nsew")

        button3 = tk.Button(self, text=buttons[2], command=self.funcButton3, font = BUTTON_FONT)
        button3.grid(row=4, column=8, columnspan=1, rowspan=2, sticky="nsew")

        button4 = tk.Button(self, text=buttons[3], command=self.funcButton4, font = BUTTON_FONT)
        button4.grid(row=6, column=8, columnspan=1, rowspan=2, sticky="nsew")

    def funcButton1(self):
        print("button1")
        # self.controller.show_frame(TimerPage)

    def funcButton2(self):
        print("button2")

    def funcButton3(self):
        print("button3")

    def funcButton4(self):
        print("button4")

class TimerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # label = tk.Label(self, text = "Timer_Page", font=LARGE_FONT)
        # label.grid(row=GENERIC_Y, column=GENERIC_X, columnspan=2, rowspan=2)
        self.this_lap_data = ['lap 5', '00:00:04', '00:00:00', '0', '[]']
        self.thisLapLap = tkinter.StringVar()
        self.thisLapPel = tkinter.StringVar()
        self.thisLapSpl = tkinter.StringVar()
        self.thisLapSpeed = tkinter.StringVar()
        self.thisLapBrk1 = tkinter.StringVar()
        self.thisLapBrk2 = tkinter.StringVar()
        self.thisLapBrk3 = tkinter.StringVar()
        self.thisRaceAvg = tkinter.StringVar()
        self.currentLapView = clockers.current_lap_index
        self.followCurrentLap = True

        # self.thisLapLap.set(self.this_lap_data[0])
        self.updatePage(self.currentLapView)
        #labels
        lapLabel = tk.Label(self, text = "Lap: ", font=DATA_LABEL_FONT)
        lapLabel.grid(row=0, column=0,sticky="nse")

        pelLabel = tk.Label(self, text = "Pel: ", font=DATA_LABEL_FONT)
        pelLabel.grid(row=1, column=0,sticky="nse")

        splLabel = tk.Label(self, text = "Spl: ", font=DATA_LABEL_FONT)
        splLabel.grid(row=2, column=0,sticky="nse")

        brkLabel = tk.Label(self, text = "Brk: ", font=DATA_LABEL_FONT)
        brkLabel.grid(row=3, column=0,sticky="nse")

        mphLabel = tk.Label(self, text = "MPH!: ", font=DATA_LABEL_FONT)
        mphLabel.grid(row=4, column=0,sticky="nse")

        clockLabel = tk.Label(self, text = "Time: ", font=DATA_LABEL_FONT)
        clockLabel.grid(row=6, column=0,sticky="nse")

        avgLabel = tk.Label(self, text = "Avg spl", font=DATA_LABEL_FONT)
        avgLabel.grid(row=0, column=2,sticky= E)

        #Data
        lapData = tk.Label(self, textvariable = self.thisLapLap, font=DATA_FONT)
        lapData.grid(row=0, column=DATA_COLUMN, columnspan = 2, sticky = W)

        pelData = tk.Label(self, textvariable = self.thisLapPel, font=DATA_FONT)
        pelData.grid(row=1, column=DATA_COLUMN, columnspan = 2, sticky = W)

        splData = tk.Label(self, textvariable = self.thisLapSpl, font=DATA_FONT)
        splData.grid(row=2, column=DATA_COLUMN, columnspan = 2, sticky = W)

        brkData = tk.Label(self, textvariable = self.thisLapBrk1, font=DATA_FONT)
        brkData.grid(row=3, column=DATA_COLUMN, columnspan = 2, sticky = W)

        mphData = tk.Label(self, textvariable = self.thisLapSpeed, font=DATA_FONT)
        mphData.grid(row=4, column=DATA_COLUMN, columnspan = 2, sticky = W)

        avgData = tk.Label(self, textvariable = self.thisRaceAvg, font=DATA_FONT)
        avgData.grid(row=1, column=2, columnspan = 2, sticky = E)


        # clockText = tk.Text(self)
        # clockText.grid(row=0, column=1, columnspan=3)
        # clockText.insert(INSERT, "00:00:00.0")

        self.clockText = tk.Label(self, textvariable = controller.current_time, font=CLOCK_FONT, bg = 'cyan')
        self.clockText.grid(row=6, column=1, columnspan = 2)

        self.clockSpl = tk.Label(self, textvariable = controller.current_spl_time, font=DATA_FONT, bg = 'cyan')
        self.clockSpl.grid(row=2, column=2, columnspan = 2, sticky = E)

        self.buttonMe()



    def buttonMe(self, buttons = ["Menu","blk","lp>","lp<"]):
        button1 = tk.Button(self, text=buttons[0], command=self.funcButton1, font = BUTTON_FONT)
        button1.grid(row=0, column=8, columnspan=1, rowspan=2, sticky="nsew")

        button2 = tk.Button(self, text=buttons[1], command=self.funcButton2, font = BUTTON_FONT)
        button2.grid(row=2, column=8, columnspan=1, rowspan=2, sticky="nsew")

        button3 = tk.Button(self, text=buttons[2], command=self.funcButton3, font = BUTTON_FONT)
        button3.grid(row=4, column=8, columnspan=1, rowspan=2, sticky="nsew")

        button4 = tk.Button(self, text=buttons[3], command=self.funcButton4, font = BUTTON_FONT)
        button4.grid(row=6, column=8, columnspan=1, rowspan=2, sticky="nsew")

    def funcButton1(self):
        print("button1")
        self.controller.show_frame(StartPage)

    def funcButton2(self):
        print("button2")


    def funcButton3(self):
        print("button3")
        if self.currentLapView < clockers.current_lap_index - 1:
            self.currentLapView = self.currentLapView + 1
            self.followCurrentLap = False
        else:
            self.followCurrentLap = True
        self.updatePage(self.currentLapView)

    def funcButton4(self):
        print("button4")
        if self.currentLapView > 0:
            self.currentLapView = self.currentLapView - 1
        self.followCurrentLap = False
        self.updatePage(self.currentLapView)

        # FancyWatchApp.ExitProgram(self)

    def PelotonSplitFunction(self):
        global clock_running
        if clockers.get_running_time() == "00:00:00":
            clockers.start()
        else:
            clockers.split_peloton()
        # self.this_lap_data
        # self.this_lap_data = FancyWatchApp.get_this_lap_data(self)
        if self.followCurrentLap == True:
            self.currentLapView = clockers.current_lap_index - 1
        self.updatePage(self.currentLapView)

    def BreakAwaySplitFunction(self):
        clockers.split_break()

    def updatePage(self, lap_lap):
        # if lap_lap == False:
        #     self.this_lap_data = (FancyWatchApp.get_this_lap_data(self))
        #     print("Full lap data: " + str(self.this_lap_data))
        # else:
        #     self.this_lap_data = (FancyWatchApp.get_this_lap_data(self, lap_lap))
        self.this_lap_data = (FancyWatchApp.get_this_lap_data(self, lap_lap))
        self.this_race_data = clockers.get_race_data()
        print(str(self.this_race_data) + "is race data")

        #Don't loop here bro
        lap = str(self.this_lap_data[0]) + ": of :" + str(clockers.current_lap_index)
        print("lap is " + str(lap))
        self.thisLapLap.set(lap)
        self.thisLapPel.set(self.this_lap_data[1])
        self.thisLapSpl.set(self.this_lap_data[2])
        self.thisLapSpeed.set(self.this_lap_data[3])
        self.thisLapBrk1.set(self.this_lap_data[4])
        self.thisRaceAvg.set(self.this_race_data[0])



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # style = ttk.Style()
        # style.configure("",
        #         foreground="midnight blue",
        #         font="Times 20 bold italic",
        #         padding=20)
        self.this = []
        self.gridMe()
        self.buttonMe()


    def gridMe(self):

        for xValue in range(6):
            for yValue in range(6):
                self.this.append(Label(self,text="Here").grid(row=yValue, column=xValue))

    def buttonMe(self, buttons = ["b1","b2","b3","b4"]):
        button1 = tk.Button(self, text=buttons[0], command=self.funcButton1)
        button1.grid(row=0, column=8, columnspan=1, rowspan=2)

        button2 = tk.Button(self, text=buttons[1], command=self.funcButton2)
        button2.grid(row=2, column=8, columnspan=1, rowspan=2)

        button3 = tk.Button(self, text=buttons[2], command=self.funcButton3)
        button3.grid(row=4, column=8, columnspan=1, rowspan=2)

        button4 = tk.Button(self, text=buttons[3], command=self.funcButton4)
        button4.grid(row=6, column=8, columnspan=1, rowspan=2)

    def funcButton1(self):
        print("button1")

    def funcButton2(self):
        print("button2")

    def funcButton3(self):
        print("button3")

    def funcButton4(self):
        print("button4")

class RaceInputPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #LARGE_FONT defined above
        self.controller = controller
        self.LapDefault = StringVar(self.controller, clockers.get_lap_miles())
        # label = tk.Label(self, text = "Race Input", font=LARGE_FONT)
        # label.grid(row=GENERIC_Y, column=GENERIC_X, columnspan=2, rowspan=2)
        #inputs
        self.inputGrid()
        self.buttonMe()

    def buttonMe(self, buttons = ["Menu","Save","lp>","lp<"]):
        button1 = tk.Button(self, text=buttons[0], command=self.funcButton1, font = BUTTON_FONT)
        button1.grid(row=0, column=8, columnspan=1, rowspan=2, sticky="nsew")

        button2 = tk.Button(self, text=buttons[1], command=self.funcButton2, font = BUTTON_FONT)
        button2.grid(row=2, column=8, columnspan=1, rowspan=2, sticky="nsew")

        button3 = tk.Button(self, text=buttons[2], command=self.funcButton3, font = BUTTON_FONT)
        button3.grid(row=4, column=8, columnspan=1, rowspan=2, sticky="nsew")

        button4 = tk.Button(self, text=buttons[3], command=self.funcButton4, font = BUTTON_FONT)
        button4.grid(row=6, column=8, columnspan=1, rowspan=2, sticky="nsew")

    def funcButton1(self):
        print("button1")
        self.controller.show_frame(StartPage)

    def funcButton2(self):
        #Save

        self.saveInputGrid()
        print("button2")

    def funcButton3(self):
        print("button3")

    def funcButton4(self):
        print("button4")

    def inputGrid(self):
        #this is a list of input boxes
        print("inputGrid")
        #race Name
        self.raceNameLabel = tk.Label(self, text = "Course", font=INPUT_FONT)
        self.raceNameLabel.grid(row=INPUT_BOX_ROW1, column=0, columnspan=2, rowspan=1)
        self.raceName = tk.Entry(self, width=16, font=INPUT_FONT)
        self.raceName.grid(row=INPUT_BOX_ROW1, column=4, columnspan=2, rowspan=1)
        # buttonRand = tk.Entry(self, text="Hello World", font = DATA_LABEL_FONT)
        # buttonRand.grid(row=0, column=0, columnspan=1, rowspan=2, sticky="nsew")
        #race date
        self.raceDateLabel = tk.Label(self, text = "Race Date", font=INPUT_FONT)
        self.raceDateLabel.grid(row=INPUT_BOX_ROW2, column=0, columnspan=2, rowspan=1)
        self.raceDate = tk.Entry(self, width=16, font=INPUT_FONT)
        self.raceDate.grid(row=INPUT_BOX_ROW2, column=4, columnspan=2, rowspan=1)
        #lap distance (moved to init)
        # self.LapDefault = StringVar(self.controller, clockers.get_lap_miles())
        # LapDefault = StringVar(self.controller,"random")
        self.lapDistanceLabel = tk.Label(self, text = "Lap Distance (Miles)", font=INPUT_FONT)
        self.lapDistanceLabel.grid(row=INPUT_BOX_ROW3, column=0, columnspan=2, rowspan=1)
        self.lapDistance = tk.Entry(self, width=16, textvariable=self.LapDefault, font=INPUT_FONT)
        self.lapDistance.grid(row=INPUT_BOX_ROW3, column=4, columnspan=2, rowspan=1)
        # LapDistance Increase decrease buttons
        buttonUp = tk.Button(self, text="Distance Up", command=self.lapDistanceIncrease, font = INPUT_FONT)
        buttonUp.grid(row=INPUT_BOX_ROW4, column=0, columnspan=1, rowspan=1, sticky="nsew")

        buttonDown = tk.Button(self, text="Distance Down", command=self.lapDistanceDecrease, font = INPUT_FONT)
        buttonDown.grid(row=INPUT_BOX_ROW4, column=4, columnspan=1, rowspan=1, sticky="nsew")

    def saveInputGrid(self):
        self.raceName.get()
        self.raceDate.get()
        clockers.set_inputs(self.lapDistance.get(),"miles")

    def lapDistanceIncrease(self):
        self.LapDefault.set(round(float(self.LapDefault.get())+.1,1))
    def lapDistanceDecrease(self):
        self.LapDefault.set(round(float(self.LapDefault.get())-.1,1))





#The end of page classes
def func1(var):
    print("Button pressed.  Button 1")
    app.frames[TimerPage].PelotonSplitFunction()

def func2(var):
    print("Button pressed.  Button 2")
    app.frames[TimerPage].BreakAwaySplitFunction()

def func3(var):
    print("Button pressed.  Button 3")

def func4(var):
    print("Button pressed.  Button 4")


app = FancyWatchApp()
app.geometry('640x480')

#Add all this back for raspberry pi
# GPIO.setmode(GPIO.BCM)
# chan_list = [17,22,23,27]
# GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
# GPIO.add_event_detect(chan_list[0], GPIO.BOTH, callback = func1, bouncetime=300)
# GPIO.add_event_detect(chan_list[1], GPIO.BOTH, callback = func2, bouncetime=300)
# GPIO.add_event_detect(chan_list[2], GPIO.BOTH, callback = func3, bouncetime=300)
# GPIO.add_event_detect(chan_list[3], GPIO.BOTH, callback = func4, bouncetime=300)
# run = True

app.mainloop()
