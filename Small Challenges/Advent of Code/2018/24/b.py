TYPES = {"cold": 1, "slashing": 2, "fire": 3, "radiation": 4, "bludgeoning": 5}
LIMIT = 2 ** 100

# Class for group
class Group:
    def __init__(self, hp, numbers, dmg, dmg_type, ini, weak, immune,
                 virusState, booster = 0):
        self.hp = hp
        self.units = numbers
        self.maxUnits = numbers
        self.boost = booster
        self.dmg = dmg
        self.dmg_type = dmg_type
        self.initiative = ini
        self.weakto = weak
        self.immuneto = immune
        self.isVirus = virusState

    # Restore units to max units
    def heal(self):
        self.units = self.maxUnits

    # Set the boost to something else
    # Does not take effect if the virus flag is set
    # param newBoost: new boost to take effect
    def set_boost(self, newBoost):
        self.boost = 0 if self.isVirus else newBoost

    # Effective power
    # returns: Product of units and damage
    def power(self):
        return self.units * (self.dmg + self.boost)

    # Key for targetting order
    # param maxInitiative: Max initiative of the battle
    # returns: key that priporitises power over initiative
    def key(self, maxInitiative):
        return self.power() * (maxInitiative + 1) + self.initiative

    # Maximum possible damage that can be inflicted on this group
    # 0 if group has no units, else enemy power affected by types
    # param power: Effective power of enemy group
    # param attackType: Enemy's attack type (int)
    # returns: damage that would be inflicted on this group
    def dmg_possible(self, power, attackType):
        if self.units == 0:
            return 0
            
        return power * (2 if attackType in self.weakto else
                        (0 if attackType in self.immuneto else 1))    

    # If this unit can attack an enemy, pop and return the best enemy to attack
    # param targetList: List of targets (can be changed in function)
    # param maxInitiative: Max initiative of all groups, used to prioritise
    # returns: best Group to attack, or None if no damage can be done
    def pop_most_vulnerable(self, targetList, maxInitiative):
        # Skip if no targets left or this group has no units left
        if len(targetList) == 0 or self.units <= 0:
            return None

        # Get max power to prioritise, similar to maxInitiative
        maxPower = max([group.power() for group in targetList])
        if maxPower == 0: # return if no enemies have health
            return None

        # Sort the possible targets
        dmgScale = (maxInitiative + 1) * (maxPower + 1)
        powerScale = maxInitiative + 1
        targetList.sort(key=lambda target:
                        target.dmg_possible(self.power(), self.dmg_type) *
                        dmgScale + target.power() * powerScale + 
                        target.initiative)

        # Return the best target, if possible
        bestDamage = targetList[-1].dmg_possible(self.power(), self.dmg_type)
        return targetList.pop() if bestDamage > 0 else None

# Create the groups for a side
# Indexes are based on the input text
# param lines: lines of text containing side information
# param virus: Bool for if the group is a virus group
# returns: List of Group created from information
def gen_side(lines, virus):
    output = []

    for line in lines:
        parts = line.strip().split()
        
        units = int(parts[0])
        hp = int(parts[4])
        dmg = int(parts[-6])
        dtype = TYPES[parts[-5]] # convert str to int (see global var)
        init = int(parts[-1])
        weak_lst = []
        imm_lst = []

        if "(" in line and ")" in line:
            modifiers = line[line.index("(")+1: line.index(")")]
            
            for half in modifiers.split("; "):
                listParts = half.split()
                if listParts[0] == "immune":
                    imm_lst = [TYPES[t.strip(",")] for t in listParts[2:]]
                elif listParts[0] == "weak":
                    weak_lst = [TYPES[t.strip(",")] for t in listParts[2:]]
                else:
                    raise ValueError("Weak/Immune text not recognised")

        output.append(Group(hp, units, dmg, dtype, init,
                            weak_lst, imm_lst, virus))

    return output

# Generate the two sides based on the file name given
# param doc_name: name of text file with battle information
# returns: tuple of two lists: (immune, virus)
def gen_groups(doc_name):
    imm_sys = []
    vir_sys = []
    doc = open(doc_name)
    
    for info in doc.read().strip().split("\n\n"):
        lines = info.strip().split("\n")
        if lines[0].strip().split()[0] == "Immune":
            imm_sys = gen_side(lines[1:], False)
        elif lines[0].strip().split()[0] == "Infection:":
            vir_sys = gen_side(lines[1:], True)

    doc.close()

    return (imm_sys, vir_sys)

# Calculate the total units for a side
# param side: List of groups to count
# returns: Group collective units
def side_health(side):
    health = 0
    for group in side:
        health += group.units

    return health

# Carry out a battle for the given boost
# param immu: List of immune groups
# param viru: List of virus groups
# param maxInit: Maximum initiative for the battle
# param boost: Boost for immune system groups
# returns: True if the immune system wins, else false
def battle(immu, viru, maxInit):
    counter = 0
    # Battle until one side is left
    while side_health(immu) > 0 and side_health(viru) > 0:
        # Update every 1000 cycles
        #if counter % 1000 == 0:
        #    print([g.units for g in immu])
        #    print([g.units for g in viru])
        #counter += 1

        # Create order of targetting based on maxInitiative
        targetOrder = sorted(viru + immu,
                             key=lambda group: group.key(maxInit), reverse=True)
        #print([g.power() for g in targetOrder])
        
        attacks = {} # Attack mapping attacker to target
        immuTargets = immu[:]
        viruTargets = viru[:]
        for group in targetOrder:
            attacks[group] = group.pop_most_vulnerable(
                immuTargets if group.isVirus else viruTargets, maxInit)
        # End for

        
        attackHappened = False # Prevent stalemates
        
        # Carry out attacks
        for group in sorted(targetOrder, key=
                            lambda group: group.initiative, reverse=True):
            target = attacks.get(group)
            if target != None:
                unitsLost = min(target.units, # Limit units lost to unit count
                                target.dmg_possible(group.power(), group.dmg_type) \
                                // target.hp)

                attackHappened = True if attackHappened or unitsLost > 0 \
                                 else False # Set if any attacks happen
                                 
                #print(-unitsLost)
                target.units -= unitsLost
        # End for

        # If stalemate detected, count as loss
        if not attackHappened:
            return False
    '''
        for ind in range(-len(immu), 0):
            if immu[ind].units <= 0:
                immu.pop(ind)

        for ind in range(-len(viru), 0):
            if viru[ind].units <= 0:
                viru.pop(ind)
    '''
    # End while

    #print((side_health(immu), side_health(viru)))
    return side_health(immu) > 0

if __name__ == "__main__":
    immuneSys, viruses = gen_groups("input.txt")
    initMax = max([group.initiative for group in immuneSys + viruses])

    ''' # Naive method - still works
    booster = 0
    while not battle(immuneSys, viruses, initMax):
        booster += 1
        [group.set_boost(booster) for group in immuneSys]
        [group.heal() for group in immuneSys + viruses]
        
    print(side_health(immuneSys))
    
    '''
    
    booster = 0
    delta = LIMIT
    while delta > 0 and booster < LIMIT:
        [group.set_boost(booster + delta) for group in immuneSys] # set boost
        if not battle(immuneSys, viruses, initMax): # Simulate battle
            booster += delta
        [group.heal() for group in immuneSys + viruses] # Heal
        delta //= 2
    
    booster += 1 # Add 1 to boost, since search will be too low
    [group.set_boost(booster) for group in immuneSys]
    battle(immuneSys, viruses, initMax)
    print(side_health(immuneSys))
