def count_trees(grid, right, down):
    x, y = (0, 0)
    trees = 0

    while y != (height - 1):
        x = (x + right) % width
        y = (y + down) % height

        trees += 1 if grid[y][x] else 0

    return trees

    

if __name__ == "__main__":
    grid = open("input.txt").read().strip().split('\n')
    if not all([len(line) == len(grid[0]) for line in grid]):
        raise Exception("Jagged grid")

    width = len(grid[0])
    height = len(grid)

    for line in range(height):
        grid[line] = [c == '#' for c in grid[line]]

    prod = 1
    for m in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        prod *= count_trees(grid, m[0], m[1])
    print(prod)
