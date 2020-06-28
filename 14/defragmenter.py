
from knotHash import doKnotHash

class Defragmenter:
    def __init__(self, keyString):
        self.keyString = keyString
        self.grid = []
        self.initializeGrid()

    def getGrid(self):
        return self.grid

    def getUsedSquareCount(self):
        count = 0
        for row in self.grid:
            for square in list(row):
                if (square == '1'):
                    count += 1
        return count

    def initializeGrid(self):
        for idx in range(128):
            rowKeyString = '%s-%d' % (self.keyString, idx)
            rowLengths = [ord(character) for character in list(rowKeyString)] + [17, 31, 73, 47, 23]
            rowHexResult = doKnotHash(list(range(256)), rowLengths)
            rowBinaryResult = bin(int(rowHexResult, 16))[2:].zfill(128)
            self.grid.append(rowBinaryResult)
