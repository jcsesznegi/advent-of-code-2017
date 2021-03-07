import os
from network import Network

f = open(os.path.join(os.path.dirname(__file__), '../input/19/part1.txt'), 'r')

def main():
    diagramStrings = []
    line = f.readline()
    while line:
        diagramStrings.append(line.rstrip('\n'))
        line = f.readline()

    n = Network(diagramStrings)

    n.run()

    print(n.getTraveledSteps())

if __name__ == '__main__':
    main()
