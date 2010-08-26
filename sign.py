
# Library file, use by multiple scripts

import serial

signfile = serial.Serial('/dev/cuau0', baudrate=9600)

def oneLine(id, txt):
  signfile.write("<ID" + str(id) + ">")
  signfile.write("<PA>")
  signfile.write("<FE>")
  signfile.write(txt)
  signfile.write("\r\n")
  signfile.write("<ID" + str(id) + ">")
  signfile.write("<RPA>")
  signfile.write("\r\n")

def twoLines(id, top_note, bottom_note):
  signfile.write("<ID" + str(id) + ">")
  signfile.write("<PA>")
  signfile.write("<FE>")
  signfile.write("<L1>")
  signfile.write(top_note)
  signfile.write("<L2>")
  signfile.write(bottom_note)
  signfile.write("\r\n")
  signfile.write("<ID" + str(id) + ">")
  signfile.write("<RPA>")
  signfile.write("\r\n")

