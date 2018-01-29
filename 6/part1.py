import os

f = open(os.path.join(os.path.dirname(__file__), '../input/6/part1.txt'), 'r')


class MemoryHandler:

    def __init__(self, initialState):
        self.currentState = initialState
        self.previousStates = []

    def hasDuplicateState(self):
        if len(self.previousStates) < 1:
            return False

        hasDuplicate = False
        for state in self.previousStates:
            isEqual = True
            for idx, value in enumerate(state):
                if self.currentState[idx] != state[idx]:
                    isEqual = False
                    break
            if isEqual:
                hasDuplicate = True
                break

        return hasDuplicate


    def _findLargestIndex(self):
        largestValue = self.currentState[0]
        largestIndex = 0
        for idx in range(1, len(self.currentState)):
            if self.currentState[idx] > largestValue:
                largestIndex = idx
                largestValue = self.currentState[idx]
        return largestIndex


    def redistribute(self):
        self.previousStates.append(list(self.currentState))

        largestIndex = self._findLargestIndex()
        largestValue = self.currentState[largestIndex]

        self.currentState[largestIndex] = 0

        currentIndex = largestIndex
        currentValue = largestValue
        while currentValue > 0:
            currentIndex += 1
            if currentIndex >= len(self.currentState):
                currentIndex = 0
            self.currentState[currentIndex] += 1
            currentValue -= 1

    def run(self):
        while (self.hasDuplicateState() == False):
            self.redistribute()


def main():

    initialState = list(map(lambda value: int(value), f.readline().rstrip().split("\t")))
    memoryHandler = MemoryHandler(initialState)
    memoryHandler.run()
    print(len(memoryHandler.previousStates))


if __name__ == '__main__':
   main()
