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
    letters = dict()
    original = set()
    for row in range(n):
        for character in range(m):
            match data[row][character]:
                case ".":
                    continue
                case _:
                    if data[row][character] in letters:
                        letters[data[row][character]].append(character + 1j * row)
                        original.add(character + 1j * row)
                    else:
                        letters[data[row][character]] = [character + 1j * row]
                        original.add(character + 1j * row)
    new = set()
    def addpositions(letter):
        for z in range(len(letter)):
            for s in range(z + 1, len(letter)):
                new.add(2 * letter[z] - letter[s])
                new.add(2 * letter[s] - letter[z])
    for i in letters:
        addpositions(letters[i])
    return len(list(i for i in new if -1 < i.imag < n and -1 < i.real < m))


def part2(filename):
    data = parser(filename)
    n = len(data)
    m = len(data[0])
    letters = dict()
    original = set()
    for row in range(n):
        for character in range(m):
            match data[row][character]:
                case ".":
                    continue
                case _:
                    if data[row][character] in letters:
                        letters[data[row][character]].append(character + 1j * row)
                        original.add(character + 1j * row)
                    else:
                        letters[data[row][character]] = [character + 1j * row]
                        original.add(character + 1j * row)
    new = set()
    def addpositions(letter):
        for z in range(len(letter)):
            for s in range(z + 1, len(letter)):
                distance = letter[z] - letter[s]
                new_antenna = letter[s] + distance
                while -1 < new_antenna.imag < n and -1 < new_antenna.real < m:
                    new.add(new_antenna)
                    new_antenna += distance
                distance = -distance
                new_antenna = letter[z] + distance
                while -1 < new_antenna.imag < n and -1 < new_antenna.real < m:
                    new.add(new_antenna)
                    new_antenna += distance
    for i in letters:
        addpositions(letters[i])
    return len(new)
