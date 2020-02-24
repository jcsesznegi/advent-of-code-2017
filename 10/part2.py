
import os
from functools import reduce

f = open(os.path.join(os.path.dirname(__file__), '../input/10/part1.txt'), 'r')


def reverseLength(circle, position, length):
    if (position + length < len(circle)):
        before = circle[:position]
        middle = circle[position:position + length]
        after = circle[position + length:]

        return before + middle[::-1] + after
    else:
        before = circle[:position]
        rest = circle[position:]
        overSize = (position + length) % len(circle) 
        valuesToReverse = rest + before[:overSize]
        reverseValues = valuesToReverse[::-1]

        return reverseValues[-overSize:] + before[overSize:] + reverseValues[:-overSize]

def doHashRound(circle, lengths, position=0, skip=0):
    for length in lengths:
        circle = reverseLength(circle, position, length)

        position = position + length + skip
        if (position >= len(circle)):
            position = position % len(circle)
        
        skip = skip + 1

    return circle, position, skip

def doKnotHash(circle, lengths):
    position = 0
    skip = 0
    for _ in range(64):
        result = doHashRound(circle, lengths, position, skip)
        circle = result[0]
        position = result[1]
        skip = result[2]

    groups = [circle[i:i + 16] for i in range(0, len(circle), 16)]
    xorGroups = [reduce(lambda i, j: i ^ j, group) for group in groups]
    print(xorGroups)
    hexValues = [format(value, '02x') for value in xorGroups]
    print(hexValues)
    return ''.join(hexValues)

def main():
    line = f.readline().rstrip()
    line = '1,2,3'
    lengths = [ord(character) for character in list(line)] + [17, 31, 73, 47, 23]
    result = doKnotHash(list(range(256)), lengths)

    print(result)

if __name__ == '__main__':
       main()
