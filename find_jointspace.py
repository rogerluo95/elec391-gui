import sys
import serial
from os import path


text_file = open("Joint_Position"+".txt","w")
port = "COM6"
ser = serial.Serial(port, 9600, timeout = None)
print "Connected to", port

while True:
    line = ser.readline()
    if len(line) > 0 :
        msg_list = [None]*5
        msg_list = str(line).split(',') # Split the output of Arduino
    if "0" or "1" or "2" or "3" not in message_list[0]:
        for item in msg_list:
            text_file.write("%s " %item)
    print msg_list
