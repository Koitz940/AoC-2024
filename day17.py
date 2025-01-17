zero = ord("0")

def parser1(filename):
    with open(filename) as f:
        registers = []
        for _ in range(3):
            line = f.readline()
            registers.append(int(line[12: -1]))
        f.readline()
        line = f.readline()
        line = line.split()
        line = line[1].split(sep=",")
        line = [ord(i) - zero for i in line]
        return registers, line

def parser2(filename):
    with open(filename) as f:
        for _ in range(4):
            f.readline()
        line = f.readline()
        line = line.split()
        line = line[1].split(sep=",")
        line = [ord(i) - zero for i in line]
        return line

def part1(filename):
    registers, program = parser1(filename)
    registers.append(0)
    registers.append("")
    m = len(program)
    def combo(n):
        if n < 4:
            return n
        if n == 7:
            exit(0)
        return registers[n-4]
    def adv(a):
        registers[0] = registers[0] >> combo(a)
        registers[3] += 2
    def bxl(a):
        registers[1] = registers[1] ^ a
        registers[3] += 2
    def jnz(a):
        if registers[0] == 0:
            registers[3] += 2
            return
        registers[3] = a
    def bst(a):
        registers[1] = combo(a) % 8
        registers[3] += 2
    def out(a):
        registers[4] += f"{combo(a) % 8},"
        registers[3] += 2
    def bxc(a):
        registers[1] = registers[1] ^ registers[2]
        registers[3] += 2
    def bdv(a):
        registers[1] = registers[0] >> combo(a)
        registers[3] += 2
    def cdv(a):
        registers[2] = registers[0] >> combo(a)
        registers[3] += 2
    funcs = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    while registers[3] < m:
        funcs[program[registers[3]]](program[registers[3] + 1])
    if not registers[4]:
        return registers[4]
    return registers[4][:-1]

def part2(filename):
    return "boring exercise I hated it it's so ruined because of the need of metadata analysis"
