
import os

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

    return circle

def main():
    line = f.readline().rstrip()
    lengths = [int(lengthString) for lengthString in line.split(',')]
    circle = doHashRound(list(range(256)), lengths)

    print(circle[0] * circle[1])

if __name__ == '__main__':
       main()
