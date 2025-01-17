def parser(filename):
    with open(filename) as f:
        numbers = []
        for line in f:
            numbers.append(int(line))
    return numbers

mod = 1<<24
def op1(n):
    return (n ^ (n << 6)) % mod
def op2(n):
    return (n ^ (n >> 5)) % mod
def op3(n):
    return (n ^ (n << 11)) % mod


def part1(filename):
    numbers = parser(filename)
    def do(n):
        for _ in range(2000):
            n = op3(op2(op1(n)))
        return n
    return sum(map(do, numbers))


def part2(filename):
    numbers = parser(filename)
    counter = [0 for _ in range(19**4)]
    for n in numbers:
        previous = 0
        dt = []
        seen = set()
        for _ in range(3):
            n = op3(op2(op1(n)))
            current = n % 10
            dt.append(current - previous)
            previous = current
        for _ in range(1998):
            n = op3(op2(op1(n)))
            current = n % 10
            dt.append(current - previous)
            previous = current
            if tuple(dt) not in seen:
                counter[sum((dt[m] + 9) * (19**m) for m in range(4))] += current
                seen.add(tuple(dt))
            dt.pop(0)
    return max(counter)