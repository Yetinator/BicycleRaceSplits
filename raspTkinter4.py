import tkinter as tk
from tkinter import *
from tkinter import Tk
import tkinter.filedialog
from stopWatchClass import SwissWatch
import time
from buttonClass import piButtons
import RPi.GPIO as GPIO
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
        self.current_time.set(clockers.get_running_time())
        # self.myButtons = piButtons()
        self.frames = {}

        #StartPage is a page we are about to make a class for
        for F in (StartPage, TimerPage, PageTwo):
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

LARGE_FONT = ("Verdana" ,54)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GENERIC_X = 1
GENERIC_Y = 0
DATA_COLUMN = 1
#Grid will be 8 x 8
DATA_FONT = ("Verdana", 24, 'bold')
DATA_LABEL_FONT = ("Verdana" ,24)
CLOCK_FONT = ("Verdana" ,54)
BUTTON_FONT = ("Verdana" ,44)



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #LARGE_FONT defined above
        label = tk.Label(self, text = "What the?", font=LARGE_FONT)
        label.grid(row=GENERIC_Y, column=GENERIC_X, columnspan=2, rowspan=2)

        button1 = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(TimerPage))
        button1.grid(row=GENERIC_Y + 1, column=GENERIC_X, columnspan=2, rowspan=2)

        self.buttonMe()

    def buttonMe(self, buttons = ["b1","b2","b3","b4"]):
        button1 = tk.Button(self, text=buttons[0], command=self.funcButton1, font = BUTTON_FONT)
        button1.grid(row=0, column=8, columnspan=1, rowspan=2)

        button2 = tk.Button(self, text=buttons[1], command=self.funcButton2, font = BUTTON_FONT)
        button2.grid(row=2, column=8, columnspan=1, rowspan=2)

        button3 = tk.Button(self, text=buttons[2], command=self.funcButton3, font = BUTTON_FONT)
        button3.grid(row=4, column=8, columnspan=1, rowspan=2)

        button4 = tk.Button(self, text=buttons[3], command=self.funcButton4, font = BUTTON_FONT)
        button4.grid(row=6, column=8, columnspan=1, rowspan=2)

    def funcButton1(self):
        print("button1")
        controller.show_frame(TimerPage)

    def funcButton2(self):
        print("button2")

    def funcButton3(self):
        print("button3")

    def funcButton4(self):
        print("button4")

class TimerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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


        # clockText = tk.Text(self)
        # clockText.grid(row=0, column=1, columnspan=3)
        # clockText.insert(INSERT, "00:00:00.0")

        self.clockText = tk.Label(self, textvariable = controller.current_time, font=CLOCK_FONT, bg = 'cyan')
        self.clockText.grid(row=6, column=1, columnspan = 2)

        self.buttonMe()



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
        controller.show_frame(StartPage)

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

        #Don't loop here bro
        lap = str(self.this_lap_data[0]) + ": of :" + str(clockers.current_lap_index)
        print("lap is " + str(lap))
        self.thisLapLap.set(lap)
        self.thisLapPel.set(self.this_lap_data[1])
        self.thisLapSpl.set(self.this_lap_data[2])
        self.thisLapSpeed.set(self.this_lap_data[3])
        self.thisLapBrk1.set(self.this_lap_data[4])



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

GPIO.setmode(GPIO.BCM)
chan_list = [17,22,23,27]
GPIO.setup(chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(chan_list[0], GPIO.BOTH, callback = func1, bouncetime=300)
GPIO.add_event_detect(chan_list[1], GPIO.BOTH, callback = func2, bouncetime=300)
GPIO.add_event_detect(chan_list[2], GPIO.BOTH, callback = func3, bouncetime=300)
GPIO.add_event_detect(chan_list[3], GPIO.BOTH, callback = func4, bouncetime=300)
# run = True

app.mainloop()
