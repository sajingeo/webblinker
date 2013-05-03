#!/usr/bin/env python
# coding: utf8

from socket import *
import struct

SETUP_CMD = chr(0)
OUTPUT_CMD = chr(1)
PATTERN_CMD= chr(3)
OUTPUT = chr(0)
INPUT = chr(1)

ON = chr(1)
OFF = chr(0)

def send(data):
     sock = socket(AF_INET,SOCK_STREAM)
     sock.connect(('localhost',21567))
     sock.send(data)
    
def setup(pin,dir):
    data = struct.pack("ccc",SETUP_CMD,chr(pin),dir)
    send(data)
    
def output(pin,val):
    data = struct.pack("ccc",OUTPUT_CMD,chr(pin),val)
    send(data)

def pattern(data):
    data = struct.pack("cc",PATTERN_CMD,chr(data))
    send(data)
