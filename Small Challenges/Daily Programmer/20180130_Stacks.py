import sys

def getAvailDigits(lst):
    output = []
    for dig in lst:
        if dig not in output:
            output.append(dig)
    return output

def isValidSolution(lst, target, limit):
    runningTally = 0
    counter = 0
    for dig in lst:
        runningTally += dig
        if runningTally > target:
            return False
        elif runningTally == target:
            counter += 1
            runningTally = 0
    return runningTally == 0 and counter == limit

def end(lst, target):
    current = []
    for dig in lst:
        current.append(dig)
        if sum(current) == target:
            print(''.join([str(num) for num in current]))
            current = []

def checkPermutation(lst, existing, target, limit):
    
    if len(lst) == 1:
        last = lst[:]+existing[:]
        if isValidSolution(last, target ,limit):
            end(last, target)
            sys.exit()
        else:
            return
    else:
        for dig in getAvailDigits(lst):
            nextOut = lst[:]
            nextOut.remove(dig)
            nextEx = existing[:]
            nextEx.append(dig)
            checkPermutation(nextOut, nextEx, target, limit)

def getInput():
    # Get an input with 2 lots of numbers
    while True:
        output = input().split()
        if len(output) == 2 and all([dig.isdigit() for dig in output]):
            return output

if __name__ == "__main__":
    inStr = getInput()
    stacks = int(inStr[0])
    boxes = [int(dig) for dig in inStr[1]]

    # Return if even stacks not possible
    if sum(boxes)%stacks == 0:
        target = sum(boxes)//stacks
        checkPermutation(boxes, [],target, stacks)

        
            
