def sum_present(base, target):
    diffArray = [target - c for c in base]
    for c in range(len(base)):
        for c2 in range(c, len(base)):
            if c != c2:
                if diffArray[c] == base[c2]:
                    return True
    return False

if __name__ == "__main__":
    nums = [int(line) for line in open("input.txt").read().strip().split("\n")]
    current = nums[:25]
    nextReplace = 0

    for target in nums[25:]:
        if not sum_present(current, target):
            print(target)
            break
        else:
            current[nextReplace] = target
            nextReplace = (nextReplace + 1) % 25
        
