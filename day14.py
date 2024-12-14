def parser(filename):
    with open(filename) as f:
        data = f.readlines()
    lines = []
    count = 0
    for i in data:
        i = i.split()
        count += 1
        lines.append([int(i[0][2:i[0].find(",")]) + 1j*int(i[0][i[0].find(",")+1:]), int(i[1][2:i[1].find(",")]) + 1j*int(i[1][i[1].find(",")+1:])])
    return lines

def part1(filename, width = 101, height = 103, time = 100):
    data = parser(filename)
    first = 0
    second = 0
    third = 0
    fourth = 0
    for robot in data:
        position = robot[0] + robot[1]*time
        x = position.real % width
        y = position.imag % height
        width_middle = width//2
        height_middle = height//2
        if x < width_middle and y < height_middle:
            first += 1
        if x > width_middle and y < height_middle:
            second += 1
        if x < width_middle and y > height_middle:
            third += 1
        if x > width_middle and y > height_middle:
            fourth += 1
    return first * second * fourth * third


def part2(filename):
    data = parser(filename)
    i = 1
    while i <= 101*103 + 1:
        positions = set()
        for robot in data:
            robot[0] = (robot[0].real + robot[1].real) % 101 + 1j * ((robot[0].imag + robot[1].imag) % 103)
            positions.add(robot[0])
        grid = ""
        for y in range(103):
            for x in range(101):
                grid += "# " if x + 1j*y in positions else "  "
            grid += "\n"
        if all(j * "# " in grid for j in range(13)):
            print(grid)
            return i
        i += 1
    return "No Tree :("


print(part2("day14_file"))