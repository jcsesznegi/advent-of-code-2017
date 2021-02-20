import os, queue
from tablet import Tablet

f = open(os.path.join(os.path.dirname(__file__), '../input/18/part1.txt'), 'r')

def main():
    instructionStrings = []
    line = f.readline()
    while line:
        instructionStrings.append(line.rstrip())
        line = f.readline()

    q0 = queue.Queue()
    q1 = queue.Queue()

    t0 = Tablet(instructionStrings, 0, q0, q1)
    t1 = Tablet(instructionStrings, 1, q1, q0)

    isDeadlock = False
    while not isDeadlock:
        t0.run()
        t1.run()

        if t0.isWaiting() and t1.isWaiting():
            isDeadlock = True

    print(t1.getTimesSent())

if __name__ == '__main__':
    main()
