import os

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

    isCaught = True
    delay = 1
    while isCaught == True:
        currentDepth = 0
        for index, depth in enumerate(depths):
            currentTime = delay + depth
            if currentTime % ((ranges[index] - 1) * 2) == 0:
                break
            else:
                currentDepth += 1
        if currentDepth == len(depths):
            isCaught = False
        else:
            delay += 1
    print(delay)

if __name__ == '__main__':
    main()
