import os

f = open(os.path.join(os.path.dirname(__file__), '../input/1/part2.txt'), 'r')


def main():
    inputString = f.read();
    inputList = list(inputString.rstrip());
    sum = 0;
    for idx, val in enumerate(inputList):
        idxComp = idx + len(inputList) // 2
        if idxComp >= len(inputList):
            idxComp -= len(inputList)
        if val == inputList[idxComp]:
            sum += int(val)
    print(sum)

if __name__ == '__main__':
   main()
