# Read input into a dict {pos: radius}
def gen_bot_lst(doc_name):
    output = {}
    doc = open(doc_name)
    line = doc.readline()

    # For each line
    while line != "":
        parts = line.split(", ") # Split line into parts

        # Extract position and radius
        pos = tuple([int(val) for val in parts[0][5:-1].split(",")])
        radius = int(parts[1].split("=")[1])

        # Add to output and get next line
        output[pos] = radius
        line = doc.readline()

    return output

# Function for getting Manhattan distance
def dist(pos1, pos2): # Hard coding size here
    return sum([abs(pos1[i]-pos2[i]) for i in range(3)])
    
if __name__ == "__main__":
    bot_list = gen_bot_lst("input.txt")

    # Get the bot with the largest radius
    best_bot = sorted(bot_list.keys(), key=lambda bot:bot_list[bot])[-1]
    best_bot_rad = bot_list[best_bot]

    # Count the number of bots within the best bot's range
    counter = 0
    for bot in bot_list.keys():
        counter += 1 if dist(best_bot, bot) <= best_bot_rad else 0

    print(counter)
