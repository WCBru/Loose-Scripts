# See the wikipedia page
def knuth(a,n,b):
    if n == 1:
        return a**b
    elif b == 0:
        return 1
    else:
        return knuth(a,n-1,knuth(a,n,b-1))

if __name__ == "__main__":
    print(knuth(int(input("a: ")),
                int(input("n: ")),
                int(input("b: "))))
