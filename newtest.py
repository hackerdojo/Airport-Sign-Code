
import serial
import tweetstream
import time
import json
import urllib2
import locale
from pprint import pprint
from string import ascii_uppercase

styles = {
	"instant" : "<FB>",
	"scroll_bottom" : "<FC>",
	"in_place_right" : "<FD>",
	"from_center_h" : "<FE>",
	"from_center_v" : "<FF>",
	"scroll_always" : "<FH>",
	"invisible" : "<FM>",	
	"scroll_stuck" : "<FM>",
	"center" : "<FB>",
	"scroll_always" : "<FH>",	
	""	: "",
}

def oneline(cmd):
  s = ""
  s += "<ID30>"
  s += cmd
  s += "\x0D\x0A"
  
  s += "<ID30>"
  s += "" + cmd
  s += "\x0D\x0A"
  
  print s
  signfile.write(s)
  time.sleep(1)

def rst(cmd):
  s = ""
  s += "<ID73>" + cmd
  s += "\x0D\x0A"
  
  s += "<ID73>"
  s += "<PA><FE>" + cmd
  s += "Hello!"
  s += "\x0D\x0A"

  s += "<ID73><RPA>"
  s += "\x0D\x0A"
  
  print s
  signfile.write(s)


signfile = serial.Serial('/dev/ttyS0',baudrate=9600)

rst("");

for i in ascii_uppercase:
  for j in ascii_uppercase:
    oneline("<"+i+j+">Test "+i+j);
