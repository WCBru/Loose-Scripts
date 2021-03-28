if __name__ == "__main__":
    scores = [0 for x in range(5)] # zeroes
    tally = input("Enter scores: ").strip()
    for char in tally:
        try:
            entry = (ord(char)-64)%32
            scores[entry-1] += 1 if ord(char) > 95 else -1
        except:
            pass

    outLst = []
    for person in range(len(scores)):
        outLst.append(chr(97+person) + ":" + str(scores[person]))
    print(", ".join(sorted(outLst, key= lambda x: int(x[2:]), reverse = True)))
