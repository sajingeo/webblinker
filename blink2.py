#!/usr/bin/env python
# Pulsates an LED connected to GPIO pin 1 with a suitable resistor 4 times using softPwm
# softPwm uses a fixed frequency
import wiringpi2

OUTPUT = 1

PIN_TO_PWM = 7

wiringpi2.wiringPiSetup()
wiringpi2.pinMode(PIN_TO_PWM,OUTPUT)
wiringpi2.softPwmCreate(PIN_TO_PWM,0,100) # Setup PWM using Pin, Initial Value and Range parameters

while(True):
	#for brightness in range(0,100): # Going from 0 to 100 will give us full off to full on
	wiringpi2.softPwmWrite(PIN_TO_PWM,0) # Change PWM duty cycle
	wiringpi2.delay(20) # Delay for 0.2 seconds
	#for brightness in reversed(range(0,100)):
	wiringpi2.softPwmWrite(PIN_TO_PWM,100)
	wiringpi2.delay(20)
