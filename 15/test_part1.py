
from duelingGenerators import generatorA, generatorB, generatorAPart2, generatorBPart2
from judge import getBinaryString, Judge

def test_generator_a():
    g = generatorA(65, 5)
    assert next(g) == 1092455
    assert next(g) == 1181022009
    assert next(g) == 245556042
    assert next(g) == 1744312007
    assert next(g) == 1352636452

def test_generator_b():
    g = generatorB(8921, 5)
    assert next(g) == 430625591
    assert next(g) == 1233683848
    assert next(g) == 1431495498
    assert next(g) == 137874439
    assert next(g) == 285222916

def test_get_binary_string():
    assert getBinaryString(1092455) == '00000000000100001010101101100111'
    assert getBinaryString(430625591) == '00011001101010101101001100110111'

    assert getBinaryString(1181022009) == '01000110011001001111011100111001'
    assert getBinaryString(1233683848) == '01001001100010001000010110001000'

def test_judge():
    judge = Judge()

    stop = 5
    genA = generatorA(65, stop)
    genB = generatorB(8921, stop)

    for _ in range(stop):
        valueA = next(genA)
        valueB = next(genB)

        judge.compare(valueA, valueB)

    assert judge.getCount() == 1

def test_judge_part2():
    judge = Judge()

    stop = 5000000
    genA = generatorAPart2(65, stop)
    genB = generatorBPart2(8921, stop)

    for _ in range(stop):
        valueA = next(genA)
        valueB = next(genB)

        judge.compare(valueA, valueB)

    assert judge.getCount() == 309
