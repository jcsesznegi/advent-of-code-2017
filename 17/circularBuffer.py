def getValueAfterZero(stepsPerInsert, insertTimes):
    bufferLength = 1
    currentIndex = 0
    currentPosition = 0
    valueAfterZero = None

    i = 0
    while i < insertTimes:
        j = 0
        while j < stepsPerInsert:
            currentIndex += 1
            if currentIndex >= bufferLength:
                currentIndex = 0
            j += 1
        if currentIndex == 0:
            valueAfterZero = currentPosition + 1
        currentIndex += 1
        currentPosition += 1
        bufferLength += 1

        i += 1

    return valueAfterZero

class CircularBuffer:
    def __init__(self, stepsPerInsert):
        self.buffer = [0]
        self.currentIndex = 0
        self.currentPosition = 0
        self.stepsPerInsert = stepsPerInsert

    def getCurrentPosition(self):
        return self.currentPosition

    def getBufferAsCSV(self):
        return ','.join(str(b) for b in self.buffer)

    def getNextIndex(self):
        nextIndex = self.currentIndex + 1
        if nextIndex >= len(self.buffer):
            return 0

        return nextIndex

    def getNextValue(self):
        return self.buffer[self.getNextIndex()]

    def stepForwardAndInsert(self):
        i = 0
        while i < self.stepsPerInsert:
            self.currentIndex = self.getNextIndex()
            i += 1

        self.currentPosition += 1
        self.buffer = (self.buffer[0:self.currentIndex + 1]
            + [self.currentPosition]
            + self.buffer[self.currentIndex + 1:])

        self.currentIndex = self.getNextIndex()

    def stepForwardAndInsertMultipleTimes(self, times):
        i = 0
        while i < times:
            self.stepForwardAndInsert()
            i += 1
