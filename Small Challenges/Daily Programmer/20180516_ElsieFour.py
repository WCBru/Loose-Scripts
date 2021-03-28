def getVect(char):
    if char == "#":
        return (0,0)
    elif char == "_":
        return (1,0)
    elif char.isdigit():
        return index2vect(int(char))
    else:
        return index2vect(ord(char)-87)

def vect2index(vect):
    return (vect[1]%6)*6 + (vect[0]%6)

def index2vect(index):
    return (index%6, index//6)

if __name__ == "__main__":    
    key = input("Enter Key: ").strip()
    msg = input("Enter Message: ").strip()

    keys = [list(key) for x in range(2)]
    markers = [0 for x in range(2)]
    strings = ["" for x in range(2)]

    for char in msg:
        for i in range(2): # 0 for de, 1 for en
            # Get next char
            MarkVect = getVect(keys[i][markers[i]])
            startVect = index2vect(keys[i].index(char))

            #encrStr += key[vect2index((startVect[0]+MarkVect[0],
            #                           startVect[1] + MarkVect[1]))]
            sign = 1 if i else -1
            genVect = ((startVect[0]+sign*MarkVect[0])%6,
                                       (startVect[1] + sign* MarkVect[1])%6)
            strings[i] += keys[i][vect2index(genVect)]

            # Move marker
            locations = [startVect, genVect]
            MarkLoc = index2vect(markers[i])
            rowNo = locations[-1+i][1]
            colNo = locations[-2+i][0]

            # Check if permutation changes marker/cipher text location
            if MarkLoc[1] == rowNo:
                MarkLoc = ( (MarkLoc[0] + 1 )%6, MarkLoc[1])

            if locations[-2+i][1] == rowNo:
                colNo = (colNo + 1)%6
                
            if MarkLoc[0] == colNo:
                MarkLoc = (MarkLoc[0], (MarkLoc[1] + 1)%6)

            addVect = getVect((char, strings[i][-1])[i])
            markers[i] = vect2index((MarkLoc[0]+addVect[0],
                                   MarkLoc[1]+ addVect[1]))

            # Permutate Key
            originRow = keys[i][rowNo*6:(rowNo+1)*6]
            for x in range(6):
                keys[i][rowNo*6+x] = originRow[x-1]

            originCol = [keys[i][6*x+colNo] for x in range(6)]
            for x in range(6):
                keys[i][6*x+colNo] = originCol[x-1]

    print("Decryption: " + strings[0])
    print("Encryption: " + strings[1])
            

        

        
