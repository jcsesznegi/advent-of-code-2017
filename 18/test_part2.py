
import queue
from tablet import Tablet

def test_how_many_times_sent():
    instructionStrings = ([
        'snd 1',
        'snd 2',
        'snd p',
        'rcv a',
        'rcv b',
        'rcv c',
        'rcv d',
    ])

    q0 = queue.Queue()
    q1 = queue.Queue()

    t0 = Tablet(instructionStrings, 0, q0, q1)
    t1 = Tablet(instructionStrings, 1, q1, q0)

    isDeadlock = False
    while not isDeadlock:
        processedCount0 = t0.run()
        processedCount1 = t1.run()

        if processedCount0 == 0 and processedCount1 == 0:
            isDeadlock = True

    assert t1.getTimesSent() == 3
