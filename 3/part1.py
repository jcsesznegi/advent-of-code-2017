import os
from math import sqrt, ceil

f = open(os.path.join(os.path.dirname(__file__), '../input/3/part1.txt'), 'r')

class SpiralMap:

    def __init__(self, maxValue):
        self.maxValue = int(maxValue)
        self.width = 0
        self.map = []

        self.centerIndex = 0
        self.centerPoint = (0, 0) 
        self.currentPoint = (0, 0) 

        self.currentValue = 1
        self.currentDirection = 0 # 0:E, 1:N, 2:W, 3:S  

        self.__init()


    def __createRow(self):
        return [None] * self.width

    def __createEmptyMap(self):
        self.map = list(map(lambda row: self.__createRow(), self.__createRow()))

    def __getPointUp(self, point):
        return (
            point[0],
            point[1] - 1
        )

    def __getPointDown(self, point):
        return (
            point[0],
            point[1] + 1
        )

    def __getPointLeft(self, point):
        return (
            point[0] - 1,
            point[1]
        )

    def __getPointRight(self, point):
        return (
            point[0] + 1,
            point[1]
        )

    def __travel(self):

        if self.currentDirection == 0:
            nextPoint = self.__getPointRight(self.currentPoint)
            leftPoint = self.__getPointUp(nextPoint)
        elif self.currentDirection == 1:
            nextPoint = self.__getPointUp(self.currentPoint)
            leftPoint = self.__getPointLeft(nextPoint)
        elif self.currentDirection == 2:
            nextPoint = self.__getPointLeft(self.currentPoint)
            leftPoint = self.__getPointDown(nextPoint)
        elif self.currentDirection == 3:
            nextPoint = self.__getPointDown(self.currentPoint)
            leftPoint = self.__getPointRight(nextPoint)

        nextValue = self.currentValue + 1
        self.map[nextPoint[0]][nextPoint[1]] = nextValue 
         
        if self.map[leftPoint[0]][leftPoint[1]] == None:
            if self.currentDirection == 3:
                self.currentDirection = 0
            else:
                self.currentDirection += 1

        self.currentPoint = nextPoint
        return nextValue

    def __init(self):
        self.width = ceil(sqrt(self.maxValue)) 
        self.__createEmptyMap()

        self.centerIndex = ceil(self.width / 2) - 1
        self.currentPoint = self.centerPoint = (self.centerIndex, self.centerIndex)

        self.map[self.centerPoint[0]][self.centerPoint[1]] = self.currentValue

        while self.currentValue < self.maxValue:
            self.currentValue = self.__travel()

    def getDistanceLastToCenterPoint (self):
        distanceX = abs(self.currentPoint[0] - self.centerPoint[0])
        distanceY = abs(self.currentPoint[1] - self.centerPoint[1])
        return distanceX + distanceY


def main():
    maxValue = f.read().rstrip()

    s = SpiralMap(maxValue)
    print(s.getDistanceLastToCenterPoint()) 

if __name__ == '__main__':
   main()
