ENCRYPT = 1
DECRYPT = -1

def vig(mode):
    msg = input("Enter keyword and message: ").strip().split()
    if len(msg) < 2: # If only 1 word found, no message entered
        print("No message entered")
    else:
        msg = [msg[0]] + [' '.join(msg[1:])] # Concat message words
        msg = [word.lower() for word in msg] # convert to all lower case
        if not all([ord(letter) < 123 and ord(letter) > 96 for letter in msg[0]]):
            print("Keyword not all letters")
        else: # Valid keyword and message
            keyIndex = 0 # Cycle through letters in keyword
            outStr = "" # output
            for letter in msg[1]: # For all chars in message
                if ord(letter) > 96 and ord(letter) < 123:# If a letter
                    # Add ASCII values for encrypt, subtract for decrypt
                    # Letters occur at 19mod26. Add/subtract offset as needed
                    # Add final 97 to reach range of letters in ASCII
                    outStr += chr((ord(letter)+mode*ord(msg[0][keyIndex])
                                   -(19 + mode*19))%26 + 97)
                else: # If not a letter, just append it on
                    outStr += letter
                keyIndex = (keyIndex + 1)%len(msg[0]) # Move to next letter
            print(outStr) # Print output

if __name__ == "__main__":
    vig(ENCRYPT)
