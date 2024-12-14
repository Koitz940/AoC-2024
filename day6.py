def parse(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in range(len(lines)):
            lines[line] = lines[line].strip()
        new_lines = []
        for line in lines:
            new_line = []
            for i in line:
                match i:
                    case ".":
                        new_line.append(0)
                    case "#":
                        new_line.append(1)
                    case _:
                        new_line.append(i)
            new_lines.append(new_line)
    return new_lines


def part1(filename):
    lines = parse(filename)
    def findstart():
        for line in range(len(lines)):
            for symbol in range(len(lines[line])):
                if lines[line][symbol] == "^":
                    return symbol + 1j * line, complex(0, -1)
    begin = findstart()
    way = begin[1]
    pos = begin[0]
    passed = set()
    passed.add(pos)
    n = len(lines)
    m = len(lines[0])
    while -1 < pos.imag + way.imag < n and -1 < pos.real + way.real < m:
        if lines[int(pos.imag + way.imag)][int(pos.real + way.real)] == 1:
            way *= 1j
        else:
            pos += way
            passed.add(pos)
    return len(passed)


def part2(filename):
    lines = parse(filename)
    n = len(lines)
    m = len(lines[0])
    def findstart():
        for line in range(len(lines)):
            for symbol in range(len(lines[line])):
                if lines[line][symbol] == "^":
                    return symbol + 1j * line, complex(0, -1)

    begin = findstart()
    way = begin[1]
    pos = begin[0]
    path = set()
    while -1 < pos.imag + way.imag < n and -1 < pos.real + way.real < m:
        if lines[int(pos.imag + way.imag)][int(pos.real + way.real)] == 1:
            way *= 1j
        else:
            pos += way
            path.add(pos)

    def iscycle(data, start, direction):
        passed = set()
        while -1 < start.imag + direction.imag < n and -1 < start.real + direction.real < m:
            if data[int(start.imag + direction.imag)][int(start.real + direction.real)] == 1:
                if (start, direction) in passed:
                    return 1
                passed.add((start, direction))
                direction *= 1j
            else:
                start += direction
        return 0

    answer = 0
    for position in path:
        mapa = [i.copy() for i in lines]
        if position == begin[0]:
            continue
        mapa[int(position.imag)][int(position.real)] = 1
        if iscycle(mapa, begin[0], begin[1]):
            answer += 1
    return answer
