#!/usr/bin/env python
# coding: utf8
from socket import *
#import RPi.GPIO as GPIO
import subprocess

SETUP = chr(0)
OUTPUT = chr(1)
PATTERN = chr(3)

PATTERN1=chr(4)
PATTERN2=chr(5)
PATTERN3=chr(6)
PATTERN4=chr(7)
PATTERN5=chr(8)

proc=0
pid=0

FLAG=False 

#GPIO.setmode(GPIO.BCM)

def gpio_setup(data):
    pin,dir = ord(data[0]),ord(data[1])
    #GPIO.setup(pin,dir)
    print "setup",pin,dir
    return 0

def gpio_output(data):
    pin,val = ord(data[0]),ord(data[1])
    #GPIO.output(pin,val)
    print "out",pin,val
    return 0

def set_pattern1(data):
    global proc
    global FLAG
    global pid
    patternval=ord(data[0])
    print patternval
    if(FLAG==True):
        print 'killing old guy'
        FLAG=False
	print proc
        proc.kill()
    else:     
        if patternval==4:
            FLAG=True
            print 'span pattern1'
            proc = subprocess.Popen(('./blink1.py'))
        elif patternval==5:
            FLAG=True
            print 'span pattern2'
            proc = subprocess.Popen(['./blink2.py'])
        elif patternval==6:
            FLAG=True
            print 'span pattern3'
           # proc = subprocess.Popen(['./script3.py'])
        elif patternval==7:
            FLAG=True
            print 'span pattern4'
            #proc = subprocess.Popen(['./script4.py'])
        elif patternval==8:
            FLAG=True
            print 'span pattern5'
           # proc = subprocess.Popen(['./script5.py'])
    return 0
    
if __name__=='__main__':
    HOST = 'localhost'
    PORT = 21567
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind(ADDR)
    serversock.listen(2)

    while 1:
        ret = None
        print 'waiting for connection...'
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        data = clientsock.recv(BUFSIZ)
        if data[0] == SETUP:
            print 'entering SETUP'
            ret = gpio_setup(data[1:])
        elif data[0] == OUTPUT:
            print 'entering OUTPUT'
            ret = gpio_output(data[1:])
        elif data[0]== PATTERN:
            print 'entering PATTENR'
            ret=set_pattern1(data[1:])
        
            
        if  ret:
            clientsock.send(ret)
            clientsock.close()
