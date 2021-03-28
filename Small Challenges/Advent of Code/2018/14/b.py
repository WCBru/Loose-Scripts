INPUT = 681901
START = [3,7]

# This soln uses strings instead of lists
if __name__ == "__main__":
    scores = "".join([str(num) for num in START])
    input_list = str(INPUT)
    input_len = len(input_list)

    # Starting indicies
    ind1 = 0
    ind2 = 1

    # Keep going until break
    # For some reason, comparing more elements makes it go faster
    while input_list not in  scores[-(input_len+1):]:
        # Convert sum of digits into string and append
        scores += str(int(scores[ind1])+int(scores[ind2])) # Add new digits

        # Advance indicies if no match yet
        ind1 = (ind1+int(scores[ind1])+1)%len(scores)
        ind2 = (ind2+int(scores[ind2])+1)%len(scores)

    print(len(scores)-input_len-1)
