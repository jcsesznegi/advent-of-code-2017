
from dance import Dance

def test_dance():
    d = Dance('abcde')

    d.dance([
        's1',
        'x3/4',
        'pe/b',
    ])

    assert d.getPrograms() == 'baedc'
