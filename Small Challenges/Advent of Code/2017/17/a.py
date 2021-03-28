if __name__ == "__main__":
    numSteps = ""
    while not numSteps.isdigit():
        numSteps = input("Enter number of steps: ").strip()
    numSteps = int(numSteps)

    buffer = [0]
    currentPosition = 0
    for num in range(2017):
        currentPosition = (currentPosition+numSteps+1)%len(buffer)
        buffer.insert(currentPosition, num+1)

    print(buffer[buffer.index(2017)+1])
    input()
