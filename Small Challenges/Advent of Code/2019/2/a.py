if __name__ == "__main__":
    dataFile = open("input.txt")
    data = [int(i) for i in dataFile.read().split(",")]
    dataFile.close()

    data[1] = 12
    data[2] = 2

    index = 0
    while data[index] != 99:
        if data[index] == 1:
            data[data[index + 3]] = data[data[index + 2]] + data[data[index + 1]]
        elif data[index] == 2:
            data[data[index + 3]] = data[data[index + 2]] * data[data[index + 1]]
        else:
            raise ValueError("Invalid OP Code")

        index += 4

    print(data[0])
