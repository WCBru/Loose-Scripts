LAZYLIST = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

if __name__ == "__main__":
    inStr = input().strip()
    if not inStr.isdigit():
        print("Please enter a number")
    else:
        outStr = ""
        divisor = 62
        inNum = int(inStr)
        while inNum != 0:
            outStr = LAZYLIST[inNum%62] + outStr
            inNum //= divisor

        print("Note: This output will differ from the challenge" +
              "and will place the largest digits first")
        print(outStr)
            
