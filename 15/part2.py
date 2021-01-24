
from duelingGenerators import generatorAPart2, generatorBPart2
from judge import Judge

def main():
    judge = Judge()

    stop = 5000000
    genA = generatorAPart2(512, stop)
    genB = generatorBPart2(191, stop)

    for _ in range(stop):
        valueA = next(genA)
        valueB = next(genB)

        judge.compare(valueA, valueB)

    print(judge.getCount())

if __name__ == '__main__':
    main()
