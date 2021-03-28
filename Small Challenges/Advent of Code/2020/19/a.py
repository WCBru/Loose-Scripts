def parse_rules(lines):
    rules = {}
    toprocess = {}
    
    for line in lines:
        key, val = line.split(": ", 2)
        key = int(key)
        if val[0] == '"':
            rules[key] = set()
            rules[key].add((1,) if val[1] == 'a' else (-1,))
        else:
            toprocess[key] = []
            for part in val.split(" | "):
                toprocess[key].append(tuple(
                    [int(num) for num in part.split()]))

    return (rules, toprocess)

'''def generate_rules(base, tree, target):
    if target in base:
        return base[target]
        
    output = []
    for ruleset in tree[target]:
        if len(ruleset) == 1:
            for rule in generate_rules(base, tree, ruleset[0]):
                output.append(rule) 
        else:
            currentset = generate_rules(base, tree, ruleset[0])
            for rule in ruleset[1:]:
                newset = []
                nextset = generate_rules(base, tree, rule)
                for r1 in currentset:
                    for r2 in nextset:
                        newcode = list(r1)
                        if newcode[-1] * r2[0] > 0:
                            newcode[-1] += r2[0]
                            newcode.extend(list(r2[1:]))
                        else:
                            newcode.extend(list(r2))
                            
                        newset.append(tuple(newcode))
                        
                currentset = newset

            for code in currentset:
                output.append(code)

    print(len(output))
    return output '''
        
def encode_msgs(lines):
    output = []
    for line in lines:
        current = 1 if line[0] == 'a' else -1
        start = 0
        lineout = []
        for char in range(len(line)):
            code = 1 if line[char] == 'a' else -1
            if code != current:
                lineout.append(current * (char - start))
                start = char
                current = code
        lineout.append(current * (len(line) - start))
        output.append(tuple(lineout))

    return output
            

if __name__ == "__main__":
    rules, msgs = open("input.txt").read().split("\n\n", 2)

    rules, tree = parse_rules(rules.split("\n"))
    print(generate_rules(rules, tree, 0))
    
