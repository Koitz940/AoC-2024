def parser(filename):
    with open(filename) as f:
        lines = f.readlines()
        for line in range(len(lines)):
            lines[line] = lines[line].strip()
        return lines


def part1(filename):
    data = parser(filename)
    done = set()
    n = len(data)
    m = len(data[0])
    directions = (1,-1,1j,-1j)
    def findprice(position, character):
        area = set()
        def findperimetre(spot):
            if spot in done:
                return 0
            area.add(spot)
            done.add(spot)
            nexts = (spot + i for i in directions if -1 < (spot + i).imag < n and -1 < (spot + i).real < m)
            followings = tuple(i for i in nexts if data[round(i.imag)][round(i.real)] == character)
            return 4 - len(followings) + sum(map(findperimetre, followings))
        return findperimetre(position) * len(area)
    answer = 0
    for y in range(n):
        for x in range(m):
            answer +=  findprice(x + y*1j, data[round((x + y*1j).imag)][round((x + y*1j).real)])
    return answer


def part2(filename):
    data = parser(filename)
    done = set()
    n = len(data)
    m = len(data[0])
    directions = (1,-1,1j,-1j)
    def findprice(position, character):
        if position in done:
            return 0
        area = set()
        def findarea(spot):
            if spot in done:
                return
            area.add(spot)
            done.add(spot)
            nexts = (spot + i for i in directions if -1 < (spot + i).imag < n and -1 < (spot + i).real < m)
            for z in (i for i in nexts if data[round(i.imag)][round(i.real)] == character):
                findarea(z)
        findarea(position)
        ox = tuple(i.real for i in area)
        oy = tuple(i.imag for i in area)
        maxx = 2 + max(ox)
        minx = min(ox)
        maxy = 2 + max(oy)
        miny = min(oy)
        sides = 0
        previous = []
        for x in range(round(minx), round(maxx)):
            current = []
            check = True
            for y in range(round(miny), round(maxy)):
                if ((x + 1j*y) in area) == check:
                    check = not check
                    current.append(tuple((y, check)))
                    if tuple((y, check)) not in previous:
                        sides += 1
            previous = current.copy()
        previous = []
        for y in range(round(miny), round(maxy)):
            current = []
            check = True
            for x in range(round(minx), round(maxx)):
                if ((x + 1j * y) in area) == check:
                    check = not check
                    current.append(tuple((x, check)))
                    if tuple((x, check)) not in previous:
                        sides += 1
            previous = current.copy()
        return sides * len(area)
    answer = 0
    for Y in range(n):
        for X in range(m):
            answer += findprice(X + Y * 1j, data[round((X + Y * 1j).imag)][round((X + Y * 1j).real)])
    return answer