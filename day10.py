def parser(filename):
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    zero = ord("0")
    return [tuple(ord(i) - zero for i in j) for j in lines]


def part1(filename):
    directions = (1,-1,1j,-1j)
    data = parser(filename)
    n = len(data)
    m = len(data[0])
    def find9s(position):
        answer = set()
        def nextstep(current, pos):
            for nexts in (pos+z for z in directions if -1 < (pos+z).real < m and -1 < (pos+z).imag < n):
                match current:
                    case 8:
                        if data[int(nexts.imag)][int(nexts.real)] == 9:
                            answer.add(nexts)
                    case _:
                        if data[int(nexts.imag)][int(nexts.real)] == current + 1:
                            nextstep(current+1,nexts)
        nextstep(0, position)
        return len(answer)

    count = 0
    for row in range(n):
        for col in range(m):
            if data[row][col] == 0:
                count += find9s(col + 1j*row)
    return count

def part2(filename):
    directions = (1,-1,1j,-1j)
    data = parser(filename)
    n = len(data)
    m = len(data[0])
    def find9s(current, position):
        paths = 0
        for nexts in (position+z for z in directions if -1 < (position+z).real < m and -1 < (position+z).imag < n):
            match current:
                case 8:
                    if data[int(nexts.imag)][int(nexts.real)] == 9:
                        paths += 1
                case _:
                    if data[int(nexts.imag)][int(nexts.real)] == current + 1:
                        paths += find9s(current+1,nexts)
        return paths

    count = 0
    for row in range(n):
        for col in range(m):
            if data[row][col] == 0:
                count += find9s(0, col + 1j*row)
    return count
