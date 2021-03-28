# DFS Solution
# Not suitable for high branching factor

def countToDict(enum):
    register = {}
    for elm in enum:
            if elm in register:
                register[elm] += 1
            else:
                register[elm] = 0
    return register

def checkPossible(target, deck):
    available = countToDict([char for card in deck for char in card.split('/')])
    need = countToDict(target)
    for resrc in need:
        if resrc not in available:
            return False
        if need[resrc] > available[resrc]:
            return False
    
    return True

def checkComplete(target, deck):
    current = target
    for card in deck:
        if card.find('/') != -1: # Card not allocated
            return False
        elif current.find(card) != -1: # Remove if found
            index = current.find(card)          
            current = current[:index] + current[index+1:]
            
            if len(current) == 0: # Check all resources met
                return True

    return False        

def allocateExactMatches(target, deck, ded, depth):
    out = False
    needed = countToDict(target)
    available = countToDict([char for card in deck for char in card.split('/')])
    deductionList = []

    for resrc in needed: # For all needed
        if needed[resrc] == available.get(resrc):
            for card in range(len(deck)):
                if resrc in deck[card].split('/') and resrc != deck[card]:
                    deductionList.append((card, deck[card]))
                    out = True
                    deck[card] = resrc

    if len(ded) <= depth:
        ded.append(deductionList)
    else:
        ded[depth] += deductionList
    return out

# Return a list of all cards with '/' with depth and index
# (In reverse of the order just described)
def getBranches(depth, deck):
    out = []
    for card in range(len(deck)):
        if deck[card].find('/') != -1:
            out += [(card, depth, char) for char in deck[card].split('/')]
    return out

if __name__ == "__main__":
    # Take and process inputs
    inStr = input().strip().split()
    output = inStr[-1][:-1]
    cards = [card[:-1] for card in inStr[1:-4]]
    
    # Fix formatting
    cards[0] = cards[0][1:]
    cards[-1] = cards[-1][:-1]

    # Check if possible
    if not checkPossible(output, cards):
        print("Unrecognised resource in target")
    else:
        # Trackers: Index, Level and branch it was done on
        # Backtrack: Index and the card that was there 
        branches = []
        backTrack = []
        deductions = []
        level = 0
        backTrackFlag = False
        
        while not checkComplete(output, cards):
            #print(cards)
            # Allocate Exact Matches, and see if that solves it
            # Store deductions
            while allocateExactMatches(output, cards, deductions, level):
                pass
            if checkComplete(output,cards):
                break

            # Branch into next option
            else:
                # Find possible branches
                if checkPossible(output, cards):
                    branches += getBranches(level, cards)
                    
                if len(branches) == 0:
                    break
                #print(branches)
                
                # Backtrack if no branches at this level
                # TODO: Backtracking for deductions at the beginning of the top while loop
                while branches[-1][1] < level:
                    backTrackFlag = True
                    prevCard = backTrack.pop()
                    cards[prevCard[0]] = prevCard[1]

                    # Undo deductions
                    # This needs to break multiple deductions on one level
                    # Need to append? would need a way to mark it
                    for ded in deductions.pop():
                        cards[ded[0]] = ded[1]
                    level -= 1

                # Branch to next and store what's left into backtrack
                nextBranch = branches.pop()
                backTrack.append((nextBranch[0], cards[nextBranch[0]]))
                cards[nextBranch[0]] = nextBranch[2]
                level += 1

        if checkComplete(output, cards):
            print("Solution found for " + output)
            print(' '.join(cards))
        else:
            print("No solution found for " + output)
