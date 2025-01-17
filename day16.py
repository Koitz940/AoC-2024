def parser(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in range(len(lines)):
            lines[line] = lines[line].strip()
        return lines

def part1(filename):
    data = parser(filename)
    n = len(data)
    m = len(data[0])
    start = 1 + 1j*(n-2)
    end = m-2 + 1j
    movement = (1, -1, 1j, -1j)
    intersections = set()
    crosses = set()
    crosses.add(end)
    seen = set()
    def setadding(element):
        check = tuple(i for i in intersections if i[0] in element and i[1] in element)
        if len(check) == 1:
            if element[2] < check[0][2]:
                intersections.remove(check[0])
                intersections.add(element)
        else:
            intersections.add(element)

    def findinters(begin, current, direction, score):
        seen.add(current)
        if current == start:
            maybe = (current + i for i in movement if 0 < (current + i).imag < n and 0 < (current + i).real < m)
            true = tuple(i for i in maybe if data[int(i.imag)][int(i.real)] != "#")
            for i in true:
                findinters(begin, i, i-start, 1)
        while True:
            seen.add(current)
            maybe = (current + i for i in movement if 0 < (current + i).imag < n and 0 < (current + i).real < m)
            for i in maybe:
                if i in crosses:
                    if i - current == direction:
                        setadding((begin, i, score + 1))
                    else:
                        setadding((begin, i, score + 1001))
            maybe = (i for i in maybe if i - direction != current and i not in seen)
            true = tuple(i for i in maybe if data[int(i.imag)][int(i.real)] != "#")
            match len(true):
                case 0:
                    return
                case 1:
                    if true[0] - direction != current:
                        score += 1000
                        direction = true[0] - direction
                    score += 1
                    current = true[0]
                case _:
                    crosses.add(current)
                    setadding((begin, current, score))
                    for j in true:
                        if j-current != direction:
                            findinters(current, j, j-current, 1001)
                        else:
                            findinters(current, j, direction, 1)
    findinters(start, start, 9, 0)
    print(crosses)
    print(intersections)


print(part1("files/day16_file"))