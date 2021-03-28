def findNextCoin(coins, target, ava):
    # Check if limit reached
    if ava == 0 or len(coins) == 0 or coins[-1] > target or target < 0:
        return []
    else:
        for index in range(len(coins)):
            newAv = ava - 1 if ava > 0 else ava
            newAv += 1 if ava < -1 else 0
            newCoins = [coins[index]] + findNextCoin(coins[index+1:],
                                                     target-coins[index],
                                                     newAv)
            if sum(newCoins) == target and newAv >= -1:
                return newCoins

            #check valid
        
        return []

if __name__ == "__main__":
    target = 0
    limit = 0
    change = []
    cont = True
    while cont:
        try:
            firstLine = input().split()
            target = int(firstLine[1])
            change = [int(coin) for coin in firstLine[2:]]

            secondLine = input().split()
            limit += 1 if len(secondLine[2]) == 2 else 0
            limit += int(secondLine[3])
            limit *= -1 if secondLine[2][0] == ">" else 1
            cont = False
        except Exception:
            pass

    print(findNextCoin(change, target, limit))
