LIMITS = (273025, 767253)

def get_valid_numbers(num, doubleDone):
    prevInt = num % 10
    scaledUp = num * 10
    if num // 10000 > 0:
        return [scaledUp + prevInt] \
               if not doubleDone else \
               [scaledUp + x for x in range(prevInt, 10)]
    else:
        output = []
        for x in range(prevInt, 10):
            output += get_valid_numbers(scaledUp + x, doubleDone or prevInt == x)
        return output

def valid_pw(string):
    lists = []
    startInd = 0
    for i in range(len(string)):
        if string[i] != string[startInd]:
            lists.append(string[startInd:i])
            startInd = i

    lists.append(string[startInd:])
    return any([len(part) == 2 for part in lists])

if __name__ == "__main__":
    total = []
    for x in range(27, 30):
        total += get_valid_numbers(x, False)
    for x in range(3, 7):
        total += get_valid_numbers(x, False)

    print(total)
    strings = [valid_pw(str(num)) for num in total]
    print(sum([int(result) for result in strings]))
