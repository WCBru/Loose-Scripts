def strength(bridge):
    stren = 0
    for comp in bridge:
        stren += comp[0] + comp[1]

    return stren

def findChildren(target, head, lst):
    n, s = (0,1)
    outLst = []
    for comp in lst:
        if head in comp:
            outLst.append(comp)
    return outLst

if __name__ == "__main__":
    rawIn = open("data24.txt", "r").read().split("\n")
    sets = []
    for comp in rawIn:
        comSp = comp.split("/")
        sets.append((int(comSp[0]), int(comSp[1])))
    
    best = []
    stack = []
    current = []
    head = 0
    for comp in sets:
        if 0 in comp:
            stack.append((comp, len(current)))

    while len(stack) != 0:
        currNode = stack.pop()[0]
        sets.remove(currNode)
        current.append(currNode)
        head = currNode[currNode.index(head)^1]
        children = findChildren(currNode, head, sets)
        if len(children) == 0:
            if strength(current) > strength(best):
                best = current[:]
            if len(stack) != 0:
                lowLvl = stack[-1][1]
                while len(current) > lowLvl:
                    prev = current.pop()
                    head = prev[prev.index(head)^1]
                    sets.append(prev)
        else:
            for child in children:
                stack.append((child, len(current)))

    print(strength(best))
