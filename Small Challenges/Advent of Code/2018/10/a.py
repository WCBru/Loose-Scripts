# Simply class to contain light and its properties
class Light:
    def __init__(self, sx, sy, vx, vy):
        self.x  = sx
        self.y = sy
        self.dx = vx
        self.dy = vy

    def forward(self):
        self.x += self.dx
        self.y += self.dy

    def back(self):
        self.x -= self.dx
        self.y -= self.dy

# Parse input into list of lights
def parse_input(doc_name):
    out_lst = [] # Output list
    doc = open(doc_name)
    line = doc.readline()
    
    while line != "":
        line_parts = line.split('<') # Split by beginning of tuple

        # Take the end of the tuple and split by comma
        pos = line_parts[1].split('>')[0].split(',')
        vel = line_parts[2].split('>')[0].split(',')
        
        new_light = Light(int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1]))
        out_lst.append(new_light)

        line = doc.readline()

    return out_lst

# Get size of the array (x, y) from a list of lights
def get_size(lst):
    xlst = sorted([light.x for light in lst])
    ylst = sorted([light.y for light in lst])
    return ( xlst[-1] - xlst[0] + 1, ylst[-1] - ylst[0] + 1 )

# Print board
def print_board(lst):
    sx, sy = get_size(lst)
    minx = min([light.x for light in lst])
    miny = min([light.y for light in lst])

    # Initialise all to .
    board = [["." for x in range(sx)] for y in range(sy)]

    # Change light positions to #
    for light in lst:
        board[light.y - miny][light.x  - minx] = "#"

    # Print row by row
    for row in range(len(board)):
        print("".join(board[row]))

    return (sx, sy)
    
# Strategy: Assume that lights need to move inwards and outwards
# So, print the lights at their minimum
if __name__ == "__main__":
    light_list = parse_input("input.txt")

    # Get an initial size and one iteration forward
    ini_x, ini_y = get_size(light_list)
    [light.forward() for light in light_list]
    
    size_x, size_y = get_size(light_list)
    prev_x = ini_x
    prev_y = ini_y

    # Safe catch at the original size
    while size_x < ini_x or size_y < ini_y:
        # If the previous is in any way absolutely smaller, past min.
        if size_x > prev_x or size_y > prev_y:
            print("Printing board")
            [light.back() for light in light_list] # Go back 1 to min.
            print_board(light_list)
            break
        else: # Advancement: replace prev. values and advance
            prev_x = size_x
            prev_y = size_y
            [light.forward() for light in light_list]
            size_x, size_y = get_size(light_list)
