import serial

port = "COM3"
ser = serial.Serial(port, 9600, timeout = None)
print "Connected to", port

while True:
    line = ser.readline()
    print line
