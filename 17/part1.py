
from circularBuffer import CircularBuffer

def main():
    c = CircularBuffer(328)

    c.stepForwardAndInsertMultipleTimes(2017)

    print(c.getNextValue())

if __name__ == '__main__':
    main()
