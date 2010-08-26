#!/usr/local/bin/python

# Put a Twitter stream on a sign

import sign
import tweetstream
import time

words = ["tweet","oil","dojosign","hackerdojo","hacker dojo","#dojosign"]
last = 0
signs = ["40"]
with tweetstream.TrackStream("dojosign", "dojo77", words) as stream:
  for tweet in stream:
    if type(tweet['text']) is str:
      print tweet['user']['screen_name']+": "+tweet['text'] 
      print "\n"
      if True:
        formSign(signs[last], tweet)
	last = last + 1
	if last == count(signs):
	  last = 0
