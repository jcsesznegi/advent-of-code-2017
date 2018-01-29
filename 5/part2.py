import os

f = open(os.path.join(os.path.dirname(__file__), '../input/5/part2.txt'), 'r')


class InstructionSet:

    def __init__(self, instructions):
        self.instructions = instructions
        self.currentIndex = 0
        self.numberSteps = 0

    def _changeOffsetValue(self, index):
        if self.instructions[index] >= 3:
            self.instructions[index] -= 1
        else:
            self.instructions[index] += 1 

    def jump(self):
        self.numberSteps += 1
        jumpNumber = self.instructions[self.currentIndex]
        oldIndex = self.currentIndex
        self.currentIndex += jumpNumber
        self._changeOffsetValue(oldIndex)

    def run(self):
        while (self.currentIndex >= 0
            and self.currentIndex < len(self.instructions)):
            self.jump()


def main():

    def formatLine(line):
        return int(line.rstrip())

    line = f.readline()
    instructions = []
    while line:
        instructions.append(formatLine(line))
        line = f.readline()

    instructionSet = InstructionSet(instructions)
    instructionSet.run()
    print(instructionSet.numberSteps)


if __name__ == '__main__':
   main()
