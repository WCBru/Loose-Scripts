if __name__ == "__main__":
    onStrike = 0
    reserve = 1
    runs = [0,0]
    totalRuns = 0
    overCounter = 0

    for ball in input("Enter input: ").strip():
        if ball == "W":
            if len(runs) > 10:
                break
            else:
                runs.append(0)
                onStrike = len(runs)-1
        elif (ball.isdigit()):
            scored = int(ball)
            runs[onStrike] += scored
            totalRuns += scored
            if (scored%2 == 1): # Change who is on strike
                onStrike, reserve = (reserve, onStrike)
        elif ball == "w": #Wide
            totalRuns += 1
            continue
        elif ball == "b":
            totalRuns += 1
            onStrike, reserve = (reserve, onStrike)
        elif ball != ".":
            print("Ball not recognised")

        overCounter += 1
        if overCounter >= 6:
            overCounter = 0
            onStrike, reserve = (reserve, onStrike)

    for player in range(len(runs)):
        print("P"+ str(player+1) + ": " + str(runs[player]))
    print("Extras: " + str(totalRuns - sum(runs)))

