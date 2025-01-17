def parser(filename):
    with open(filename) as f:
        pairs = []
        for line in f:
            line = line.strip()
            pairs.append((line[:2], line[3:]))
        return pairs

def part1(filename):
    pairs = parser(filename)
    pcs = {}
    for pair in pairs:
        for i in pair:
            pcs[i] = []
    for pair in pairs:
        for i in pair:
            pcs[i].append(pair[~pair.index(i)])
    count = 0
    for pc in pcs:
        if pc[0] == "t":
            for i in range(len(pcs[pc])):
                for j in range(i+1, len(pcs[pc])):
                    if pcs[pc][i] in pcs[pcs[pc][j]]:
                        count += 1/(2**sum(1 if f[0] =="t" else 0 for f in (pcs[pc][i], pcs[pc][j])))
    return int(count)

def part2(filename):
    pairs = parser(filename)
    pcs = {}
    for pair in pairs:
        for i in pair:
            pcs[i] = set()
    for pair in pairs:
        for i in pair:
            pcs[i].add(pair[~pair.index(i)])
    groups = []
    for pair in pairs:
        for i in pair:
            for group in groups:
                if all(i in pcs[j] for j in group):
                    group.append(i)
        groups.append([pair[0]])
        groups.append([pair[1]])
    m = 0
    ma = []
    for group in groups:
        if len(group) > m:
            m = len(group)
            ma = group
    ma.sort()
    answer = ""
    for i in ma:
        answer += i
        answer += ","
    if not answer:
        return answer
    return answer[:-1]

