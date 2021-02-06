
from dance import Dance

def test_dance_multiple_times():
    d = Dance('abcde')

    d.danceMultipleTimes([
        's1',
        'x3/4',
        'pe/b',
    ], 2)

    assert d.getPrograms() == 'ceadb'
