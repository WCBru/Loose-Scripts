def sgn(num):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    else:
        return 1

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

if __name__ == "__main__":
    moonLst = create_moons("input.txt")

    for x in range(1000):
        [moon.calc_acc(moonLst) for moon in moonLst]
        [moon.move() for moon in moonLst]

    print(sum([moon.totalEnergy() for moon in moonLst]))
