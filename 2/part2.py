import os

f = open(os.path.join(os.path.dirname(__file__), '../input/2/part2.txt'), 'r')


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
        for idx, val in enumerate(row):
            for idx2, val2 in enumerate(row):
                if (
                    idx != idx2
                    and val <= (val2 / 2)
                    and val2 % val == 0
                ):
                    sum += val2 // val
    print(sum)

if __name__ == '__main__':
   main()
