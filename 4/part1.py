import os

f = open(os.path.join(os.path.dirname(__file__), '../input/4/part1.txt'), 'r')


def main():
    line = f.readline()
    inputList = []
    while line:
        inputList.append(line)
        line = f.readline()
        
    totalValid = 0
    for row in inputList:
        passPhrase = row.rstrip().split(" ")
        uniqueWords = set(passPhrase)
        if (len(passPhrase) == len(uniqueWords)): 
            totalValid += 1

    print(totalValid)

if __name__ == '__main__':
   main()
