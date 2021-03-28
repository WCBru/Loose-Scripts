if __name__ == "__main__":
    # Ensure input is only numbers and has three elements
    inStr = ""
    while True:
        if len(inStr.strip().split()) == 3:
            if all([dig.isdigit() for dig in inStr.strip().split()]):
                break
        inStr = input("Enter input: ")
    
    total, opFemale, goal = [int(dig) for dig in inStr.strip().split()]
    total+= opFemale
    opTotal = total
    femaleTrack = [0 for x in range(96)]
    femaleTrack[2] = opFemale
    months = 0
    ded = 0

    # Main loop
    while total < goal: # The number of cycles can be calculated
        fertile = sum(femaleTrack[4:]) # Number of fertile female this cycle
        total += 14 * fertile # the total num of rabbits born
        femaleTrack.insert(0, 9* fertile) # add the number of females born
        toRemove = femaleTrack.pop() # females which died
        
        if months >= 94: # once the inital population starts dying
            if opTotal > 0: # if the inital population is dying
                ded += opTotal
                total -= opTotal
                opTotal = 0
            else: # Otherwise, use the 9:5 ratio
                ded += 14*toRemove//9
                total -= 14*toRemove//9
        months += 1

    print(months)
    print(ded)
    input()
