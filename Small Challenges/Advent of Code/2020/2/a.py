def parse_line(line):
    parts = line.split()
    return (tuple(parts[0].split('-')), parts[1][0], parts[2])

def is_line_valid(line):
    params = parse_line(line)
    letterCount = sum([params[1] == c for c in params[2]])
    return letterCount >= int(params[0][0]) and letterCount <= int(params[0][1])

if __name__ == "__main__":
    print(sum([is_line_valid(line) for line in
               open("input.txt").read().strip().split('\n')]))
