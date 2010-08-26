#!/usr/local/bin/python

# Pledgie

import urllib2
import json
import sign
import locale

usock = urllib2.urlopen("http://pledgie.com/campaigns/10602.json")
data = usock.read()
usock.close()
pledgie = json.loads(data)

amount = pledgie['campaign']['amount_raised']
pledges = pledgie['campaign']['pledges_count']
percent = pledgie['campaign']['percent_towards_goal']
pledge_guy = pledgie['campaign']['pledges'][-1]['display_name']
 
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )
parsedAmount = str(locale.currency(amount,grouping=True))[:-3]

sign.twoLines("96", "Last donation:", str(pledge_guy))
sign.oneLine("97", parsedAmount)
sign.twoLines("98", " %.1f%%" % percent + " of $35,000", "THANK YOU!  If you can, please donate at hackerdojo.com to help us get heat & air conditioning!")

