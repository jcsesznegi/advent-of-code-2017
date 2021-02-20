import os
from tablet import Tablet

f = open(os.path.join(os.path.dirname(__file__), '../input/18/part1.txt'), 'r')

def main():
    instructionStrings = []
    line = f.readline()
    while line:
        instructionStrings.append(line.rstrip())
        line = f.readline()

    t = Tablet(instructionStrings)

    t.run()

    print(t.getFirstRecoveredFrequency())

if __name__ == '__main__':
    main()
