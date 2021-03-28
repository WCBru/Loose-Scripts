def traverse(graph, code, seen):
    if code not in graph:
        return
    
    for node in graph[code]:
        if node not in seen:
            seen.add(node)
            traverse(graph, node, seen)

if __name__ == "__main__":
    dCount = 0
    cCount = 0

    desc = {}
    col = {}
    in_out_map = {}
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

        if len(inner.split()) < 4:
            continue
        else:
            contents = inner.split(", ")
            for cont in contents:
                words = cont.split()
                dc = words[1]
                cc = words[2]
                if dc not in desc:
                    desc[dc] = dCount
                    dCount += 1
                if cc not in col:
                    col[cc] = cCount
                    cCount += 1
                code = (desc[dc], col[cc])
                    
                if code not in in_out_map:
                    in_out_map[code] = set()

                in_out_map[code].add((desc[do], col[co]))

    seen = set()
    traverse(in_out_map, (desc["shiny"], col["gold"]), seen)
    print(len(seen))
