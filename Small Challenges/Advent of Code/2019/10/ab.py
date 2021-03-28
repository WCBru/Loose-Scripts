# Generate the vector to get from asteroid to another
# Reduce by the GCD, store in a set (to remove unique elements
# Count the number of elements in the set for the number of visible asteroids
# Repeat for all asteroids
# Ignores the current asteroid being assessed when counting visible asteroids

import math

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

def get_asteroid_locations(fileName):
    output = []
    file = open(fileName)
    line = file.readline()
    row = 0
    while line != "":
        for i in range(len(line.strip())):
            if line[i] == "#":
                output.append((i, row))

        row += 1
        line = file.readline()

    return output

# 2D only
def reduced_vector(pt1, pt2):
    vect = [pt2[i] - pt1[i] for i in range(2)]
    fact = gcd(abs(vect[0]), abs(vect[1]))
    return tuple([coord//fact for coord in vect])

def get_visible(astList, pt):
    vectSet = set()
    for ast in astList:
        # Skip if is point being tested
        if ast == pt:
            continue

        # Will not add dupes
        vectSet.add(reduced_vector(ast, pt))

    return len(vectSet)

def dec_and_remove(lst, amount):
    newDict = {}
    for key in lst.keys():
        if lst[key] > amount:
            newDict[key] = lst[key] - amount
        elif lst[key] < amount:
            raise ValueError("Sightline calculation error")

    return newDict

def true_bearing(v):
    ang = math.atan2(-float(v[1]), float(v[0]))
    return math.fmod((5 * math.pi / 2) - (ang if ang >= 0 else (2 * math.pi + ang)),
                     2 * math.pi)

def get_vape_coords(astList, pt, num):
    # Count the number of asteroids in each sightline
    vectCounts = {}
    for ast in astList:
        if ast != pt:
            vect = reduced_vector(pt, ast)
            if vect in vectCounts:
                vectCounts[vect] += 1
            else:
                vectCounts[vect] = 1

    print("Sights Counted")
    destroyed = 0
    rotations = 0
    while (destroyed + len(vectCounts)) < num and len(vectCounts) > 0:
        minSights = min([vectCounts[ast] for ast in vectCount])

        # Remove the lowest sightline count 
        if len(vectCounts) * minSights + destroyed < num:
            destroyed += len(vectCounts) * minSights
            vectCounts = dec_and_remove(vectCounts, minSights)
            rotations += minSights
        # Trim off 1 rotation
        else:
            destroyed += len(vectCounts)
            vectCounts = dec_and_remove(vectCounts, 1)
            rotations += 1

    # Final rotation - sort vectors by bearing
    vectOrdered = sorted(vectCounts.keys(), key=lambda vect: true_bearing(vect))
    #print(vectOrdered)
    sLine = vectOrdered[num - destroyed - 1]
    print("Sight Line: " + str(sLine))
    
    currentPt = pt
    encounters = 0
    while encounters <= rotations:
        currentPt = (currentPt[0] + sLine[0], currentPt[1] + sLine[1])
        encounters += 1 if currentPt in astList else 0

    return currentPt

if __name__ == "__main__":
    astLocs = get_asteroid_locations("input.txt")
    visList = [get_visible(astLocs, ast) for ast in astLocs]
    print(max(visList))
    bestPt = astLocs[visList.index(max(visList))]
    print(bestPt)
    
    coord = get_vape_coords(astLocs, bestPt, 200)
    print(coord[0] * 100 + coord[1])
    

    
