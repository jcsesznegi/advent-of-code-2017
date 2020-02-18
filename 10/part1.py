

import os

f = open(os.path.join(os.path.dirname(__file__), '../input/10/part1.txt'), 'r')

rangeSize = 256
circle = []
for i in range(rangeSize):
    circle.append(i)

currentPosition = 0
lengths = []
skip = 0

def reverseLength(length):
    endPosition = currentPosition + length

    overSize = 0
    if (endPosition > rangeSize - 1):
        overSize = endPosition - rangeSize - 1

    currentValues = circle[currentPosition:endPosition - overSize]
    if overSize:
        for index in range(overSize):
            currentValues.append(circle[index])

    reverseValues = currentValues.reverse()

    for index in range(currentPosition, endPosition - overSize):
        circle[index] = reverseValues[index - currentPosition]
    
    for index in range(overSize):
        circle[index] = reverseValues[endPosition + index +1]

def updateCurrentPosition():
    currentPosition += skip

    if (currentPosition > rangeSize - 1):
        currentPosition -= rangeSize

def main():

    line = f.readline().rstrip()

    for lengthString in line.split(','):
        lengths.append(int(lengthString))

    for length in lengths:
        reverseLength(length)
        updateCurrentPosition()
        skip += 1

    print(circle[0] * circle[1])

if __name__ == '__main__':
       main()
