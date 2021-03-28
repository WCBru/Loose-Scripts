def reverse(deck):
    return deck[::-1]

def cut(deck, n):
    if n > 0:
        return deck[n:] + deck[:n]
    elif n < 0:
        return deck[n:] + deck[:n]

def inc(deck, n):
    newDeck = [None for card in deck]
    for card in range(len(deck)):
        newDeck[(card * n) % len(deck)] = deck[card]

    return newDeck

if __name__ == "__main__":
    instr = open("input.txt").read().strip().split("\n")
    deck = [x for x in range(10007)]
    for line in instr:
        parts = line.split()
        if parts[-1] == "stack":
            deck = reverse(deck)
        elif parts[0] == "cut":
            deck = cut(deck, int(parts[1]))
        else:
            deck = inc(deck, int(parts[-1]))

    print(deck.index(2019))
