INPUT = 681901
START = [3,7]

if __name__ == "__main__":
    scores = START[:] # Hard copy - prevent reference issues

    # Starting indicies
    ind1 = 0
    ind2 = 1

    # Keep going until enough recipes are generated
    while len(scores) < INPUT + 10:
        # Get digits: turn into string and turn each char into an int
        digit_list = [int(char) for char in
                      list(str(scores[ind1]+scores[ind2]))]
        scores += digit_list # Add new digits

        # Advance indicies
        ind1 = (ind1+scores[ind1]+1)%len(scores)
        ind2 = (ind2+scores[ind2]+1)%len(scores)

    # Print output
    print("".join([str(digit) for digit in scores[INPUT:INPUT+10]]))
