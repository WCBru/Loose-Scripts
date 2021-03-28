def parse_mask(phrase):
    zero, one = (0, 0)
    for bit in range(len(phrase)):
        if phrase[bit] == '1':
            one += 2**(len(phrase) - 1 - bit)
        elif phrase[bit] == '0':
            zero += 2**(len(phrase) - 1 - bit)

    if zero & one != 0:
        raise ValueError("Masks not mutually exclusive")

    return (zero, one)
    

if __name__ == "__main__":
    lines = open("input.txt").read().split('\n')
    vals = {}
    mask0, mask1 = (0, 0)
    
    for line in lines:
        parts = line.split(' = ')
        if parts[0] == "mask":
            mask0, mask1 = parse_mask(parts[1])
        elif parts[0][0:3] == "mem":
            key = int(parts[0][4:-1])
            vals[key] = ((int(parts[1]) | mask1) & (~mask0))
        else:
            raise KeyError("Keyword not recognised: " + parts[0])

    print(all([vals[k] >= 0 for k in vals.keys()]))
    print(sum([vals[k] for k in vals.keys()]))
