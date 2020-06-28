
from knotHash import doKnotHash
from defragmenter import Defragmenter

def test_knot_hash_1():
    lengths = [ord(character) for character in list('')] + [17, 31, 73, 47, 23]
    result = doKnotHash(list(range(256)), lengths)
    assert result == 'a2582a3a0e66e6e86e3812dcb672a272'

def test_knot_hash_2():
    lengths = [ord(character) for character in list('AoC 2017')] + [17, 31, 73, 47, 23]
    result = doKnotHash(list(range(256)), lengths)
    assert result == '33efeb34ea91902bb2f59c9920caa6cd'

def test_knot_hash_3():
    lengths = [ord(character) for character in list('1,2,3')] + [17, 31, 73, 47, 23]
    result = doKnotHash(list(range(256)), lengths)
    assert result == '3efbe78a8d82f29979031a4aa0b16a9d'

def test_hexadecimal_to_binary_string():
    hexResult = 'a0c20170000000000000000000000000'
    binaryResult = bin(int(hexResult, 16))[2:].zfill(128)
    assert binaryResult.startswith('10100000110000100000000101110000')

def test_defragmenter():
    defragmenter = Defragmenter('flqrgnkx')
    grid = defragmenter.getGrid()
    assert grid[0].startswith('11010100')
    assert grid[1].startswith('01010101')
    assert grid[3].startswith('10101101')
    assert grid[5].startswith('11001001')
