import random
from flask import url_for
import serial

class Position():
	def to_dict(self):
		while True:
			ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
			ser.flush()
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
				'distance' : dis,
				'direction': ang
			}
			return data
