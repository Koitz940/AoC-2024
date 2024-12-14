def parse(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines


def part1(filename):
    data = parse(filename)
    y = len(data)
    x = len(data[0]) - 1
    directions = (1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 -1j)
    answer = 0
    def findM(position):
        nexts = (position + z for z in directions if -1 < (position + z).real < x and -1 < (position + z).imag < y)
        return sum(findnext(z, z-position) for z in nexts if data[int(z.imag)][int(z.real)] == "M")
    def findnext(position, direction):
        match data[int(position.imag)][int(position.real)]:
            case "M":
                if not -1 < position.imag + direction.imag < y or not -1 < position.real + direction.real < x:
                    return 0
                if not data[int(position.imag + direction.imag)][int(position.real + direction.real)] == "A":
                    return 0
                return findnext(position + direction, direction)
            case "A":
                if not -1 < position.imag + direction.imag < y or not -1 < position.real + direction.real < x:
                    return 0
                if not data[int(position.imag + direction.imag)][int(position.real + direction.real)] == "S":
                    return 0
                return 1

    for i in range(x):
        for j in range(y):
            if data[j][i] == "X":
                answer += findM(i + j * 1j)
    return answer

def part2(filename):
    data = parse(filename)
    directions = (1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j)
    answer = 0
    def findcross(position):
        nexts = []
        for x in directions:
            nexts.append(data[int((x+position).imag)][int((x+position).real)])
        if ((nexts[1] == "S" and nexts[2] == "M") or (nexts[2] == "S" and nexts[1] == "M")) and ((nexts[0] == "M" and nexts[3] == "S") or (nexts[0] == "S" and nexts[3] == "M")):
            return 1
        return 0

    for i in range(1, len(data[0])-2):
        for j in range(1, len(data)-1):
            if data[j][i] == "A":
                answer += findcross(i + j * 1j)
    return answer

