# A slow implementation
# It should instead increment the result only, and branch based on what numbers can be used to sum to it

def addLetters(string, ref):
    for letter in string:
        print(letter)
        if letter not in ref:
            ref[letter] = -1

def val(word):
    outStr = ""
    for letter in word.upper():
        if values[letter] == -1:
            raise ValueError("Letter value not set")
        else:
            outStr += str(values[letter])
    return int(outStr)

def currentNines(current, existing, value):
    for letter in current:
        if value[letter] != 9 and letter not in existing:
            return False
    else:
        return True

def noDupes(nums, letters):
    for letter in letters:
        for key in nums:
            if letter != key and nums[key] == nums[letter]:
                return False
    else:
        return True

def letterOnLevel(index, carry, vol, vals, inp):
    if index == -1:
        return False
    elif index == len(inp[-1]):
        return True
    else:
        # Previously set letters
        setLetters = [] 
        for prevLetter in range(index):
            setLetters += vol[prevLetter]

        currLetters = []
        for word in inp:
            if index < len(word):
                currLetters.append(word[-1-index])
                if vals[word[-1-index]] == -1:
                    vals[word[-1-index]] = 0 if index != len(word) - 1 else 1
        
        while True:
            currSum = sum([vals[let] for let in currLetters[:-1]]) + carry
            #print(str({letter:vals[letter] for letter in currLetters}) + str(currSum))
            if currSum%10 == vals[inp[-1][-1-index]] and noDupes(values, currLetters):
                vol[index] = []
                for letter in currLetters:
                    if letter not in setLetters:
                        vol[index].append(letter)
                if letterOnLevel(index+1, currSum//10, vol, vals, inp):
                    return True
                else:
                    for prevLetter in range(index):
                        setLetters += vol[prevLetter]

            if currentNines(currLetters, setLetters, vals):
                for letter in currLetters:
                    vals[letter] = -1 if letter not in setLetters else vals[letter]
                vol[index] = []
                return False
                
            # increment
            for letter in currLetters:
                if letter not in setLetters:
                    vals[letter] += 1
                    if vals[letter] == 10:
                        vals[letter] = 0
                        continue
                    else:
                        break

if __name__ == "__main__":
    inStr = input("Enter input: ").split()[::2]
    values = {}
    for word in inStr:
        for letter in word:
            if letter not in values:
                values[letter] = -1

    volatile = {} # level of volatility of numbers

    
        # Replace with recursive functionality
        # Since letters are already determined, it would not be difficult to simply set the index
        # to whatever the output is
        # this output would simply be the index: either len(result) or the previous level
        # in that case, volatile addition would happen in the function
        # Loop for incrementing at a level
    '''
        while sum([vals[let] for let in currLetters[:-1]]) + carry != vals[result[-1-index]]:
            else:
                print("Prev Level " + str(vals))
                index -= 1
                vol[index][-1] += 1
                break
        else: # when the digit matches
            print("Next Level " + str(vals))
            vol[index] = []
            for letter in currLetters:
                if letter not in setLetters:
                    vol[index].append(letter)
            vol[index].append(sum([vals[let] for let in currLetters[:-1]]) % 10)
            print(vol)
            index += 1
    '''
            

    if not letterOnLevel(0,0,volatile, values, inStr):
        print(values)
        raise Exception("No solution found")
    
    lhs = sum([val(word) for word in inStr[:-1]])
    rhs = val(inStr[-1])
    if lhs != rhs:
        print(values)
        raise ValueError("Results don't add up\n" + str(lhs) + " != " + str(rhs))
    else:
        print(values)
