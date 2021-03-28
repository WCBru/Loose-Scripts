def solve(line):
    mark = 0
    index = 0
    level = 0
    
    multlist = []
    add = None
    level = 0
    digitflag = False
    while index < len(line):
        if level > 0:
            if line[index] == '(':
                level += 1
            elif line[index] == ')':
                level -= 1

            if level <= 0:
                num = solve(line[mark:index] + " ")
                if add:
                    multlist[-1] += num
                else:
                    multlist.append(num)
        elif line[index].isdigit():
            if not digitflag:
                mark = index
                digitflag = True
        elif line[index] == '+':
            add = True
        elif line[index] == '*':
            add = False
        elif line[index] == ' ':
            if digitflag:
                num = int(line[mark:index])
                if add:
                    multlist[-1] += num
                else:
                    multlist.append(num)
                digitflag = False
        elif line[index] == '(':
            level += 1
            mark = index + 1
        
        index += 1

    total = 1
    for num in multlist:
        total *= num
    return total
        
if __name__ == "__main__":
    results = []
    for line in open("input.txt").read().split("\n"):
        results.append(solve(line + " "))

    print(sum(results))
