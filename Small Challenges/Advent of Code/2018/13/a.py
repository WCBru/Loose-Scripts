CART_TILES = ["^", ">", "v", "<"]
DEBUG_GENERAL = False
DEBUG_TRACKS = False
DEBUG_MOVEMENT = False

# Get adjascent points for the tile given
# Order: UP, RIGHT, DOWN, LEFT
# Each option takes from the above order
# For corner tiles, an additional flag for if the tile is connected at the top
def get_points(x,y,tile, up_tile=None):
    tiles_from_true_north = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]

    if tile == "+":
        return tiles_from_true_north
    elif tile == "-":
        return tiles_from_true_north[1::2]
    elif tile == "|":
        return tiles_from_true_north[::2]
    elif up_tile == None:
        raise ValueError("Need to define tile above for diagonal tile")
    else:
        if tile == "\\" and up_tile:
            return tiles_from_true_north[0:2]
        elif tile == "\\":
            return tiles_from_true_north[2:]
        elif tile == "/" and up_tile:
            return tiles_from_true_north[::3]
        elif tile == "/":
            return tiles_from_true_north[1:3]
        else:
            raise ValueError("Tile not recognised: {0}".format(tile))

# Detects if two carts have collided
# Does so by keeping track of encountered locations, returns true if one is
# Encountered twice
def collosion(lst):
    counted = []
    for cart in lst:
        if cart.get_pos() in counted:
            return True
        else:
            counted.append(cart.get_pos())
            
    return False

# Class for each segment of track
class Track:
    def __init__(self, x, y, tile, up_tile):
        self.x = x
        self.y = y
        self.tile = tile

        # Check if above tile connected to this one
        up_conn = False # Flag for if connected at the top
        if up_tile != None:
            up_conn = (x,y) in up_tile.endpoints # Above tile's endpoints
        
        self.endpoints = get_points(x,y,tile, up_conn)
        
        if DEBUG_TRACKS: # Print tile characteristics
            print("Track {0} at {1} with endpoints {2}".format(
                tile, (x,y), self.endpoints))

    # Get next point based on previous point and counter (for intersections)
    def get_next_endpoint(self, prev_pos, counter):
        # Determine intersection direction (0 -> 2 ==> left -> right)
        # If not at intersection, resolves to 0, and is redundant
        int_dir = counter%(len(self.endpoints)-1)

        # Take prev_tile, go to next endpoint (which is a left turn)
        # And then add the intersection direction above
        next_t = self.endpoints[(self.endpoints.index(prev_pos) + 1 + int_dir)
                              % len(self.endpoints)] # Prevent overrflow

        if DEBUG_MOVEMENT:
            print("From {0} to {1}, for {2}, advance to {3}".format(
                prev_pos, (self.x, self.y), self.tile, next_tile))
            
        return next_t
        
# Cart class
class Cart:
    def __init__(self,x, y, char):
        self.x = x
        self.y = y
        self.dir_counter = 0 # Intersection direction counter
        self.prev_tile = self.set_initial_prev(x,y,char)

    # Get postition as tuple
    def get_pos(self):
        return (self.x, self.y)

    # Sets the intial previous position
    # Based on the intial character given
    def set_initial_prev(self,x,y,tile):
        if tile == "v":
            return (x,y-1)
        elif tile == "^":
            return (x, y+1)
        elif tile == ">":
            return (x-1, y)
        elif tile == "<":
            return (x+1, y)
        else:
            raise ValueError("Cart tile not recognised: {0}".format(tile))

    # Advance the cart. Interally tracks intersection turn direction
    def advance(self, track):
        new_pos = track.get_next_endpoint(self.prev_tile, self.dir_counter)
        self.prev_tile = self.get_pos() # Set previous tile to current
        self.x, self.y = new_pos # Set current position to next tile

        # If advanced passed intersection, increment direction counter
        self.dir_counter = ((self.dir_counter + 1) % 3
                            if track.tile == "+" else self.dir_counter)

# Main function
if __name__ == "__main__":
    # BEGIN Parsing Input
    doc = open("input.txt")
    line = doc.readline()
    tracks = {} # (x,y): Track object
    carts = [] # List of Cart objects
    row = 0 # Tracks the current row (y)
    while line != "":
        # For each char in a line (x)
        for char in range(len(line)):
            if not line[char].isspace(): # Exclude " " and "\n"
                track_char = line[char] # Input char

                # If a cart was found
                if track_char in CART_TILES:
                    carts.append(Cart(char, row, track_char))
                    re_char = ("|" if CART_TILES.index(track_char) % 2 == 0
                               else "-") # Replace cart tile char
                    
                    if DEBUG_GENERAL:
                        print("Cart found at {0}: {1} => {2}".format(
                            (char,row), track_char, re_char))
                        
                    track_char = re_char # Replace char

                # Add track to list of tracks
                # Last argument: track above (or None if it doesn't exist)
                # Used for determining "/" or "\" endpoints
                tracks[(char, row)] = Track(char , row, track_char , tracks.get((char, row-1)))

        # Advance to next line
        line = doc.readline()
        row += 1
    # END Parsing Input

    if DEBUG_GENERAL:
        print("Tracks: {0}, Carts: {1}".format(len(tracks), len(carts)))

    maxx = max([cart.x for cart in carts]) # Max x co-ord
    cont = True # Flag for continuing iteration
    while cont:
        # Iterate carts in of L -> R, U -> D
        for cart in sorted(carts, key=lambda c: c.y*maxx + c.x):
            # Advance cart and check for collisions
            cart.advance(tracks[cart.get_pos()])

            # If a collosion occurs, print current cart co-ord
            # Since this is where the collision must have occurred
            if collosion(carts):
                print((cart.x, cart.y))
                
                if DEBUG_GENERAL:
                    print([c.get_pos() for c in carts])

                cont = False
                break # Break for loop
            
