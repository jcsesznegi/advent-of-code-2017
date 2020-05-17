
import os
from firewall import Firewall

f = open(os.path.join(os.path.dirname(__file__), '../input/13/part1.txt'), 'r')

def main():
    depths = []
    ranges = []
    line = f.readline().rstrip()
    while line:
        parts = line.split(': ')
        depths.append(int(parts[0]))
        ranges.append(int(parts[1]))
        line = f.readline().rstrip()

    firewall = Firewall(depths, ranges)
    firewall.run()
    print(firewall.totalSeverity)

if __name__ == '__main__':
       main()
