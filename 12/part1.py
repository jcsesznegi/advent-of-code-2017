
import os

f = open(os.path.join(os.path.dirname(__file__), '../input/12/part1.txt'), 'r')

def main():

    programs = []

    line = f.readline().rstrip()
    while line:
        parts = line.split(' <-> ')
        pipes = [ int(pipeString) for pipeString in parts[1].split(', ') ]
        programs.append(pipes)
        line = f.readline().rstrip()

    def containsProgram(checkedList, programs, programList, checkProgram):
        if checkProgram in programList:
            return True

        def filterCheckedList(program, filterList):
            return program not in filterList

        filteredProgramList = filter(lambda p: filterCheckedList(p, checkedList), programList)

        for program in filteredProgramList:
            newCheckedList = checkedList + [program]
            if containsProgram(newCheckedList, programs, programs[program], checkProgram):
                return True

        return False

    total = 0
    checkProgram = 0
    for index, programList in enumerate(programs):
        if index == checkProgram:
            total += 1
        elif containsProgram([index], programs, programList, checkProgram):
            total += 1

    print(total)

if __name__ == '__main__':
   main()
