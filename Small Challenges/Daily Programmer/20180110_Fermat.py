import math
import random

def powMod(num, tar):
    return math.pow(num, tar)%tar

if __name__ == "__main__":
    target, prob = input("Enter input: ").split()
    target = int(target)
    prob = float(prob)
    cycles = math.ceil(math.log(1-prob, 0.5))
    usedNum = []

    for x in range(cycles):
        num = random.randint(1, target -1)
        while num in usedNum:
            num = random.randint(1, target -1)
        if pow(num, target, target) != num:
            print(False)
            break
        else:
            usedNum.append(num)
    else:
        print(True)
        
    
