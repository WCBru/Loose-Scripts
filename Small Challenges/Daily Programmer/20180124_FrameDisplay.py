if __name__ == "__main__":    
    scores = input("Enter Scores: ").strip().split()
    # Check that input is valid
    while True: 
        try: # Check if all numbers are from 0 - 10
            if (all([int(score) <= 10 and int(score) >= 0
                     for score in scores])):
                break;
        except ValueError: # if NaN was in the input
            pass
        scores = input("Enter Scores: ").strip().split() # Ask again

    scores = [int(score) for score in scores] # change scores to integers
    output = ""
    firstRoll = 0 # Tracks if the first bowl was not a strike

    # Main loop removes scores as they are used
    while (len(scores) > 0):
        current = scores.pop(0)
        if current == 10: # strike
            output += "X  "
        elif firstRoll == 0: # first bowl
            output += str(current) if current > 0 else "-"
            firstRoll = current
        else: # second bowl
            if current + firstRoll == 10: # spare
                output += "/ "
            else: # total < 10
                output += str(current) + " " if current > 0 else "- "
            firstRoll = 0 # reset first bowl flag
            
    beginFrames = output.split()[:9] # first 9 frames normal
    lastFrame = output.split()[9:] # last frame can be combined
    print(" ".join(beginFrames) + " " + "".join(lastFrame))
    input()
