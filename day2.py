def parse(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = tuple([int(lvl) for lvl in line.split(" ")] for line in lines)
        return lines


def part1(filename):
    lines = parse(filename)
    return sum(map(lambda x: 1 if all(0 < x[i] - x[i-1] < 4 for i in range(1, len(x))) or all(0 > x[i] - x[i-1] > -4 for i in range(1, len(x))) else 0, lines))


def part2(filename):
    lines = parse(filename)
    def issafe(x):
        if all(0 < x[i] - x[i-1] < 4 for i in range(1, len(x))) or all(0 > x[i] - x[i-1] > -4 for i in range(1, len(x))):
            return 1
        for i in range(len(x)):
            check = x.copy()
            del check[i]
            if all(0 < check[i] - check[i - 1] < 4 for i in range(1, len(check))) or all(
                    0 > check[i] - check[i - 1] > -4 for i in range(1, len(check))):
                return 1
        return 0
    return sum(map(issafe, lines))

