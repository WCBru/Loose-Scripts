# Check if letters differ only by type-case
def check_letters(letter1, letter2):
    return letter1 != letter2 and letter1.upper() == letter2.upper()

# Get length from completely reacting letters
def get_length_reduced(lst):
    chain = lst
    while True:
        index = 0
        no_change = True

        # Remove reactive letters
        while index < len(chain) - 1:
            if (check_letters(chain[index], chain[index+1])):
                chain[index] = ""
                chain[index+1] = ""
                index += 1
                no_change = False
            index += 1

        # Update Chain
        if no_change: # No changes: break
            break
        else:
            chain = list("".join(chain))

    print(len(chain))
    return len(chain)

# Create a copy of the given list with all of a certain letter
# (regardless of case) removed
def remove_letter_from_list(lst, target):
    print(target)
    newlst = lst[:]

    # Convert matches to empty strings
    for index in range(len(newlst)):
        if newlst[index].upper() == target.upper():
            newlst[index] = ""

    # Return list without empty strings
    return list("".join(newlst))

if __name__ == "__main__":
    # Split into letters
    chain = list(open("input.txt").read().strip())

    # Iterate over A - Z
    # Get the min length after removing a letter
    print(min([get_length_reduced(remove_letter_from_list(chain, chr(num))) for num in range(65, 91)]))
                
