from time import time
#this works by putting start = time() at some moment and then doing print(time() - start) after part you wanted to measure has happened
#one to calculate whole code is written

def parser(filename):
    with open(filename) as f:
        lines = f.read()
    lines = lines.split(sep="\n\n")
    given = {}
    for i in lines[0].split(sep="\n"):
        k = i.split()
        given[k[0][:-1]] = int(k[1])
    to_guess = []
    solutions = set()
    for i in lines[1].split(sep="\n"):
        k = i.split()
        to_guess.append([k[0], k[2], k[1], k[4]])
        for j in (0,2,4):
            if k[j][0] == "z":
                solutions.add(k[j])
    return given, to_guess, len(solutions)


def o(c, b):
    return c | b
def a(c, b):
    return c & b
def x(c, b):
    return c ^ b

zero = ord("0")
operations = {
    "AND": a,
    "OR":  o,
    "XOR": x}

def solve(n, known, to_know):
    r = time()
    m = len(to_know)
    solutions = {}
    i = 0
    while True:
        if i >= m:
            i = 0
        if len(solutions) == n:
            break
        if to_know[i][0] in known:
            if to_know[i][1] in known:
                known[to_know[i][3]] = operations[to_know[i][2]](known[to_know[i][0]], known[to_know[i][1]])
                if to_know[i][3][0] == "z":
                    solutions[to_know[i][3]] = operations[to_know[i][2]](known[to_know[i][0]], known[to_know[i][1]])
                to_know.pop(i)
                m -= 1
                continue
            elif known[to_know[i][0]] == 1 and to_know[i][2] == "OR":
                known[to_know[i][3]] = 1
                if to_know[i][3][0] == "z":
                    solutions[to_know[i][3]] = 1
                to_know.pop(i)
                m -= 1
                continue
        elif to_know[i][1] in known:
            if known[to_know[i][1]] == 1 and to_know[i][2] == "OR":
                known[to_know[i][3]] = 1
                if to_know[i][3][0] == "z":
                    solutions[to_know[i][3]] = 1
                to_know.pop(i)
                m -= 1
                continue
        i += 1
    answer = 0
    for i in range(n):
        if i < 10:
            j = "0" + chr(zero + i)
        else:
            j = str(i)
        answer += solutions["z" + j] * 2 ** i
    return answer

def part1(filename):
    known, to_know, n = parser(filename)
    return solve(n, known, to_know)

start = time()
print(part1("files/day24_file"))
print(time() - start)