if __name__ == "__main__":
    data = open("data4.txt","r")
    total = 0
    currentRow = data.readline().split()
    while len(currentRow) != 0:
        currentRow = data.readline().split()
        checkedWords = []
        for word in currentRow:
            if word in checkedWords:
                break
            else:
                checkedWords.append(word)
        else:
            total+= 1
    print(total)
