
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

    def getConnectedPrograms(programs, index, connectedPrograms):
        connectedPrograms.add(index)

        for program in programs[index]:
            if program in connectedPrograms:
                continue
            nextConnectedPrograms = getConnectedPrograms(programs, program, connectedPrograms)
            connectedPrograms.update(nextConnectedPrograms)

        return connectedPrograms;

    groups = []
    for index, programList in enumerate(programs):
        isAlreadyChecked = False
        for group in groups:
            if index in group:
                isAlreadyChecked = True;

        if not isAlreadyChecked:
            connectedPrograms = getConnectedPrograms(programs, index, set([]))
            groups.append(connectedPrograms)

    print(len(groups))

if __name__ == '__main__':
   main()
