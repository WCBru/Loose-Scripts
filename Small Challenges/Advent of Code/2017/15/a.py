aFact = 16807
bFact = 48271
div = 2147483647

def genNextVals(x, y):
    return ((x*aFact)%div, (y*bFact)%div)

def bitMatch(num1, num2):
    x = num1
    y = num2
    for n in range(16):
        if x%2 != y%2:
            return False
        else:
            x = int(x/2)
            y = int(y/2)
    else:
        return True

if __name__ == "__main__":
    file = open("data15.txt", "r")
    aNum = int(file.readline().split()[-1])
    bNum = int(file.readline().split()[-1])
    score= 0

    for x in range(40000000):
        aNum, bNum = genNextVals(aNum, bNum)
        score += 1 if bitMatch(aNum, bNum) else 0

    print(score)
