
import os, re

f = open(os.path.join(os.path.dirname(__file__), '../input/9/part1.txt'), 'r')

def getGarbageCharacterCount(stream):
    cleanStream = re.sub('<[^>]*>', '', stream)
    matches = re.findall('<[^>]*>', stream)
    containerCharacterCount = len(matches) * 2
    
    return len(stream) - len(cleanStream) - containerCharacterCount

def main():

    line = f.readline().rstrip()
    line = re.sub('!.', '', line)
    
    count = getGarbageCharacterCount(line)

    print(count)


if __name__ == '__main__':
       main()
