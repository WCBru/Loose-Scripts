# Note: No checking if number is valid
# Split by newline, cast to int, place in a list and sum over the list
if __name__ == "__main__":
    print(str(sum([int(val) for val in open("input.txt").read().split("\n")])))
