#!/usr/bin/env python3
import serial
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            line = line.split(',')
            if(line[0]!=''):
              ang = float(line[0])
            else:
              ang = 0
            if(len(line)>1):
             if(line[1] != ''):
              dis = float(line[1])
             else:
              dis = 0
            else:
              dis = 0
            data = {
                 'distance': dis,
                 'direction' :ang
            }
            print(data)

