#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)


x=0
i=0
print 'blink1'
while(True):
	GPIO.output(23,True)
	#time.sleep(1)
	for i in range(1,100):
		x=x+i
	x=0
	i=0
	GPIO.output(23,False)
	#time.sleep(1)
	for i in range(1,100):
		x=x+i
	x=0
	i=0
