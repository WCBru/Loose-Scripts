def decode(string):
    row, col = (0, 0)
    for r in range(7):
        row += 2**(6-r) if string[r] == "B" else 0

    for r in range(3):
        col += 2**(2-r) if string[r+7] == "R" else 0

    return (row, col)

if __name__ == "__main__":
    seats = [decode(s) for s in open("input.txt").read().strip().split()]
    ids = sorted([s[0] * 8 + s [1] for s in seats])
    
    for i in range(len(ids)):
        s = i + ids[0]
        if ids[i] != s:
            print(s)
            break
        
