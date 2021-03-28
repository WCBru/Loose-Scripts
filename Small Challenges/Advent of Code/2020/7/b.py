def traverse(graph, code):
    total = 1
    for node in graph[code]:
        total += node[2] * traverse(graph, node[0:2])

    return total

if __name__ == "__main__":
    dCount = 0
    cCount = 0

    desc = {}
    col = {}
    bagmap = {}
    lines = open("input.txt").read().strip().split("\n")
    
    for line in lines:
        outer, inner = line.split(" bags contain ", 2)

        do, co = outer.split()
        if do not in desc:
            desc[do] = dCount
            dCount += 1
        if co not in col:
            col[co] = cCount
            cCount += 1

        bagmap[(desc[do], col[co])] = set()

        if len(inner.split()) < 4:
            continue
        else:
            contents = inner.split(", ")
            for cont in contents:
                words = cont.split()
                quant = words[0]
                dc = words[1]
                cc = words[2]
                
                if dc not in desc:
                    desc[dc] = dCount
                    dCount += 1
                if cc not in col:
                    col[cc] = cCount
                    cCount += 1

                code = (desc[dc], col[cc], int(quant))
                    
                if code[0:2] not in bagmap:
                    bagmap[code[0:2]] = set()

                bagmap[(desc[do], col[co])].add(code)

    start = (desc["shiny"], col["gold"])
    print(traverse(bagmap, start) - 1)
