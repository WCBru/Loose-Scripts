import urllib.request
import json, math

def rad(deg):
    return float(deg*math.pi/180);

def genlimits(origin, dist):
    longRatio = 111111*math.cos(rad(origin[0]))
    limits = [origin[0] - dist/111111, origin[0] + dist/111111,
              origin[1] - dist/longRatio, origin[1] + dist/longRatio]
    limitStrings = ["lamin=", "lamax=", "lomin=", "lomax="]
    for x in range(4):
        limitStrings[x] += str(float(limits[x]))
    return "?" + "&".join(limitStrings)

def getDist(origin, lat, long):
    longRatio = 111111*math.cos(rad(origin[0]))
    return ((origin[0]-lat)**2 + (origin[1]-long)**2)**0.5

def printInfo(origin, planeList):
    print(str(getDist(origin, planeList[6], planeList[5])))
    print(planeList[1])
    print(", ".join([str(planeList[6]), str(planeList[5])]))
    print(str(planeList[7]) + "\n" + planeList[2] + "\n" + str(planeList[0]))
    

if __name__ == "__main__":
    coords = [input("Enter Lat: ").strip().split()]
    coords.append(input("Enter Long: ").strip().split())
    coeff = [1 if coords[0][1] == "N" else -1]
    coeff.append(1 if coords[1][1] == "E" else -1)
    coords = [float(coords[i][0])*coeff[i] for i in range(2)]

    for power in range(2,5): # search 100 m to 100 km
        print("Distance: " + str(10**power))
        loclimit = genlimits(coords, 10**power)
        rawJson = urllib.request.urlopen("https://opensky-network.org/api/states/all" + loclimit)
        decoded = json.loads(rawJson.read().decode()).get("states")
        
        if decoded == None:
            continue
        else:
            # Get rid of planes missing Geo data
            infoOnly = []
            for plane in decoded:
                if plane[5] == None or plane[6] == None or plane[7] == None:
                    continue
                else:
                    infoOnly.append(plane)

            # Find closest plane and print info
            infoOnly.sort(key=lambda x: getDist(coords, x[6], x[5]))
            printInfo(coords, infoOnly[0])
            break
    else:
        print("No Planes found within a 100 km square of target location")
