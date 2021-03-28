if __name__ == "__main__":
    fileIn = open("input.txt", 'r').read().strip()
    numbers = sorted([int(x) for x in fileIn.split('\n')])
    for a in range(len(numbers) - 2, 0, -1):
        for b in range(len(numbers) - 1, a, -1):
            curr = numbers[a] + numbers[b]
            if curr < 2020:
                break
            elif curr == 2020:
                print(numbers[a] * numbers[b])
                raise Exception("")
