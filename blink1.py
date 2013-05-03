#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)

#print 'blink2'
while(True):
	GPIO.output(23,True)
	time.sleep(2)
	GPIO.output(23,False)
	time.sleep(3)

