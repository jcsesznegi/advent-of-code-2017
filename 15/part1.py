
from duelingGenerators import generatorA, generatorB
from judge import Judge

def main():
    judge = Judge()

    stop = 40000000
    genA = generatorA(512, stop)
    genB = generatorB(191, stop)

    for _ in range(stop):
        valueA = next(genA)
        valueB = next(genB)

        judge.compare(valueA, valueB)

    print(judge.getCount())

if __name__ == '__main__':
    main()
