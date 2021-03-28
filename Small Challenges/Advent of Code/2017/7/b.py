import sys

def findTowerWeight(root, mapping):
    weights = []
    if len(mapping[root][1]) == 0:
        return mapping[root][0]
    else:
        for child in mapping[root][1]:
            weights.append(findTowerWeight(child, mapping))
        for tower in range(len(weights)):
            if weights[tower] != weights[tower-1]:
                childWeights = []
                for child in mapping[root][1]:
                    childWeights.append(mapping[child][0])
                print("Weight MisMatch Detected!")
                print("Current Weight: " + str(mapping[root][0]))
                print("Children: " + str(weights))
                print("1st Child Weights: " + str(childWeights))
                
                sys.exit()
        return len(weights)*weights[0] + mapping[root][0]

if __name__ =="__main__":
    base = "rqwgj" # Determined from previous section
    childMap = {}
    
    indata = open("data7.txt", "r")
    data = indata.readline()
    while data != "":
        rawdata = data.split()
        name = rawdata[0]
        newchildren = []
        weight = int(rawdata[1][1:-1])
        if len(rawdata) > 2:
            children = rawdata[3:]
            for child in children:
                if child[-1] == ",":
                    child = child[:-1]
                newchildren.append(child)
        childMap[name] = (weight, newchildren[:])

        
        data = indata.readline()
    findTowerWeight(base, childMap)
    
