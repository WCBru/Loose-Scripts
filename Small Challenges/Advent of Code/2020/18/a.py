def solve(line):
    mark = 0
    index = 0
    total = 0
    add = None
    level = 0

    digitflag = False
    while index < len(line):
        if level != 0:
            if line[index] == '(':
                level += 1
            elif line[index] == ')':
                level -= 1

            if level <= 0:
                num = solve(line[mark:index] + " ")
                if add == None:
                    total = num
                else:
                    total = (total + num) if add else (total * num)
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
                if add == None:
                    total = num
                elif digitflag:
                    total = (total + num) if add else (total * num)
                digitflag = False
        elif line[index] == '(':
            level += 1
            mark = index + 1
        
        index += 1

    return total
        
if __name__ == "__main__":
    results = []
    for line in open("input.txt").read().split("\n"):
        results.append(solve(line + " "))

    print(sum(results))
