import os

f = open(os.path.join(os.path.dirname(__file__), '../input/1/part1.txt'), 'r')


def main():
    inputString = f.read();
    inputList = list(inputString.rstrip());
    sum = 0;
    for idx, val in enumerate(inputList):
        if idx == (len(inputList) - 1):
            if inputList[idx] == inputList[0]:
                sum += int(inputList[idx])
        elif (inputList[idx] == inputList[idx + 1]):
            sum += int(inputList[idx])
    print(sum)

if __name__ == '__main__':
   main()
