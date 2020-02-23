

import os

f = open(os.path.join(os.path.dirname(__file__), '../input/10/part1.txt'), 'r')

rangeSize = 256

def reverseLength(circle, currentPosition, length):
    global rangeSize
    endPosition = currentPosition + length - 1

    overSize = 0
    if (endPosition > rangeSize - 1):
        overSize = endPosition - rangeSize + 1

    currentValues = circle[currentPosition:endPosition - overSize + 1]
    if overSize:
        for index in range(overSize):
            currentValues.append(circle[index])

    reverseValues = currentValues[::-1]

    currentReverseIndex = 0
    for index in range(currentPosition, endPosition - overSize + 1):
        circle[index] = reverseValues[currentReverseIndex]
        currentReverseIndex = currentReverseIndex + 1

    for index in range(overSize):
        circle[index] = reverseValues[currentReverseIndex]
        currentReverseIndex = currentReverseIndex + 1

    return circle

def updateCurrentPosition(position, length, skip):
    global rangeSize
    position = position + length + skip

    if (position > rangeSize - 1):
        position = position - rangeSize

    return position

def main():

    circle = []
    for i in range(rangeSize):
         circle.append(i)

    line = f.readline().rstrip()

    lengths = []
    for lengthString in line.split(','):
        lengths.append(int(lengthString))

    currentPosition = 0
    skip = 0
    for length in lengths:
        circle = reverseLength(circle, currentPosition, length)
        currentPosition = updateCurrentPosition(currentPosition, length, skip)
        skip = skip + 1

    print(circle[0] * circle[1])

if __name__ == '__main__':
       main()
