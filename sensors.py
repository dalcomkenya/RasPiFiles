import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)


#import modules

#initialize sensors
#
#vibration sensors
#
#motion sensors
#
#trap switches
#
#

#initialize actuators
#
#siren
#
#strobes

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
