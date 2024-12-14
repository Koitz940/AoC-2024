def parser(filename):
    with open(filename) as f:
        lines = f.readlines()
        comparisons = lines[: lines.index("\n")]
        for line in range(len(comparisons)):
            comparisons[line] = comparisons[line].strip()
            comparisons[line] = comparisons[line].split(sep = "|")
            comparisons[line] = [int(i) for i in comparisons[line]]
        data = lines[lines.index("\n")+1:]
        for line in range(len(data)):
            data[line] = data[line].strip()
            data[line] = data[line].split(sep=",")
            data[line] = [int(i) for i in data[line]]
        return comparisons, data

def part1(filename):
    data = parser(filename)
    comparisons = data[0]
    stuff = data[1]
    better = {}
    for i in comparisons:
        better[i[0]] = set()
    for i in comparisons:
        better[i[0]].add(i[1])
    def isgood(line):
        for x in range(len(line[:-1])):
            if line[x] not in better:
                continue
            for j in range(len(line[x+1:])):
                if line[x+1+j] in better[line[x]]:
                    continue
                elif line[x+1+j] not in better:
                    continue
                elif line[x] in better[line[x+1+j]]:
                    return 0
            if line[-1] not in better:
                continue
            for j in line[:-1]:
                if j in better[line[-1]]:
                    return 0
        return line[len(line)//2]
    return sum(map(isgood, stuff))


def part2(filename):
    data = parser(filename)
    comparisons = data[0]
    stuff = data[1]
    better = {}
    for i in comparisons:
        better[i[0]] = set()
    for i in comparisons:
        better[i[0]].add(i[1])


    def isbad(line):
        for x in range(len(line[:-1])):
            if line[x] not in better:
                continue
            for j in range(len(line[x + 1:])):
                if line[x + 1 + j] in better[line[x]]:
                    continue
                elif line[x + 1 + j] not in better:
                    continue
                elif line[x] in better[line[x + 1 + j]]:
                    return True
            if line[-1] not in better:
                continue
            for j in line[:-1]:
                if j in better[line[-1]]:
                    return True
        return False


    answer = 0


    def sorting(thing):
        for j in range(len(thing)-1):
            for x in range(len(thing)-j-1):
                if line[x+1] not in better:
                    continue
                if line[x] in better[line[x+1]]:
                    line[x], line[x+1] = line[x+1], line[x]

    for line in stuff:
        if isbad(line):
            sorting(line)
            answer += line[len(line)//2]
    return answer

