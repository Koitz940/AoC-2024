def parser1(filename):
    with open(filename) as f:
        data = f.read()
        data = data.split("\n\n")
        warehouse = data[0].split()
        instructions = data[1]
        instructions = instructions.replace("\n", "")
    new_warehouse = []
    for i in warehouse:
        i = i.strip()
        line = []
        for j in i:
            match j:
                case ".":
                    line.append(0)
                case "#":
                    line.append(-1)
                case "O":
                    line.append(1)
                case "@":
                    line.append(2)
        new_warehouse.append(line.copy())
    return new_warehouse, instructions


def parser2(filename):
    with open(filename) as f:
        data = f.read()
        data = data.split("\n\n")
        warehouse = data[0].split()
        instructions = data[1]
        instructions = instructions.replace("\n", "")
    new_warehouse = []
    for i in warehouse:
        i = i.strip()
        line = []
        for j in i:
            line.append(j)
            line.append(".")
        new_warehouse.append(line.copy())
    return new_warehouse, instructions


def part1(filename):
    warehouse, instructions = parser1(filename)
    n = len(warehouse)
    m = len(warehouse[0])
    for i in range(n):
        for j in range(m):
            if warehouse[i][j] == 2:
                position = [i, j]
    def execute(instruction, pos):
        match instruction:
            case "<":
                direction = (0, -1)
            case ">":
                direction = (0, 1)
            case "^":
                direction = (-1, 0)
            case "v":
                direction = (1, 0)
            case _:
                print("not a correct direction")
                exit(1)
        holder = pos.copy()
        holder[0] += direction[0]
        holder[1] += direction[1]
        while warehouse[holder[0]][holder[1]] == 1:
            holder[0] += direction[0]
            holder[1] += direction[1]
        if warehouse[holder[0]][holder[1]] == -1:
            return pos
        warehouse[holder[0]][holder[1]], warehouse[direction[0] + pos[0]][direction[1] + pos[1]] = warehouse[direction[0] + pos[0]][direction[1] + pos[1]], warehouse[holder[0]][holder[1]]
        warehouse[pos[0]][pos[1]], warehouse[direction[0] + pos[0]][direction[1] + pos[1]] = warehouse[direction[0] + pos[0]][direction[1] + pos[1]], warehouse[pos[0]][pos[1]]
        return [pos[0] + direction[0], pos[1] + direction[1]]
    for inst in instructions:
        position = execute(inst, position)
    answer = 0
    for i in range(n):
        for j in range(m):
            if warehouse[i][j] == 1:
                answer += 100 * i + j
    return answer


def part2(filename):
    warehouse, instructions = parser2(filename)
    n = len(warehouse)
    m = len(warehouse[0])
    for i in range(n):
        for j in range(m):
            if warehouse[i][j] == "@":
                position = [i, j]
    def execute(instruction, pos):
        match instruction:
            case "<":
                direction = (0, -1)
            case ">":
                direction = (0, 1)
            case "^":
                direction = (-1, 0)
            case "v":
                direction = (1, 0)
            case _:
                print("not a correct direction")
                exit(1)
        if instruction == (0, -1) or instruction == (0, 1):
            holder = pos.copy()
            holder[1] += direction[1]
            while warehouse[holder[0]][holder[1]] in "[]":
                holder[1] += direction[1]
            if warehouse[holder[0]][holder[1]] == "#":
                return pos
            for x in range(holder[1] - direction[1], pos[1], -direction[1]):
                warehouse[holder[0]][x], warehouse[holder[0]][x - direction[1]] = warehouse[holder[0]][x - direction[1]], warehouse[holder[0]][x]


print(part1("files/day15_file"))
