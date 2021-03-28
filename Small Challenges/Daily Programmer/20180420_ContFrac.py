# This works a little differently from the challenge:
# The Gaussian form is taken comma-delimited. This is rectifed in-script
# Fractions are interpretted as a 2-tuple of numerator then denominator

def gauss2frac(nums):
    output = (1,1)
    if len(nums) > 1:
        output = (1,nums.pop()) # First number

        # This creates the next fraction up based on the current fraction
        # And the next number in the list
        while len(nums) > 1:
            output = (output[1],output[1]*nums.pop() + output[0])
    
    # Return last number
    return (output[0] + (nums.pop() * output[1]), output[1])
    

def frac2gauss(frac):
    output = []
    current = frac

    # Add the div of the fraction to the list, next fraction is
    # The denominator on the remainder of the num. on denom.
    while current[1] > 1:
        output.append(current[0]//current[1])
        current = (current[1], current[0]%current[1])
    output.append(current[0]//current[1]) # Add last number
    
    return output

if __name__ == "__main__":
    target = input("Enter input: ").strip()
    for char in range(len(target)):
        if target[char] == ";":
            target = target[:char] + "," + target[char+1:]
    targetNums = [int(num) for num in target[1:-1].split(",")]

    # Gaussian detected    
    if target[0] == "[" and target[-1] == "]":
        frac = gauss2frac(targetNums)
        print(str(frac))
        print("\\frac{" + str(frac[0]) + "}{" + str(frac[1]) + "}")
    # Fraction detected
    elif target[0] == "(" and target[-1] == ")":
        target = tuple(targetNums)
        gauss = frac2gauss(target)
        print(str(gauss))

        # Print in LaTeX form
        outStr = str(gauss[0])
        for num in gauss[1:]:
            outStr += "+\\frac{1}{" + str(num)
        for num in gauss[1:]:
            outStr += "}"
        print(outStr)

    # Unrecognised input
    else:
        print("Input not recognised")
