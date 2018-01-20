import os
from math import sqrt, ceil

f = open(os.path.join(os.path.dirname(__file__), '../input/3/part1.txt'), 'r')

class SpiralMap:

    def __init__(self, maxValue):
        self.maxValue = int(maxValue)
        self.width = 0
        self.height = 0
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
        if ((point[1] - 1) < 0): 
            return None
        return (
            point[0],
            point[1] - 1
        )

    def __getPointUpLeft(self, point):
        if ((point[0] - 1) < 0
            or (point[1] - 1) < 0): 
            return None
        return (
            point[0] - 1,
            point[1] - 1
        )

    def __getPointUpRight(self, point):
        if ((point[0] + 1) >= self.width
            or (point[1] - 1) < 0): 
            return None
        return (
            point[0] + 1,
            point[1] - 1
        )

    def __getPointDown(self, point):
        if ((point[1] + 1) >= self.height): 
            return None
        return (
            point[0],
            point[1] + 1
        )

    def __getPointDownLeft(self, point):
        if ((point[0] - 1) < 0
            or (point[1] + 1) >= self.height): 
            return None
        return (
            point[0] - 1,
            point[1] + 1
        )

    def __getPointDownRight(self, point):
        if ((point[0] + 1) >= self.width
            or (point[1] + 1) >= self.height): 
            return None
        return (
            point[0] + 1,
            point[1] + 1
        )

    def __getPointLeft(self, point):
        if ((point[0] - 1) < 0): 
            return None
        return (
            point[0] - 1,
            point[1]
        )

    def __getPointRight(self, point):
        if ((point[0] + 1) >= self.width): 
            return None
        return (
            point[0] + 1,
            point[1]
        )

    def __getPointValue(self, point):
        if (point == None):
            return None
        return self.map[point[0]][point[1]]

    def __getNextValue(self, nextPoint):
        points = [
            nextPoint,
            self.__getPointUp(nextPoint),
            self.__getPointUpLeft(nextPoint),
            self.__getPointUpRight(nextPoint),
            self.__getPointDown(nextPoint),
            self.__getPointDownLeft(nextPoint),
            self.__getPointDownRight(nextPoint),
            self.__getPointLeft(nextPoint),
            self.__getPointRight(nextPoint)
        ]
        total = 0
        for point in points:
            if point and self.__getPointValue(point):
                total += self.__getPointValue(point);
        return total

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

        nextValue = self.__getNextValue(nextPoint)
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
        self.height = self.width 
        self.__createEmptyMap()

        self.centerIndex = ceil(self.width / 2) - 1
        self.currentPoint = self.centerPoint = (self.centerIndex, self.centerIndex)

        self.map[self.centerPoint[0]][self.centerPoint[1]] = self.currentValue

        while self.currentValue <= self.maxValue:
            self.currentValue = self.__travel()

    def getDistanceLastToCenterPoint (self):
        distanceX = abs(self.currentPoint[0] - self.centerPoint[0])
        distanceY = abs(self.currentPoint[1] - self.centerPoint[1])
        return distanceX + distanceY


def main():
    maxValue = f.read().rstrip()

    s = SpiralMap(maxValue)
    print(s.currentValue) 

if __name__ == '__main__':
   main()
