from intcode import Program

if __name__ == "__main__":
    camera = Program("input.txt")
    camera.run(stop = 3)

    grid = camera.get_outputs()
    gridStr = ''.join([chr(x) for x in grid])
    print(gridStr)

    # assumes bot doesnt start on intersection
    gridRows = gridStr.strip().split('\n')
    total = 0
    for row in range(1, len(gridRows) - 1):
        for col in range(1, len(gridRows[row]) - 1):
            if gridRows[row][col] == '#':
                if (gridRows[row + 1][col] == '#' and
                    gridRows[row - 1][col] == '#' and
                    gridRows[row][col - 1] == '#' and
                    gridRows[row][col + 1] == '#'):
                    total += row * col

    print(total)
