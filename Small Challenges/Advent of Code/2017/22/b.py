direct = ((-1,0), (0,1), (1,0), (0,-1)) # changes in nested list indcies. up start, goes cw

def nextLoc(start, delta, length):
    return (start[0]+delta[0], start[1]+delta[1])

if __name__ == "__main__":
    grid = open("data22.txt", "r").read().split("\n")
    starting = []
    for line in range(len(grid)):
        grid[line] = [char for char in grid[line]]
        for char in range(len(grid[line])):
            if grid[line][char] == "#":
                starting.append((line, char))
    virLoc = (int(len(grid)/2), int(len(grid)/2))
    virDir = 0 # index in direct list
    states = {loc:1 for loc in starting}
    length = len(direct)

    infTot = 0 # track num infections
    burstNo = ""
    while not burstNo.isdigit():
        burstNo = input("Enter number of bursts: ")
    burstNo = int(burstNo)

    for x in range(burstNo):
        if states.get(virLoc) == None:
            states[virLoc] = -1
        infTot += 1 if states[virLoc] == 0 else 0
        virDir = (virDir+states[virLoc])%length
        states[virLoc] = (states[virLoc]+1)%length

        virLoc = nextLoc(virLoc, direct[virDir], len(grid)-1)

    print(infTot)
