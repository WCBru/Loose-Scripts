INPUT = [20,9,11,0,1,2]
LIMIT = 30000000#2020

if __name__ == "__main__":
    turn = 0
    last = -1
    log = {}

    for num in INPUT[0:-1]:
        log[num] = turn
        turn += 1

    last = INPUT[-1]
    
    while turn < LIMIT - 1:
        newNum = None
        if last in log:
            newNum = turn - log[last]
        else:
            newNum = 0

        log[last] = turn
        last = newNum
        turn += 1

    print(last)

    
