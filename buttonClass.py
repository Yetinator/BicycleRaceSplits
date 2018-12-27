import RPi.GPIO as GPIO
import time

class piButtons:
    #This should interface with whatever hard buttons exist on the raspberry pi
    def __init__(self, inButtons = ['a','b','c','d']):
        GPIO.setmode(GPIO.BCM)
        self.chan_list = [17,22,23,27]
        self.buttons = inButtons
        GPIO.setup(self.chan_list, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # def buttonRun(self, inButtons = [a,b,c,d]):
    #     #this should return the ailias of whatever button is pressed?
    #     #button 3 ends the button loop
    #     self.buttons = inButtons
    #     self.run = True
    #     while run:
    #         #input_state = GPIO.input(22)
    #     	button = False
    #     	for i in range(self.chan_list):
    #     		if GPIO.input(chan_list[i]) == False:
    #     			#print(str(i) + ' Button Pressed')
    #     			button = i
    #     			time.sleep(0.2)
    #     	if button == 0:
    #     		print("hey")
    #             return self.buttons[0]
    #
    #     	if button == 1:
    #     		print("you")
    #             self.buttons[1]
    #
    #     	if button == 2:
    #     		print("there")
    #             self.buttons[2]
    #
    #     	if button == 3:
    #     		print("guy")
    #             self.buttons[3]
    #     		self.buttonEnd()

        def get(self):
            button = False
        	for i in range(self.chan_list):
        		if GPIO.input(chan_list[i]) == False:
        			#print(str(i) + ' Button Pressed')
        			button = self.buttons[i]
            return button

        def buttonEnd(self):
            self.run = False
            GPIO.cleanup()
