from random import randint

if __name__ == "__main__":
    inputs = []
    nextStr = "Hello"
    while nextStr != "":
        nextStr = input().strip()
        inputs.append(nextStr)
    inputs.pop()
    rolls = [[randint(0, int(die.split("d")[1])) for x in range(int(die.split("d")[0]))] for die in inputs]
    print("\n".join([str(sum(results)) + ": " + ", ".join([str(num) for num in results]) for results in rolls]))
