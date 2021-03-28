SSDCHARS = [
    [" _ ", "   ", " _ ", " _ ", "   ", " _ ", " _ ", " _ ", " _ ", " _ "],
    ["| |", "  |", " _|", " _|", "|_|", "|_ ", "|_ ", "  |", "|_|", "|_|"],
    ["|_|", "  |", "|_ ", " _|", "  |", " _|", "|_|", "  |", "|_|", " _|"]
    ]

if __name__ == "__main__":
    inStr = ""
    while not inStr.isdigit():
        inStr = input("Enter a number: ").strip()

    outList = [[SSDCHARS[row][int(dig)] for dig in inStr] for row in range(3)]
    print("\n".join([" ".join(row) for row in outList]))    
