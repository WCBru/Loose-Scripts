import urllib.request as url

PATTERN_URL = "https://gist.githubusercontent.com/cosmologicon/1e7291714094d71a0e25678316141586/raw/006f7e9093dc7ad72b12ff9f1da649822e56d39d/tex-hyphenation-patterns.txt"

def getPatternList(inList, indicies): # Read list into given parameter, letter indicies
    for word in url.urlopen(PATTERN_URL).read().decode().split("\n"):
        inList.append(word)

    for letter in range(97, 123): # for a - z (. is the beginning)
        counter = 0 if len(indicies) == 0 else indicies[-1] # start point for letter

        # Determine if we've reached a new section
        while counter < len(inList):
            letterNo = 0
            # Find first letter
            while not inList[counter][letterNo].isalpha():
                letterNo += 1

            # Check if first letter is the one we want
            if inList[counter][letterNo] == chr(letter) and inList[counter][0] != '.':
                indicies.append(counter)
                break

            counter += 1

def findLetterMatches(wordArray, index, wordList, indicies):
    # Find the start and end of the patterns - based on the letter index given
    firstLetter = wordArray[2*index]
    start = indicies[ord(firstLetter) - 97] if firstLetter.isalpha() else 0
    end = indicies[ord(firstLetter) - 96] if firstLetter != 'z' and firstLetter != '.' else -1

    # Go through the patterns with this letter
    for word in wordList[start:end]:
        # Initialise the array for each letter
        candList = [0]
        for let in word:
            if let.isdigit(): # is number - update score to last added 0
                candList[-1] = int(let)
            else: # Is letter - add to array
                candList.append(let)
                candList.append(0)

        # Don't try if the pattern is too long
        if len(candList) >= len(wordArray[index:]):
            continue

        # Check that the pattern matches
        for let in range(len(candList)//2):
            if candList[2*let+1] != wordArray[(2*index)+ 2*let]:
                break
        else: # If it does, update the values
            for num in range(len(candList)//2+  1):
               wordArray[(2*index)-1 + 2*num] = max(wordArray[(2*index)-1 + 2*num],candList[2*num])


if __name__ == "__main__":
    patterns = []
    letIndex = []
    getPatternList(patterns, letIndex)

    # Input and list creation
    target = "." + input("Please enter word: ").strip().lower() + "."
    targetArray = []
    for letter in target:
        targetArray.append(letter)
        targetArray.append(0)

    # Assigning of values by iterating through each letter
    for letind in range(len(target)-1):
        findLetterMatches(targetArray, letind, patterns, letIndex)

    # Convert and print out final word
    targetArray = targetArray[2:-3]
    outArray = []
    for char in targetArray:
        if type(char) == int:
            outArray.append("" if char%2==0 else "-")
        else:
            outArray.append(char)

    print("".join(outArray))
        
