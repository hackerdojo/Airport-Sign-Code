#!/usr/local/bin/python

# This file is run by cron every minute
# Does a quick HTTP get every 15 seconds, three times

import urllib
import json
import sign
import time
import sys

def setup_signs(api):
  result = urllib.urlopen("http://signs.hackerdojo.com"+api)              
  rawdata = result.read()
  result.close()
  signs = json.loads(rawdata)
  for s in signs:
    msg = s['message']
    lines = msg.split("\r\n")
    if len(lines)==2:
      sign.twoLines(s['two_digit_id'], lines[0], lines[1])
    if len(lines)==1:
      sign.oneLine(s['two_digit_id'], lines[0])

if len(sys.argv)==2 and sys.argv[1] == "all":
  setup_signs("/api/all")
else:
  for i in range(1,3):                        
    setup_signs("/api")
    time.sleep(15)
