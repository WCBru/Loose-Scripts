if __name__ == "__main__":
    jolts = [0] + [int(x) for x in open("input.txt").read().strip().split("\n")]
    ones = 0
    threes = 1
    jolts.sort()

    for j in range(1, len(jolts)):
        ones += int(jolts[j] - jolts[j - 1] == 1)
        threes += int(jolts[j] - jolts[j - 1] == 3)
        

    print(ones * threes)
