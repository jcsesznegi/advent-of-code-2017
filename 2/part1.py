import os

f = open(os.path.join(os.path.dirname(__file__), '../input/2/part1.txt'), 'r')


def main():
    line = f.readline();
    inputList = []
    while line:
        inputList.append(line)
        line = f.readline();

    def formatItems(row):
        return sorted(list(map(lambda item: int(item), row.split('\t'))))

    inputList = list(map(lambda row: formatItems(row), inputList))
        
    sum = 0;
    for row in inputList:
        sum += row[len(row) - 1] - row[0]

    print(sum)

if __name__ == '__main__':
   main()
