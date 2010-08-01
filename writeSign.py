import serial
import tweetstream
import time

styles = {
	"scroll_stuck" : "<FM>",
	"center" : "<FB>",
	"scroll_always" : "<FH>",
}

def tosign(id, topStyle, u, bottomStyle, s):
	signfile.write("\x0D\x0A\x0A")
	signfile.write("  <ID"+str(id)+"><PZ>")
	signfile.write(styles.get(topStyle))
	signfile.write("<L1>")
	signfile.write(u)
	signfile.write("<L2>"+s)
	signfile.write(styles.get(bottomStyle))
	signfile.write("\x0D\x0A")
	signfile.write("  ")
	signfile.write("<ID"+str(id)+"><RPZ>")
	signfile.write("\x0D\x0A")
	signfile.write("  <ID00><L1>")
	signfile.write("\x0D\x0A")
	signfile.write("  <ID00><RPZ>")
	time.sleep(0.1)
	signfile.write("\x0C")

def formSign(sign, tweet):
  tosign(sign, "center", '@'+tweet['user']['screen_name'].upper(), "scroll_always", tweet['text'])

signfile = serial.Serial('/dev/ttyS0',baudrate=9600)
tosign(30, "center", "", "center", "Please tweet at me!")
tosign(40,"center", "", "center", "")
tosign(73,"center", "", "center", "")
words = ["tweet","oil","dojosign","hackerdojo","hacker dojo","#dojosign"]
last = 0
signs = [30,40,73]
with tweetstream.TrackStream("dojosign", "dojo77", words) as stream:
  for tweet in stream:
    if type(tweet['text']) is str:
      print tweet['user']['screen_name']+": "+tweet['text'] 
      print "\n"
      if "t" in tweet['text']:
        formSign(signs[last], tweet)
	last = last + 1
	if last == 3:
	  last = 0

signfile.close()



