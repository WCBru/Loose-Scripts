direct = ((-1,0), (0,1), (1,0), (0,-1)) # changes in nested list indcies. up start, goes cw

def nextLoc(start, delta, length):
    out = (start[0]+delta[0], start[1]+delta[1])
    #out = (min(out[0], length), min(out[1], length))
    #out = (max(out[0], 0), max(out[1], 0))
    return out

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
    infected = starting[:]

    infTot = 0 # track num infections
    burstNo = ""
    while not burstNo.isdigit():
        burstNo = input("Enter number of bursts: ")
    burstNo = int(burstNo)

    for x in range(burstNo):
        #USE A TRACKING METHOD, INSTEAD OF CREATING THE GRID ITSELF
        #REMEMBER THAT THE GRID GOES PAST WHAT IS GIVEN
        if virLoc not in infected:
            infected.append(virLoc)
            infTot += 1
            virDir = (virDir-1) % len(direct)  
        else:
            infected.remove(virLoc)
            virDir = (virDir+1) % len(direct)

        virLoc = nextLoc(virLoc, direct[virDir], len(grid)-1)

    print(infTot)
