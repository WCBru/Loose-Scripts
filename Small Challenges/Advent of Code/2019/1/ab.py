def recursive_fuel(mass):
    fuel = mass // 3 - 2
    return 0 if fuel <= 0 else fuel + recursive_fuel(fuel) 
    

if __name__ == "__main__":
    print(sum([int(val) // 3 - 2 for val in open("input.txt").read().split('\n')]))
    print(sum([recursive_fuel(int(val)) for val in open("input.txt").read().split('\n')]))
