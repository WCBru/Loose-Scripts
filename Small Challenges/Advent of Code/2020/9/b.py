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
    errVal = None

    for target in nums[25:]:
        if not sum_present(current, target):
            errVal = target
            break
        else:
            current[nextReplace] = target
            nextReplace = (nextReplace + 1) % 25
        

    integral = [nums[0] for x in range(len(nums) + 1)]
    for n in range(1, len(nums)):
        integral[n] = integral[n - 1] + nums[n - 1]

    for lower in range(len(nums)):
        for upper in range(lower + 1, len(nums)):
            if integral[upper] - integral[lower] == errVal:
                ran = nums[lower:upper + 1]
                print(min(ran) + max(ran))
                
                raise Exception("Done")
