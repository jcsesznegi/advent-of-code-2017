

from network import Network

def test_traveled_route():
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

    assert n.getTraveledRoute() == 'ABCDEF'
