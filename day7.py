def parser(filename):
    with open(filename) as f:
        lines = f.readlines()
    for line in range(len(lines)):
        lines[line] = lines[line].strip()
        lines[line] = lines[line].split(sep = ":")
        lines[line][0] = int(lines[line][0])
        lines[line][1] = lines[line][1][1:].split()
        lines[line][1] = [int(i) for i in lines[line][1]]
    return lines


def part1(filename):
    def combinations(n):
        if n == 1:
            return [[0], [1]]
        following = combinations(n-1)
        answer = [[0] + i for i in following]
        for j in [[1] + i for i in following]:
            answer.append(j)
        return answer


    def operate(x, y, op):
        return x+y if not op else x*y

    data = parser(filename)
    combs = dict()
    for x in range(1, max(len(line[1]) for line in data)):
        combs[x] = combinations(x)

    def isvalid(line):
        operators = combs[len(line[1]) - 1]
        for i in operators:
            answer = operate(line[1][0], line[1][1], i[0])
            for j in range(2, len(line[1])):
                answer = operate(answer, line[1][j], i[j-1])
            if answer == line[0]:
                return line[0]
        return 0
    return sum(map(isvalid, data))


def part2(filename):
    def combinations(n):
        if n == 1:
            return [[0], [1], [2]]
        following = combinations(n - 1)
        answer = [[0] + i for i in following]
        for j in [[1] + i for i in following]:
            answer.append(j)
        for j in [[2] + i for i in following]:
            answer.append(j)
        return answer

    def operate(x, y, op):
        match op:
            case 0:
                return x + y
            case 1:
                return x * y
            case 2:
                return (10**(len(str(y))))*x + y

    data = parser(filename)
    combs = dict()
    for l in range(1, max(len(line[1]) for line in data)):
        combs[l] = combinations(l)

    def isvalid(line):
        operators = combs[len(line[1]) - 1]
        for i in operators:
            answer = operate(line[1][0], line[1][1], i[0])
            for j in range(2, len(line[1])):
                answer = operate(answer, line[1][j], i[j - 1])
            if answer == line[0]:
                return line[0]
        return 0

    return sum(map(isvalid, data))

