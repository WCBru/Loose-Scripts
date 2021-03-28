# Assuming all groups are well-formed
if __name__ == "__main__":
    data = open("data9.txt", "r")
    currChar = data.read(1)
    currLevel = 0
    inGarbage = False
    total = 0
    while currChar != "":
        if currChar == "!":
            data.read(1) #skip 1 char
        elif not inGarbage:
            if currChar == "{":
                currLevel += 1
            elif currChar == "}":
                currLevel -= 1
            elif currChar == "<":
                inGarbage = True
        elif currChar == ">":
            inGarbage = False
        else:
            total += 1
        
        currChar = data.read(1)

    print(total)
