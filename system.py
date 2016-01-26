#		IMPORT LIBRARIES
########################################
import RPi.GPIO as GPIO
import time
import os

#		VARIABLES
########################################
##
##	vibration sensors
########################################
v_s_1 = 6
v_s_2 = 13
v_s_3 = 19
v_s_4 = 26
##
##	trap loops
########################################
t_l_1 = 10
t_l_2 = 9
t_l_3 = 11
t_l_4 = 5
##
##	actuators
########################################
stb = 27
srn = 17
##
##	sensor power
########################################
sns = 



#		FUNCTIONS
########################################
##
##		take image with time-stamp
def take_image():
	os.system('fswebcam -r 500x300 --jpg --save /home/pi/media/%Y-%m-%d-%H:%M.jpg')
##
##		sensor interrupt callback
def sensor_callback(channel):
	actuators_on()
	send_alert()
##
##		turn actuators on
def actuators_on():
	GPIO.output(stb, 0)
	GPIO.output(srn, 0)
##
##		turn actuators off
def actuators_on():
	GPIO.output(stb, 1)
	GPIO.output(srn, 1)
##
##
def store_to_file():
	filename = '%Y-%m-%d-%H:%M.txt'
	sensors = open(filename, 'w')
	sensors.write('pylonID')		##to be updated with actual pylon ID
	sensors.write('\n')
	sensors.write('vibration=1')
	sensors.write('\n')
	sensors.write('traps=1')
	sensors.close()
##
##		send via https
def send_alert():


#		SETUP
########################################
##
GPIO.setmode(GPIO.BCM)
##
##		vibration sensors
GPIO.setup(v_s_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(v_s_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(v_s_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(v_s_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
##
##		trap loop
GPIO.setup(t_l_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(t_l_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(t_l_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(t_l_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
##
##		actuators
###	the initial value is set to 1 cos we are working with active low o/p hence being low
GPIO.setup(stb, GPIO.OUT, initial=1)
GPIO.setup(srn, GPIO.OUT, initial=1)
##
##		sensor power
###	the initial value is set to high (active low remember)
GPIO.setup(sns, GPIO.OUT, initial=0)



#		INTERRUPT CALLS
########################################
##
##		vibration sensor interrupts
GPIO.add_event_detect(v_s_1, GPIO.FALLING, callback=sensor_callback)
GPIO.add_event_detect(v_s_2, GPIO.FALLING, callback=sensor_callback)
GPIO.add_event_detect(v_s_3, GPIO.FALLING, callback=sensor_callback)
GPIO.add_event_detect(v_s_4, GPIO.FALLING, callback=sensor_callback)
##
##		vibration sensor interrupts
GPIO.add_event_detect(t_l_1, GPIO.FALLING, callback=sensor_callback)
GPIO.add_event_detect(t_l_2, GPIO.FALLING, callback=sensor_callback)
GPIO.add_event_detect(t_l_3, GPIO.FALLING, callback=sensor_callback)
GPIO.add_event_detect(t_l_4, GPIO.FALLING, callback=sensor_callback)

#		LOOP
########################################
try:
	while True:
		##no loop here for now
		##running on full interupts
finally:
	GPIO.cleanup()
