import random
from flask import url_for

class Position():
	def to_dict(self):
		data = {
			'distance': random.randint(5,20),
			'direction': random.randint(0,360)
		}

		return data
