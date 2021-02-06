
def swapPositions(s, pos1, pos2):
    l = list(s)
    l[pos1], l[pos2] = l[pos2], l[pos1]
    return ''.join(l)

class Dance:
    def __init__(self, programs):
        self.programs = programs

    def getPrograms(self):
        return self.programs

    def performSpin(self, spinSize):
        self.programs = self.programs[-spinSize:] + self.programs[0:len(self.programs) - spinSize]

    def performExchange(self, posA, posB):
        self.programs = swapPositions(self.programs, posA, posB)

    def performPartner(self, programA, programB):
        posA = self.programs.find(programA)
        posB = self.programs.find(programB)
        self.programs = swapPositions(self.programs, posA, posB)

    def performMove(self, moveType, paramString):
        if moveType == 's':
            self.performSpin(int(paramString))
        elif moveType == 'x':
            positions = paramString.split('/')
            self.performExchange(int(positions[0]), int(positions[1]))
        elif moveType == 'p':
            programs = paramString.split('/')
            self.performPartner(programs[0], programs[1])

    def dance(self, moveList):
        for move in moveList:
            self.performMove(move[0], move[1:])

    def danceMultipleTimes(self, moveList, times):
        memo = {}

        i = 0
        while i < times:
            if self.programs in memo:
                self.programs = memo[self.programs]
            else:
                currentPrograms = self.programs
                for move in moveList:
                    self.performMove(move[0], move[1:])
                memo[currentPrograms] = self.programs
            i += 1
