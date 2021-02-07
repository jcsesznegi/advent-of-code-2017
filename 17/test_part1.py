

from circularBuffer import CircularBuffer

def test_step_forward_and_insert_1():
    c = CircularBuffer(3)
    c.stepForwardAndInsert()

    assert c.getBufferAsCSV() == '0,1'

    assert c.getCurrentPosition() == 1

def test_step_forward_and_insert_2():
    c = CircularBuffer(3)
    c.stepForwardAndInsertMultipleTimes(2)

    assert c.getBufferAsCSV() == '0,2,1'

    assert c.getCurrentPosition() == 2

def test_step_forward_and_insert_3():
    c = CircularBuffer(3)
    c.stepForwardAndInsertMultipleTimes(3)

    assert c.getBufferAsCSV() == '0,2,3,1'

    assert c.getCurrentPosition() == 3

def test_step_forward_and_insert_2017():
    c = CircularBuffer(3)
    c.stepForwardAndInsertMultipleTimes(2017)

    assert c.getNextValue() == 638
