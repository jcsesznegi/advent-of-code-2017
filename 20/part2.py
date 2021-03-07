import os
import re
from pprint import pprint
from swarm import Swarm

f = open(os.path.join(os.path.dirname(__file__), '../input/20/part1.txt'), 'r')

def main():
    positions = []
    velocities = []
    accelerations = []

    line = f.readline()
    while line:
        m = re.search('p=<(.*)>, v=<(.*)>, a=<(.*)>', line.rstrip('\n'))
        pStrings = m.group(1).split(',')
        vStrings = m.group(2).split(',')
        aStrings = m.group(3).split(',')

        positions.append([int(pStrings[0]), int(pStrings[1]), int(pStrings[2])])
        velocities.append([int(vStrings[0]), int(vStrings[1]), int(vStrings[2])])
        accelerations.append([int(aStrings[0]), int(aStrings[1]), int(aStrings[2])])

        line = f.readline()

    s = Swarm(positions, velocities, accelerations)

    s.run(1000)

    print(s.getRemainingParticleCount())

if __name__ == '__main__':
    main()
