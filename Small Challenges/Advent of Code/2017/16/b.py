numDances = 1000000000

def carryOrder(order, lst):
    outLst = lst[:]
    if order[0] == 's': #spin
        offset = int(order[1:])
        for elm in range(len(lst)):
            outLst[(elm+offset)%len(lst)] = lst[elm]
    elif order[0] == 'x':
        targets = order[1:].split("/")
        for target in range(2):
            outLst[int(targets[target])] = lst[int(targets[target-1])]
    elif order[0] == 'p':
        targets = order[1:].split("/")
        for elm in range(2):
            targets[elm] = lst.index(targets[elm])
        for target in range(2):
            outLst[int(targets[target])] = lst[int(targets[target-1])]

    return outLst

if __name__ == "__main__":
    posns = [chr(x) for x in range(97, 113)]
    first = posns[:]
    orders = open("data16.txt", "r").read().split(',')
    for x in range(numDances):
        if posns == first and x != 0:
            loop = x
            break
        for order in orders:
            posns = carryOrder(order, posns)

    for x in range(numDances%loop):
        for order in orders:
            posns = carryOrder(order, posns)

    print("".join(posns))
