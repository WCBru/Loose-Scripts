BASE = [0, 1, 0, -1]

def generate_patterns(length, limit):
    output = []
    baseline = BASE[:]
    for i in range(length // len(BASE)):
        baseline.extend(BASE)

    baseline = baseline[0:length + 1]
    output.append(baseline[1:length + 1])

    for lst in range(1, limit):
        nextList = []
        for elm in range(len(baseline)):
            nextList.append(baseline[elm])
            for repeat in range(lst):
                nextList.append(baseline[elm])

            if len(nextList) > length:
                output.append(nextList[1:length + 1])
                break

    return output

def apply_patterns(start, patterns):
    output = []
    for pat in patterns:
        output.append(round(abs(sum(
            [start[i] * pat[i] for i in range(len(pat))]))) % 10)

    return output

if __name__ == "__main__":
    signal = [int(x) for x in open("input.txt").read().strip()]
    patterns = generate_patterns(len(signal), len(signal))
    coeffs = signal[:]

    x = time.time()
    for i in range(100):
        coeffs = apply_patterns(coeffs, patterns)

    print(''.join([str(x) for x in coeffs[:8]]))
