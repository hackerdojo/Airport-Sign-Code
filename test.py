
import serial
import tweetstream
import time
import json
import urllib2
import locale
from pprint import pprint

def rst(id):
  signfile.write("<ID06>")
  signfile.write("<PA>Welcome to Hacker Dojo!")
  signfile.write("\x0D\x0A")
  
#signfile = serial.Serial('/dev/ttyS0',baudrate=9600)
signfile = serial.Serial('/dev/ttyUSB0',baudrate=9600)

rst(6);

print signfile.readline();
print signfile.readline();
