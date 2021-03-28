if __name__ == "__main__":
    jmpLst = []
    data = open("data5.txt", "r")
    currentRow = data.readline().strip()
    while currentRow != "":
        jmpLst.append(int(currentRow))
        currentRow = data.readline().strip()

    steps = 0
    currentJmp = 0
    while currentJmp >=0 and currentJmp < len(jmpLst):
        increment = 1
        if jmpLst[currentJmp] > 2:
            increment*=-1
        jmpLst[currentJmp] += increment
        currentJmp += jmpLst[currentJmp] - increment
        steps += 1

    print(steps)
