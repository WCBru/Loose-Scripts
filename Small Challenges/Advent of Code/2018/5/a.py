def check_letters(letter1, letter2):
    return letter1 != letter2 and letter1.upper() == letter2.upper()

if __name__ == "__main__":
    # Split into letters
    chain = list(open("input.txt").read().strip())

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
        if no_change: # All done: break
            break
        else:
            chain = list("".join(chain))

    print(len(chain))
                
