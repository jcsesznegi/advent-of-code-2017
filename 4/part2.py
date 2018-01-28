import os

f = open(os.path.join(os.path.dirname(__file__), '../input/4/part2.txt'), 'r')


def main():
    line = f.readline()
    inputList = []
    while line:
        inputList.append(line)
        line = f.readline()

    def hasUniqueWords(passPhrase): 
        if (len(passPhrase) == len(set(passPhrase))): 
            return True
        return False

    def isAnagram(word1, word2): 
        if (len(word1) != len(word2)):
            return False

        list1 = list(word1)
        list2 = list(word2)
        list1.sort()
        list2.sort()

        matches = True
        for idx in range(0, len(list1)):
            if list1[idx] != list2[idx]:
                matches = False

        return matches

    def hasNoAnagrams(passPhrase): 
        for idx, word in enumerate(passPhrase):
            if idx == len(passPhrase) - 1:
                break
            for idx2 in range(idx + 1, len(passPhrase)):
                if isAnagram(word, passPhrase[idx2]):
                    return False
        return True

    totalValid = 0
    for row in inputList:
        passPhrase = row.rstrip().split(" ")
        if (hasUniqueWords(passPhrase)
            and hasNoAnagrams(passPhrase)): 
            totalValid += 1

    print(totalValid)

if __name__ == '__main__':
   main()
