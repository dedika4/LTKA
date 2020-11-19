import random

class positionData:
    def __init__(self):
        self.distance = 0
        self.direction = 0

    def getDistance(self):
        self.distance = random.randint(5,20)
        return

    def getDirection(self):
        self.direction = random.randint(0,360)
        return
