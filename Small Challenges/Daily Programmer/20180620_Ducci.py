if __name__ == "__main__":
    # Handle input and create record of previous tuples
    current = [int(num) for num in input("Enter tuple: ").strip()[1:-1].split(", ")]
    checked = []

    # Append new tuple and do abs diff
    # The same list recycled for each iteration, with records saved as tuples
    while tuple(current) not in checked and not all([num == 0 for num in current]):
        checked.append(tuple(current))
        for elm in range(-len(current), 0):
            current[elm] = abs(checked[-1][elm] - checked[-1][elm+1])

    # Add last step and print results
    checked.append(tuple(current))  
    for step in checked:
        print(step)
    print(str(len(checked)), "steps")
