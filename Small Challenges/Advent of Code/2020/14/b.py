def parse_mask(phrase):
    zero, floats, count = (0, 0, 0)
    for bit in range(len(phrase)):
        if phrase[bit] == '1':
            one += 2**(len(phrase) - 1 - bit)
        elif phrase[bit] == 'X':
            floats += 2**(len(phrase) - 1 - bit)
            count += 1

    if floats & one != 0:
        raise ValueError("Masks not mutually exclusive")

    return (floats, one, 2**count)
    

if __name__ == "__main__":
    lines = open("input.txt").read().split('\n')
    vals = {}
    maskf, mask1 = (0, 0)
    
    for line in lines:
        parts = line.split(' = ')
        if parts[0] == "mask":
            maskf, mask1, addr = parse_mask(parts[1])
        elif parts[0][0:3] == "mem":
            count = addr
            key = int(parts[0][4:-1]) | mask1
            for key in vals.keys():
                if 
            vals[(key, maskf)] = (count, int(parts[1]))
        else:
            raise KeyError("Keyword not recognised: " + parts[0])

    print(all([vals[k] >= 0 for k in vals.keys()]))
    print(sum([vals[k] for k in vals.keys()]))
