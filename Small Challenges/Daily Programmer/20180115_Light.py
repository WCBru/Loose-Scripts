def processNewTime(newTime, knownTimes):
    for oldTime in knownTimes:
            #Check for overrlap
            if newTime[1] >= oldTime[0] and newTime[0] <= oldTime[1]:
                oldTime[0] = min(oldTime[0], newTime[0])
                oldTime[1] = max(oldTime[1], newTime[1])
                break
    else: # Add if the list is empty
        knownTimes.append(list(newTime))

if __name__ == "__main__":
    # Input as list of tuples
    # Requires "input.txt" to contain the input
    times = []
    for pair in open("input.txt", "r").read().split("\n"):
        times.append(tuple(int(time) for time in pair.split()))

    # Process each time
    knownIntervals = []
    for time in times:
        processNewTime(time, knownIntervals)
        
    # check internal overrlap
    finalList = []
    for pair in knownIntervals:
        processNewTime(pair, finalList)

    total = 0 # Find the number of hours on
    for time in finalList:
        total += time[1]- time[0]

    print(total)
