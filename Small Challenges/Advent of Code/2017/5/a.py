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
        jmpLst[currentJmp] += 1
        currentJmp += jmpLst[currentJmp] - 1
        steps += 1

    print(steps)
