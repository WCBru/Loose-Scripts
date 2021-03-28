def first_service(start, mult):
    factor = start // mult
    if mult * factor == start:
        return start
    else:
        return (factor + 1) * mult

if __name__ == "__main__":
    start, servs = open("input.txt").read().split("\n", 2)
    start = int(start)

    times = []
    for num in servs.split(','):
        if num != 'x':
            times.append((int(num), first_service(start, int(num))))

    times.sort(key=lambda x: x[1])
    print(times[0][0] * (times[0][1] - start))
