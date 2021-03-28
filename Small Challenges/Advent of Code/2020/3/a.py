if __name__ == "__main__":
    grid = open("input.txt").read().strip().split('\n')
    if not all([len(line) == len(grid[0]) for line in grid]):
        raise Exception("Jagged grid")

    width = len(grid[0])
    height = len(grid)

    for line in range(height):
        grid[line] = [c == '#' for c in grid[line]]

    x, y = (0, 0)
    trees = 0

    while y != (height - 1):
        x = (x + 3) % width
        y = (y + 1) % height

        trees += 1 if grid[y][x] else 0

    print(trees)
