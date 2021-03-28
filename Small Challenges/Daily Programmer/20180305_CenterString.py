if __name__ == "__main__":
    inStr = """11
ACAAAATCCTATCAAAAACTACCATACCAAT
ACTATACTTCTAATATCATTCATTACACTTT
TTAACTCCCATTATATATTATTAATTTACCC
CCAACATACTAAACTTATTTTTTAACTACCA
TTCTAAACATTACTCCTACACCTACATACCT
ATCATCAATTACCTAATAATTCCCAATTTAT
TCCCTAATCATACCATTTTACACTCAAAAAC
AATTCAAACTTTACACACCCCTCTCATCATC
CTCCATCTTATCATATAATAAACCAAATTTA
AAAAATCCATCATTTTTTAATTCCATTCCTT
CCACTCCAAACACAAAATTATTACAATAACA
ATATTTACTCACACAAACAATTACCATCACA
TTCAAATACAAATCTCAAAATCACCTTATTT
TCCTTTAACAACTTCCCTTATCTATCTATTC
CATCCATCCCAAAACTCTCACACATAACAAC
ATTACTTATACAAAATAACTACTCCCCAATA
TATATTTTAACCACTTACCAAAATCTCTACT
TCTTTTATATCCATAAATCCAACAACTCCTA
CTCTCAAACATATATTTCTATAACTCTTATC
ACAAATAATAAAACATCCATTTCATTCATAA
CACCACCAAACCTTATAATCCCCAACCACAC"""

    #lines = int(input().strip())
    #strings = []
    #for x in range(lines):
    #    strings.append(input().strip())
    strings = inStr.split("\n")[1:]
    
    scores = {}
    minDiff = len(strings)*len(strings[0])  
    for string in strings:
        currDiff = 0
        for string2 in strings:
            for char in range(min(len(string), len(string2))):
                currDiff += 1 if string[char] != string2[char] else 0

        scores[string] = currDiff
        if currDiff < minDiff:
            minDiff = currDiff

    for string in scores:
        if scores[string] == minDiff:
            print(string)
            break
