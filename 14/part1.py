
import os
from defragmenter import Defragmenter

f = open(os.path.join(os.path.dirname(__file__), '../input/14/part1.txt'), 'r')

def main():
    keyString = f.readline().rstrip()
    defragmenter = Defragmenter(keyString)
    count = defragmenter.getUsedSquareCount()
    print(count)

if __name__ == '__main__':
       main()
