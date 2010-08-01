
import serial
import tweetstream
import time
import json
import urllib2
import locale
from pprint import pprint

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

def rst(id):
  s = "\x0D\x0A"
  s += "<ID"
  if id<10:
    s += "0"
  s += ">"
  #print str
  

def oneline(id, txt):
  s = "\x0D\x0A"
  s += "<ID"
  if id<10:
    s += "0"
  s += str(id)
  s += ">"
  s += "<PA>"
  s += txt
  s += "\x0D\x0A"
  signfile.write(s)
  #print s
  
  
def tosign(id, topStyle, u, bottomStyle, b):
  s = "\x0D\x0A"
  s += "<ID"
  if id<10:
    s += "0"
  s += str(id)
  s += ">"
  s += "<PZ>"
  s += "<L1>"
  s += styles.get(topStyle)
  s += u
  s += "<L2>"
  s += styles.get(bottomStyle)
  s += b
  s += "\x0D\x0A"
  signfile.write(s)
  s += "<ID"
  if id<10:
    s += "0"
  s += str(id)
  s += ">"
  s += "<RPZ>"
  s += "\x0D\x0A"
  signfile.write(s)
  #print s

def formSign(sign, tweet):
  tosign(sign, "center", '@'+tweet['user']['screen_name'].upper(), "scroll_always", tweet['text'])

signfile = serial.Serial('/dev/ttyS0',baudrate=9600)


#tosign(73,"center","Hacker Dojo", "center", "Welcome");
oneline(73, "<FE>" + "Hacker Dojo")
