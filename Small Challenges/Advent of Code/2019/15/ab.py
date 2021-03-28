from intcode import Program

DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

class Search:
    def __init__(self, inp, start = (0, 0)):
        self.bot = Program(inp)
        self.curr = start
        self.dirList = {self.curr: 0}
        self.expandList = [(0, self.curr, d, self.bot.get_state()) for d in range(len(DIRS))]
        self.goalPos = None

    def expand_next(self, sort = True):
        # Find closest point to expand
        if sort:
            self.expandList.sort(reverse = True, key = lambda x: x[0])
        nextTile = None
        dist = None
        delta = None

        while (nextTile == 0 or nextTile is None) and len(self.expandList) > 0:
            dist, pos, delta, bot_state = self.expandList.pop()

            # Skip if this tile has already been expanded
            self.curr = (pos[0] + DIRS[delta][0], pos[1] + DIRS[delta][1])
            if self.curr in self.dirList.keys():
                continue
            
            self.bot.program = bot_state[2]
            self.bot.base = bot_state[1]
            self.bot.pos = bot_state[0]
            self.bot.input = delta + 1

            # Run intcode to find response
            self.bot.run(stop = 4)
            self.bot.run(stop = 3)
            nextTile = self.bot.output

        if nextTile is not None and nextTile != 0:
            # Set optimal direction to get back to start
            self.dirList[self.curr] = DIRS[delta + (1 if delta % 2 == 0 else -1)]
            
            if nextTile == 2: # set goalpos if found
                self.goalPos = self.curr

            # Add adjascent tiles (if they haven't already been expanded)
            for i in range(len(DIRS)):
                nextPos = (self.curr[0] + DIRS[i][0], DIRS[i][1] + self.curr[1])
                if nextPos not in self.dirList.keys():
                    self.expandList.append((dist + 1, self.curr, i, self.bot.get_state()))

        return nextTile

    def expand_front(self, limit):
        self.expandList.sort(reverse = True, key = lambda x: x[0])
        while len(self.expandList) > 0 and self.expandList[-1][0] <= limit:
            expand_next(sort = false)

    def find_min_dist(self):
        # stop when list empty, or goal found
        while len(self.expandList) > 0:
            if self.expand_next() == 2:
                break

        # Backtrace to find distance
        dist = 0
        curr = self.goalPos
        while curr != (0, 0):
            curr = (curr[0] + self.dirList[curr][0], curr[1] + self.dirList[curr][1])
            dist = dist + 1

        return dist

    def find_max_dist(self):
        maxDist = 0
        # Explore all possible parts of the list
        while len(self.expandList) > 0:
            result = self.expand_next()
            if result == None or result == 0:
                break
            else:
                maxDist = self.expandList[-1][0]

        # The thinking here is that the last place to be explored will be a wall which is next to the furtherest point
        return maxDist

if __name__ == "__main__":
    searcherA = Search("input.txt")    
    print(searcherA.find_min_dist())

    searcherA.curr = searcherA.goalPos
    searcherA.dirList = {searcherA.curr: 0}
    searcherA.expandList = [(0, searcherA.curr, d, searcherA.bot.get_state()) for d in range(len(DIRS))]
    print(searcherA.find_max_dist())
