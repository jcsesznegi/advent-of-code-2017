
def getBinaryString(n):
    return '{:032b}'.format(n)

class Judge:
    def __init__(self):
        self.count = 0

    def getCount(self):
        return self.count

    def compare(self, valueA, valueB):
        valueAString = getBinaryString(valueA)
        valueBString = getBinaryString(valueB)

        if valueAString[-16:] == valueBString[-16:]:
            self.count += 1
