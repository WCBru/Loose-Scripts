import knotCode as kHash

if __name__ == "__main__":
    keyStr = input("Enter a key: ")
    usedTotal = 0
    
    for row in range(128):
        roundSeq = kHash.createSeq(keyStr + "-" + str(row))
        hexChars = kHash.fullKnot(roundSeq)
        for char in hexChars:
            for digit in str(bin(int(char, 16)))[2:]:
                usedTotal += 1 if digit == '1' else 0

    print(usedTotal)
