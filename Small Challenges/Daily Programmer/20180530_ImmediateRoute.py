# This is so poorly done, but I've left it for a month or so
# If I ever come back to doing decrpytion, it ought to be done properly
# Otherwise, this will be left the way it is

def encrypt(string):
    # Parse input
    plain = string[1]
    dim, cw = string[2].split(") ")
    dimTup = tuple([int(digit) for digit in dim[2:].split(", ")])
    cw = True if cw == "clockwise" else False
    plain = "".join([char if char.isalpha() else "" for char in plain])
    while len(plain) < dimTup[0]*dimTup[1]:
        plain += "X"

    cipherString = ""
    for perim in range(min(dimTup)//2):
        perimString = traverse(plain, dimTup, -1, dimTup[0]-1-perim,1)
        perimString += traverse(plain, dimTup, dimTup[1]-1-perim,-1, -1)
        perimString += traverse(plain, dimTup, -1, perim, -1)
        perimString += traverse(plain, dimTup, perim, -1, 1)
        if not cw:
            perimString = perimString[0] + perimString[:0:-1]
        cipherString += perimString

    # Special Cases - odd number of rows/cols
    if dimTup[0]%2 == 0 and dimTup[1] == 0:
        return cipherString
    
    if dimTup[0] > dimTup[1]: # rows longer than col - an extra row
        cipherString += traverse(plain, dimTup, -1, dimTup[0]-1-dimTup[1]//2,1)
        cipherString += traverse(plain, dimTup, dimTup[1]//2,-1, -1)
        cipherString += traverse(plain, dimTup, -1, dimTup[1]//2, -1)
    else: # col longer than rows: one more col, or square
        cipherString += traverse(plain, dimTup, -1, dimTup[0]//2,1)

    return cipherString[0:len(plain)].upper()
        

def traverse(key, dim, row, col, sign):
    # Extract the required row/col
    if col == -1: # Traversing row, exclude ends
        padding = min(row, dim[1]-row-1) + 1
        outStr = key[dim[0]*row+padding:dim[0]*(row+1)-padding]
    if row == -1: # Traversing column, include ends
        padding = min(col, dim[0]-col-1)
        outStr = key[col+(dim[0]*padding):(dim[1]-padding)*dim[0]+col:dim[0]]
    
    return outStr[::sign] # Reverse if sign == -1

if __name__ == "__main__":
    inStr = input("Enter Input: ").strip().split("\"")
    
    if len(inStr) == 2:
        print(decrypt(inStr))
    elif len(inStr) == 3:
        print(encrypt(inStr))
    else:
        print("Unable to determine what is needed")
