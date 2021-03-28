# ceil(a / b)
def ceil(a, b):
    if a % b == 0:
        return a//b
    else:
        return (a//b) + 1

class Receipe:
    def __init__(self, line):
        equation = line.split(" => ")
        div, prod = equation[1].split(" ", 2)
        self.pQuant = int(div)
        self.pName = prod
        self.ingreds = []
        for ingred in equation[0].split(", "):
            quant, name = ingred.split(" ", 2)
            self.ingreds.append((name, int(quant)))

def get_reactions(filename):
    output = {}

    file = open(filename)
    line = file.readline().strip()
    while line != "":
        newRec = Receipe(line)
        output[newRec.pName] = newRec
        line = file.readline().strip()

    file.close()
    return output

def get_tiers(recp):
    tiers = {"ORE": 0}
    while len(tiers) <= len(recp):
        for rec in recp.keys():
            if rec not in tiers and all(
                [ing[0] in tiers for ing in recp[rec].ingreds]):
                
                tiers[rec] = max([tiers[ing[0]] for ing in recp[rec].ingreds]) + 1

    return tiers

if __name__ == "__main__":
    reactList = get_reactions("input.txt")
    tiers = get_tiers(reactList)
    reqList = {elm: 0 for elm in tiers}
    tierGroups = {}
    for i in range(tiers["FUEL"] + 1):
        tierGroups[i] = []
        for elm in tiers:
            if tiers[elm] == i:
                tierGroups[i].append(elm)

    reqList["FUEL"] = 1
    tier = tiers["FUEL"]
    while tier > 0:
        for chem in tierGroups[tier]:
            if reqList[chem] > 0:
                lotsNeeded = ceil(reqList[chem], reactList[chem].pQuant)
                # Add ingredients to required list
                for name, quant in reactList[chem].ingreds:
                    reqList[name] += quant * lotsNeeded
        
        tier -= 1
    
    print(reqList["ORE"])
