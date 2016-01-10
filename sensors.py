#import modules
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD 
import time

#variables
#
#sensors
v_s = 
m_s = 
t_s = 
#
#actuators
stb = 
srn = 

#initialize sensors
#
#vibration sensors
GPIO.setup(v_s, GPIO.IN)  # set a port/pin as an input
#
#motion sensors
GPIO.setup(m_s, GPIO.IN)  # set a port/pin as an input
#
#trap switches
GPIO.setup(t_s, GPIO.IN)  # set a port/pin as an input
#
#

#initialize actuators
#
#siren
GPIO.setup(srn, GPIO.OUT) # set a port/pin as an output  
#
#strobes
GPIO.setup(stb, GPIO.OUT) # set a port/pin as an output  


#initialize functions
#
#activate actuators
def actuatorsOn:
    GPIO.output(stb, 1) and GPIO.output(srn, 1)
#
#deactivate actuators
def actuatorsOn:
    GPIO.output(stb, 0) and GPIO.output(srn, 0)
#
#camera capture
def camera:
#
#send image over
def sendImages:

##loop
#
try:
    while True:
        #if v.s and m.s and t.s are active, activate 
        if GPIO.input(v_s) and GPIO.input(m_s) and GPIO.input(t_s): # if port 25 == 1 
            actuatorsOn
            camera
            sendImages
        #
        #if v.s and m.s are active
        if GPIO.input(v_s) and GPIO.input(m_s): # if port 25 == 1 
            actuatorsOn
            camera
            sendImages
        #
        #if v.s and t.s are active
        if GPIO.input(v_s) and GPIO.input(t_s): # if port 25 == 1 
            actuatorsOn
            camera
            sendImages
        #
        #if m.s and t.s are active
        if GPIO.input(m_s) and GPIO.input(t_s): # if port 25 == 1 
            actuatorsOn
            camera
            sendImages 
            
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup()         # clean up after yourself  
    
