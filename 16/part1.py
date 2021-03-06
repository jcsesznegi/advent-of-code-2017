
import os
from dance import Dance

f = open(os.path.join(os.path.dirname(__file__), '../input/16/part1.txt'), 'r')

def main():
    line = f.readline().rstrip()
    d = Dance('abcdefghijklmnop')

    d.dance(line.split(','))

    print(d.getPrograms())

if __name__ == '__main__':
    main()
