
from tkinter import *
import tkinter.filedialog
import time
from array import *
from writeClass import *
from windowClass import AbstractWindow
from windowClass import MyWindow
from windowClass import MyWindowTimer
from stopWatchClass import Watch
from stopWatchClass import SwissWatch


# def start_timer(clock):
#     clock.start_timer()

def foo():
    tempWindow.update_time_stamp(a_clock.get_t_time())
    tempWindow.update_idletasks()
    tempWindow.update()

def swissAlps():
    tempWindow.update_time_stamp(swiss_clock.bazinga())
    tempWindow.update()

def swissLoop():
    tempWindow.looptie_loop(swiss_clock)


run = True
swiss_clock = SwissWatch()
tempWindow = MyWindowTimer()
# tempWindow2 =Tk()
# a_clock = Watch(tempWindow)
# a_clock.start()
# for i in range(1000):
#
#     tempWindow.update_time_stamp(a_clock.get_t_time())
# a_clock.start_timer()
# print(help(tempWindow))
# swissLoop()
mainloop()
#
# while(run == True):
#     swissAlps()

# tempWindow.after(1, swissAlps)
# tempWindow.mainloop()
# while(run == True):
#     tempWindow.update_time_stamp("what")
#     # a_clock.get_t_time())
#     tempWindow.update()
