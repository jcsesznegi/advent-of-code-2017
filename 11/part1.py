
import os

f = open(os.path.join(os.path.dirname(__file__), '../input/11/part1.txt'), 'r')


class HexGrid:

    def __init__(self, start=(0,0)):
        self.start = start
        self.currentPosition = start

    def setCurrentPosition(self, offset):
        self.currentPosition = (self.currentPosition[0] + offset[0], self.currentPosition[1] + offset[1])

    def move(self, direction):
        offset = (0, 0)
        if direction == 'n':
            offset = (-1, 0)
        elif direction == 'ne':
            if self.currentPosition[1] % 2:
                offset = (-1, 1)
            else:
                offset = (0, 1)
        elif direction == 'se':
            if self.currentPosition[1] % 2:
                offset = (0, 1)
            else:
                offset = (1, 1)
        if direction == 's':
            offset = (1, 0)
        elif direction == 'sw':
            if self.currentPosition[1] % 2:
                offset = (0, -1)
            else:
                offset = (1, -1)
        elif direction == 'nw':
            if self.currentPosition[1] % 2:
                offset = (-1, -1)
            else:
                offset = (0, -1)

        self.setCurrentPosition(offset) 

    def distanceToStart(self):
        y1, x1 = self.start
        y2, x2 = self.currentPosition
        du = x2 - x1
        dv = (y2 + x2 // 2) - (y1 + x1 // 2)
        
        return max(abs(du), abs(dv)) if ((du >= 0 and dv >= 0) or (du < 0 and dv < 0)) else abs(du) + abs(dv)

def main():

    line = f.readline().rstrip()
    moveList = line.split(',')
    hexGrid = HexGrid()

    for direction in moveList:
        hexGrid.move(direction)

    print(hexGrid.start)
    print(hexGrid.currentPosition)
    print(hexGrid.distanceToStart())


if __name__ == '__main__':
   main()
