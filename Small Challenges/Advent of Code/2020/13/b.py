# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Using_the_existence_construction
def egcd(tup1, tup2):
    q, r = divmod(tup1[0], tup2[0])
    if r == 0:
        return tup2
    else:
        return egcd(tup2,
                    tuple([tup1[i] - q * tup2[i] for i in range(len(tup1))]))

if __name__ == "__main__":
    start, servs = open("input.txt").read().split("\n", 2)
    servs = servs.split(',')
    current = int(servs[0])
    base = current
    
    for i in range(1, len(servs)):
        if servs[i] == 'x':
            continue
        else:
            num = int(servs[i])
            g, i1, i2 = egcd((base, 1, 0), (num, 0, 1))
            if g != 1:
                raise Exception("Not coprime")
            else:
                current = (current * i2 * num - i * i1 * base) % (base * num)
                base *= num
            
    print(current)
