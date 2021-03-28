def find_near_match(lst):
    if len(lst) < 2:
        return ""

    # Compare words raw
    count = 1 # Counter to reduce redundant checks
    for word1 in lst[:-1]:
        for word2 in lst[count:]:
            # Check for matching lengths
            if len(word1) != len(word2):
                continue
            
            disc = False # Discrepancy
            outstr = "" # Output if near matched
            
            # Check letter by letter
            for ind in range(len(word1)):
                # If letter matches, append letter
                if word1[ind] == word2[ind]:
                    outstr = outstr + word1[ind]
                else: # Else check if a mismatch has already occurred
                    if disc: # Has occurred, move to next pair
                        break
                    else: # Has not, set to has occurred
                        disc = True
            else:
                if disc: # Only 1 mismatch
                    return outstr
        count += 1
    else: # If not suitable candidate
        return ""         
            
def bin_letters(lst, index):
    bins = [[] for i in range(26)]
    
    for string in lst:
        # Add the current ID to the bin based on the index
        # Note 97 is the ASCII no. for 'a'
        if len(string) > 0:
            bins[ord(string[index])-97].append(string)
    
    for inlst in bins:
        match = find_near_match(inlst)
        if match != "":
            return match
    else:
        return ""

if __name__ == "__main__":
    id_list = open("input.txt").read().split("\n")

    # Run once on first letter, otherwise, will work for second
    run_0 = bin_letters(id_list, 0)
    if len(run_0) == 0:
        print(bin_letters(id_list, 1))
    else:
        print(run_0)
    
