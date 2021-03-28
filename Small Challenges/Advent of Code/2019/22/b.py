# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Using_the_existence_construction
def egcd(tup1, tup2):
    q, r = divmod(tup1[0], tup2[0])
    if r == 0:
        return tup2
    else:
        return egcd(tup2,
                    tuple([tup1[i] - q * tup2[i] for i in range(len(tup1))]))

def reverse(length, target):
    return ((-target - 1) % length, -1, -1)

def cut(length, n, target):
    return ((target + n) % length, 1, n)

def inc(length, n, target):
    g, i1, i2 = egcd((n, 1, 0), (length, 0, 1))
    if g != 1:
        raise Exception("Not coprime")
    else:
        return ((i1 * target) % length, i1, 0)

if __name__ == "__main__":
    instr = open("input.txt").read().strip().split("\n")[::-1]
    #start = 0
    #length = 10
    #repeat = 1

    start = 2020
    length = 119315717514047
    repeat = 101741582076661

    pos = start
    mult = 1
    add = 0
    for line in instr:
        parts = line.split()
        if parts[-1] == "stack":
            pos, m, a = reverse(length, pos)
        elif parts[0] == "cut":
            pos, m, a = cut(length, int(parts[1]), pos)
        else:
            pos, m, a = inc(length, int(parts[-1]), pos)
            
        mult = (m * mult) % length
        add = (m * add + a) % length

    print(pos)    

    # Polynomial division is not my strong siot
    # want add * (mult^repeat - 1) / (mult - 1)
    _, i, _ = egcd((mult - 1, 1, 0), (length, 0, 1))
    m2 = pow(mult, repeat, length)
    a2 = (add * (m2 - 1) * i) % length

    print((m2 * start + a2) % length)
