def execute(filename, iterations):
    with open(filename) as f:
        numbs = f.read()
        numbs = (int(i) for i in numbs.split())
    count = {}
    for i in numbs:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    for _ in range(iterations):
        new_count = {}
        for i in count:
            m = len(str(i))
            if i == 0:
                if 1 not in new_count:
                    new_count[1] = count[i]
                else:
                    new_count[1] += count[i]
            elif m % 2 == 0:
                x = i % (10 ** (m//2))
                y = (i - x) // (10 ** (m//2))
                if x not in new_count:
                    new_count[x] = count[i]
                else:
                    new_count[x] += count[i]
                if y not in new_count:
                    new_count[y] = count[i]
                else:
                    new_count[y] += count[i]
            else:
                x = i * 2024
                if x not in new_count:
                    new_count[x] = count[i]
                else:
                    new_count[x] += count[i]
        count = new_count
    return sum(count[i] for i in count)

def part1(filename):
    return execute(filename, 25)

def part2(filename):
    return execute(filename, 75)
