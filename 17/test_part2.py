

from circularBuffer import getValueAfterZero

def test_get_value_after_zero():
    stepsPerInsert = 3

    valueAfterZero = getValueAfterZero(stepsPerInsert, 0)
    assert valueAfterZero == None

    valueAfterZero = getValueAfterZero(stepsPerInsert, 1)
    assert valueAfterZero == 1

    valueAfterZero = getValueAfterZero(stepsPerInsert, 2)
    assert valueAfterZero == 2

    valueAfterZero = getValueAfterZero(stepsPerInsert, 5)
    assert valueAfterZero == 5

    valueAfterZero = getValueAfterZero(stepsPerInsert, 9)
    assert valueAfterZero == 90
