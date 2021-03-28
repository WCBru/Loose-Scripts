numLock = 50000000

if __name__ == "__main__":
    numSteps = ""
    while not numSteps.isdigit():
        numSteps = input("Enter number of steps: ").strip()
    numSteps = int(numSteps)

    buffer = [0]
    currPos = 0
    currSoln = 1
    currZPos = 0
    length = 1
    for num in range(numLock):
        currPos = (currPos+numSteps+1)%length
        if currPos == currZPos:
            currSoln = num+1
        elif currPos < currZPos:
            currZPos += 1
        length += 1

    print(currSoln)
    input()
