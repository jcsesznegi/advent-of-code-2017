
def generatorA(value, stop):
    i = 0
    while i < stop:
        value = (value * 16807) % 2147483647
        yield value
        i += 1

def generatorB(value, stop):
    i = 0
    while i < stop:
        value = (value * 48271) % 2147483647
        yield value
        i += 1

def generatorAPart2(value, stop):
    i = 0
    while i < stop:
        value = (value * 16807) % 2147483647
        while value % 4 != 0:
            value = (value * 16807) % 2147483647
        yield value
        i += 1

def generatorBPart2(value, stop):
    i = 0
    while i < stop:
        value = (value * 48271) % 2147483647
        while value % 8 != 0:
            value = (value * 48271) % 2147483647
        yield value
        i += 1
