WIDTH = 25
HEIGHT = 6
SIZE = WIDTH * HEIGHT

def count_occurs(layer, num):
    return sum([sum([i == num for i in row]) for row in layer])

if __name__ == "__main__":
    file = open("input.txt")
    data = file.read()
    file.close()

    layers = []
    for layer in range(len(data) // SIZE):
        layers.append([])
        layerData = data[layer * SIZE: (layer + 1) * SIZE]
        for row in range(len(layerData) // WIDTH):
            layers[-1].append([int(i) for i in
                                   layerData[WIDTH * row: WIDTH * (row + 1)]])

    sortedLayers = sorted(layers, key=lambda lay:count_occurs(lay, 0))
    print(count_occurs(sortedLayers[0], 1) * count_occurs(sortedLayers[0], 2))

    finalImage = [[2 for col in row] for row in layers[0]]

    for row in range(len(layers[0])):
        for col in range(len(layers[0][row])):
            for layer in range(len(layers)):
                if layers[layer][row][col] != 2:
                    finalImage[row][col] = layers[layer][row][col]
                    break

    for row in finalImage:
        print("".join([" " if i == 0 else "#" for i in row]))
    
    
