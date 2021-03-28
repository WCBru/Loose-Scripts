if __name__ == "__main__":
    fileIn = open("input.txt", 'r').read().strip()
    numbers = sorted([int(x) for x in fileIn.split('\n')])
    for a in range(len(numbers) - 3, 0, -1):
        for b in range(len(numbers) - 2, a, -1):
            for c in range(len(numbers) - 1, b, -1):
                curr = numbers[a] + numbers[b] + numbers[c]
                if curr < 2020:
                    break
                elif curr == 2020:
                    print(numbers[a] * numbers[b] * numbers[c])
                    raise Exception("")
