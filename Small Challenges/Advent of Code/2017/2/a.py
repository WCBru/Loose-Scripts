if __name__ == "__main__":
    data = open("data2.txt", "r")
    total = 0
    currentRow = data.readline().strip()
    while currentRow != "":
        rowData = currentRow.split()
        maxNum = int(rowData[0])
        minNum = maxNum
        for cell in rowData:
            maxNum = max(maxNum, int(cell))
            minNum = min(minNum, int(cell))

        total += maxNum - minNum
        currentRow = data.readline().strip()

    print(total)
