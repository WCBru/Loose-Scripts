if __name__ == "__main__":
    # General Approach:
    # Track a one level compression: use the fact that it alternates
    # And store how many of the next digit is used
    # There are better ways to compress but this is fine

    seqIndex = 1 # index in seq list
    seqRem = 1 # How much is left to use from seq list
    seq = [1,2] # 1-level compress sequence
    total = 3 #  Total number in the seq

    limit = int(input("Enter sequence length: "))

    while total < limit:
        # Append how many numbers were added, and add to total
        seq.append(2-((seqIndex+1)%2))
        total += seq[-1]

        if seqRem <2: # move to next number if finished with current count
            seqIndex += 1
            seqRem = seq[seqIndex]
        else: # stay on current number, but decrement
            seqRem -= 1

    if total > limit: # subtract 1 if total exceeds what was desired
        total -= 1
    oneSum = sum(seq[0::2])
    print(str(oneSum) + ":" + str(sum(seq)-oneSum))
