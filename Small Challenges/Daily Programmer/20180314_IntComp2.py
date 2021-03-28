if __name__ == "__main__":
    target = 1000
    reg = {key:target for key in range(1, target + 1)}
    reg[1] = 1
    for key in range(2, target + 1):
        sub = 1
        while sub < key:
            reg[key] = min(reg[key], reg[key-sub] + sub)
            sub += 1

        factor = 2
        while key*factor <= target and factor <= key:
            reg[key*factor] = min(reg[key*factor], reg[key]+factor)
            factor += 1
            
    print(sum([reg[key] for key in reg.keys()])) # print sum of values
