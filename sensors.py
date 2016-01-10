

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)


#import modules
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD 
import time

    import RPi.GPIO as GPIO           # import RPi.GPIO module  
     
      
     
    GPIO.output(port_or_pin, 1)       # set an output port/pin value to 1/HIGH/True  
    GPIO.output(port_or_pin, 0)       # set an output port/pin value to 0/LOW/False  
    i = GPIO.input(port_or_pin)       # read status of pin/port and assign to variable i  

#initialize sensors
#
#vibration sensors
GPIO.setup(port_or_pin, GPIO.IN)  # set a port/pin as an input
#
#motion sensors
GPIO.setup(port_or_pin, GPIO.IN)  # set a port/pin as an input
#
#trap switches
GPIO.setup(port_or_pin, GPIO.IN)  # set a port/pin as an input
#
#

#initialize actuators
#
#siren
GPIO.setup(port_or_pin, GPIO.OUT) # set a port/pin as an output  
#
#strobes
GPIO.setup(port_or_pin, GPIO.OUT) # set a port/pin as an output  


#initialize functions
#
#camera capture
#
#send image over

##loop
#
#if v.s and m.s and t.s are active, activate 
#
#if v.s and m.s are active
#
#if v.s and t.s are active
#
#if m.s and t.s are active
