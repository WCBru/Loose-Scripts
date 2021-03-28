# The hard/slow way, since using .find() feels like cheating
import urllib.request as req

def check(word):
    for letter in range(len(word)):
        if word[letter] == 'e':
            if letter > 1:
                if word[letter-1] == 'i' and word[letter-2] == 'c':
                    return False

            if letter < len(word) - 1:
                if word[letter+1] == 'i' and (word[letter-1] != 'c' or letter == 0):
                    return False
    return True

if __name__ == "__main__":
    counter = 0
    wordList = req.urlopen("https://norvig.com/ngrams/enable1.txt").read().decode().split("\n")
    print("Processing " + str(len(wordList)) + " words")
    for word in wordList:
        counter += 0 if check(word.lower()) else 1

    print(str(counter) + " words violate the rule")
