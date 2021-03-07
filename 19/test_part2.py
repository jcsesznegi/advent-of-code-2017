

from network import Network

def test_traveled_steps():
    diagram = ([
        '     |          ',
		'     |  +--+    ',
		'     A  |  C    ',
		' F---|----E|--+ ',
		'     |  |  |  D ',
		'     +B-+  +--+ ',
    ])

    n = Network(diagram)

    n.run()

    assert n.getTraveledSteps() == 38
