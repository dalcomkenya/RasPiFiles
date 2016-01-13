#import modules
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD 
import time

#assign the sensor and actuator gpio variables
#
#sensors
v_s = 16
m_s = 20
t_s = 21
#
#actuators
stb = 19
srn = 26

#initialize sensors as inputs with internal pulldown resistors
#the bridging voltage divider circuit will make use of 1.2k and 2.2k resistors
#the high resistance is to limit the current going into the circuit to below 50mA as specified for the pi
#
#vibration sensors
GPIO.setup(v_s, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#
#motion sensors
GPIO.setup(m_s, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#
#trap switches
GPIO.setup(t_s, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#
#

#initialize actuators as outputs. 
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
#file name formatting of the image
def get_file_name(): 
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")
#
#camera capture
def camera:
    fswebcam -r 1280x720 --no-banner image3.jpg
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
    
