if __name__ == "__main__":
    num = int(input("Enter Number: ").strip())
    if num < 0:
        ans = num+1
    elif num == 0:
        ans = 0
    else:
        ans = int(num**0.5)
        while ans > 0 and num%ans != 0:
            ans -= 1

        if ans == 0:
            print("Answer not found")
        else:
            print("B, C = " + str(ans) + ", " + str(num//ans))
            print("B + C = " + str(ans + (num//ans)))
