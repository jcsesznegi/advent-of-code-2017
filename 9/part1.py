
import os, re

f = open(os.path.join(os.path.dirname(__file__), '../input/9/part1.txt'), 'r')

def findGroups(stream):
    groups = []
    startIndex = stream.find('{')

    if startIndex == -1:
        return groups

    endIndex = startIndex + 1
    groupMatchCount = 1

    while groupMatchCount > 0 and endIndex < len(stream):
        if stream[endIndex] == '{':
            groupMatchCount += 1
            endIndex += 1
        elif stream[endIndex] == '}':
            groupMatchCount -= 1
            if groupMatchCount != 0:
                endIndex += 1
        else:
            endIndex += 1

    if groupMatchCount != 0:
        return groups

    groups.append(stream[startIndex + 1:endIndex])

    otherGroups = []
    if endIndex < len(stream) - 1:
        otherGroups = findGroups(stream[endIndex:])

    return groups + otherGroups

def processStream(stream, score=1):
    groups = findGroups(stream)
    length = len(groups)

    streamScore = score * length

    for group in groups:
        if not group:
            continue

        subStreamScore = processStream(group, score + 1)
        streamScore += subStreamScore

    return streamScore

def main():

    line = f.readline().rstrip()
    line = re.sub('!.', '', line)
    line = re.sub('<[^>]*>', '', line)

    score = processStream(line)

    print(score)


if __name__ == '__main__':
       main()
