import tkinter as tk
from tkinter import *
from tkinter import Tk
import tkinter.filedialog
# from tkinter import ttk


#this codebox represents a "baseline" future "StartPage" will be defined later
class FancyWatchApp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.grid(row=8, column=8)

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


        self.frames = {}

        #StartPage is a page we are about to make a class for
        for F in (StartPage, TimerPage, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0,  columnspan=8, rowspan=8,sticky="nsew")


        self.show_frame(StartPage)

    def show_frame(self, cont):
        #looking at the frames list at position cont
        for gone in self.frames:
            gone.grid_remove(self)
        frame = self.frames[cont]
        frame.tkraise()
        # frame.grid()


#startPage class from the codebox above

LARGE_FONT = ("Verdana" ,14)
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
GENERIC_X = 1
GENERIC_Y = 0
DATA_COLUMN = 2
#Grid will be 8 x 8
DATA_FONT = ("Verdana" ,8)
CLOCK_FONT = ("Verdana" ,14)
BUTTON_FONT = ("Verdana" ,14)



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

class TimerPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # label = tk.Label(self, text = "Timer_Page", font=LARGE_FONT)
        # label.grid(row=GENERIC_Y, column=GENERIC_X, columnspan=2, rowspan=2)

        #labels
        lapLabel = tk.Label(self, text = "Lap", font=DATA_FONT)
        lapLabel.grid(row=0, column=0,sticky="nsew")

        pelLabel = tk.Label(self, text = "Pel", font=DATA_FONT)
        pelLabel.grid(row=1, column=0,sticky="nsew")

        splLabel = tk.Label(self, text = "Spl", font=DATA_FONT)
        splLabel.grid(row=2, column=0,sticky="nsew")

        brkLabel = tk.Label(self, text = "Brk", font=DATA_FONT)
        brkLabel.grid(row=3, column=0,sticky="nsew")

        mphLabel = tk.Label(self, text = "MPH!", font=DATA_FONT)
        mphLabel.grid(row=4, column=0,sticky="nsew")

        clockLabel = tk.Label(self, text = "Time", font=DATA_FONT)
        clockLabel.grid(row=6, column=0,sticky="nsew")

        #Data
        lapData = tk.Label(self, text = "12", font=DATA_FONT)
        lapData.grid(row=0, column=DATA_COLUMN, columnspan = 2)

        pelData = tk.Label(self, text = "00:32:12.5", font=DATA_FONT)
        pelData.grid(row=1, column=DATA_COLUMN, columnspan = 2)

        splData = tk.Label(self, text = "03:22.3", font=DATA_FONT)
        splData.grid(row=2, column=DATA_COLUMN, columnspan = 2)

        brkData = tk.Label(self, text = "27.3/24.2/17.1", font=DATA_FONT)
        brkData.grid(row=3, column=DATA_COLUMN, columnspan = 2)

        mphData = tk.Label(self, text = "27.6", font=DATA_FONT)
        mphData.grid(row=4, column=DATA_COLUMN, columnspan = 2)


        # clockText = tk.Text(self)
        # clockText.grid(row=0, column=1, columnspan=3)
        # clockText.insert(INSERT, "00:00:00.0")
        clockText = tk.Label(self, text = "00:00:00.0", font=CLOCK_FONT, bg = 'cyan')
        clockText.grid(row=6, column=1, columnspan = 2)

        self.buttonMe()

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


app = FancyWatchApp()
app.geometry('320x240')

app.mainloop()
