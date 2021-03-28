# Plan: Calculate 3 axes seperately
# Use hashed sets for fast lookup of visited states
# Simulate forward to find the first duplicated set
# This gives the cycle length and steps to reach the cycle
# Answer is lowest common multiple of cycles + highest steps to start a cycle

def sgn(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    elif a == b:
        return a
    elif a == 0:
        if b == 0:
            return 1
        else:
            return b
    elif b == 0:
        return a
    else:
        rem = a % b
        if rem == 0:
            return b
        else:
            return gcd(b, rem)

def lcm(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        output = lst[0] * lst[1] // gcd(lst[0], lst[1])
        if len(lst) > 2:
            return lcm([output] + lst[2:])
        else:
            return output

class Moon:
    def __init__(self, lineIn):
        commaSep = lineIn.strip()[1:-1].split(",")
        fullSep = [part.split("=") for part in commaSep]
        self.pos = [int(part[1]) for part in fullSep]
        self.vel = [0, 0, 0]

    def calc_acc(self, moons):
        for moon in moons:
            self.vel = [self.vel[i] + sgn(moon.pos[i] - self.pos[i])
                        for i in range(3)]

    def move(self):
        self.pos = [self.pos[i] + self.vel[i] for i in range(3)]

    def pot(self):
        return sum([abs(coord) for coord in self.pos])

    def kin(self):
        return sum([abs(coord) for coord in self.vel])

    def totalEnergy(self):
        return self.pot() * self.kin()
        
def create_moons(filename):
    moons = []
    
    file = open(filename)
    line = file.readline()
    while line.strip() != "":
        moons.append(Moon(line))
        line = file.readline()

    return moons

def axis_update(lst):
    hLen = len(lst) // 2
    for i in range(hLen):
        lst[hLen + i] += sum([sgn(lst[j] - lst[i]) for j in range(hLen)])
    for i in range(hLen):
        lst[i] += lst[hLen + i]

    return lst
        

def get_cycles(lst, ind):
    start = [moon.pos[ind] for moon in lst] + [moon.vel[ind] for moon in lst]
    moonData = start[:]
    states = set()
    tup = tuple(moonData)

    # Find the first repeat
    # Using sets speeds up checking (hashing?)
    while tup not in states:
        states.add(tup)
        moonData = axis_update(moonData)
        tup = tuple(moonData)
        

    repIndex = 0
    while start != moonData:
        start = axis_update(start)
        repIndex += 1
    
    return (len(states) - repIndex, repIndex)
    

if __name__ == "__main__":
    moonLst = create_moons("input.txt")
    cycles = []
    for i in range(3):
        cycles.append(get_cycles(moonLst, i))

    print("LCM of cycles + max of offsets")
    print(lcm([c[0] for c in cycles]) + max([c[1] for c in cycles]))
