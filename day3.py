def parse(filename):
    with open(filename) as f:
        line = f.read()
        return line


def part1(filename):
    line = parse(filename)
    numbers = "0123456789"
    i = 0
    n = len(line)
    answer = 0
    while i < n:
        if line[i:i+4] == "mul(" and line[i+4] in numbers:
            i += 4
            j = i
            while line[j] in numbers:
                j += 1
            if line[j] == "," and line[j+1] in numbers:
                half = j
                j += 2
                while line[j] in numbers:
                    j += 1
                if line[j] == ")":
                    print(int(line[i:half]), int(line[half + 1:j]))
                    answer += int(line[i:half]) * int(line[half + 1:j])
            i = j
        else:
            i+= 1
    return answer


def part2(filename):
    line = parse(filename)
    numbers = "0123456789"
    i = 0
    n = len(line)
    answer = 0
    able = True
    while i < n:
        if line[i:i+4] == "do()":
            able = True
            i += 4
        elif line[i:i+7] == "don't()":
            able = False
            i += 7
            continue
        elif line[i:i+4] == "mul(" and line[i+4] in numbers and able:
            i += 4
            j = i
            while line[j] in numbers:
                j += 1
            if line[j] == "," and line[j+1] in numbers:
                half = j
                j += 2
                while line[j] in numbers:
                    j += 1
                if line[j] == ")":
                    answer += int(line[i:half]) * int(line[half + 1:j])
            i = j
        else:
            i+= 1
    return answer


