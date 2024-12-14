def parse(file):
    with open(file) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split()
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
    return lines


def part1(stuff):
    data = parse(stuff)
    left =  sorted(i[0] for i in data)
    right = sorted(i[1] for i in data)
    return sum((abs(pair[0] - pair[1]) for pair in zip(right, left)))


def part2(stuff):
    data = parse(stuff)
    counting = dict()
    for j in (i[0] for i in data):
        counting[j] = 0
    for j in (i[1] for i in data):
        counting[j] = 0
    for j in (i[1] for i in data):
        counting[j] += 1
    return sum((i * counting[i] for i in (j[0] for j in data)))
