def genLetterDict(word):
    targetLetters = {}
    for letter in word:
        if targetLetters.get(letter) != None: # if already catalogued
            targetLetters[letter] += 1
        else:
            targetLetters[letter] = 1
    return targetLetters

def hasAnagram(target, lst):
    #generate target letters
    targetLetters = genLetterDict(target)

    for word in lst:
        wordLetters = genLetterDict(word)
        wordKeys = wordLetters.keys()
        for key in wordKeys:
            if targetLetters.get(key) == None:
                break # if they contain different letters, not anagram
            elif targetLetters[key] != wordLetters[key]:
                break # if differing amounts, not anagram
            
        else: # chceked word is substring of the target, check vice versa
            for letter in targetLetters.keys():
                if letter not in wordKeys:
                    return False
            else:
                return True
    return False # no anagram was found
                

if __name__ == "__main__":
    data = open("data4.txt","r")
    total = 0
    currentRow = data.readline().split()
    while len(currentRow) != 0:
        checkedWords = []
        for word in currentRow:
            #print(checkedWords)
            if hasAnagram(word, checkedWords):
                break
            else:
                checkedWords.append(word)
        else:
            #print("valid")
            total+= 1
        currentRow = data.readline().split()
    print(total)
