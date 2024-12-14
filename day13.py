def parse1(filename):
    with open(filename) as f:
        data = f.read()
        data = data.split(sep = "\n\n")
    lines = []
    for line in data:
        line = line.split(sep = "\n")
        info = []
        for i in line:
            info.append([int(i[i.find("X") + 2: i.find(",")]), int(i[i.find("Y") + 2:])])
        lines.append(info.copy())
    return lines

def parse2(filename):
    with open(filename) as f:
        data = f.read()
        data = data.split(sep = "\n\n")
    lines = []
    for line in data:
        line = line.split(sep = "\n")
        info = []
        for i in line:
            info.append([int(i[i.find("X") + 2: i.find(",")]), int(i[i.find("Y") + 2:])])
        info[2][0] += 10000000000000
        info[2][1] += 10000000000000
        lines.append(info.copy())
    return lines


def part1(filename):
    data = parse1(filename)
    def execute(coefs):
        det = coefs[0][0] * coefs[1][1] - coefs[0][1] * coefs[1][0]
        if det == 0:
            return 0
        a = (coefs[1][1] * coefs[2][0] - coefs[1][0] * coefs[2][1])/det
        b = (coefs[0][0] * coefs[2][1] - coefs[0][1] * coefs[2][0])/det
        if a == round(a) and b == round(b) and -1 < a < 101 and -1 < b < 101:
            return 3 * a + b
        return 0
    return round(sum(map(execute, data)))


def part2(filename):
    data = parse2(filename)
    def execute(coefs):
        det = coefs[0][0] * coefs[1][1] - coefs[0][1] * coefs[1][0]
        if det == 0:
            return 0
        a = (coefs[1][1] * coefs[2][0] - coefs[1][0] * coefs[2][1])/det
        b = (coefs[0][0] * coefs[2][1] - coefs[0][1] * coefs[2][0])/det
        if a == round(a) and b == round(b):
            return 3 * a + b
        return 0
    return round(sum(map(execute, data)))
