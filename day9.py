zero = ord("0")

def part1(filename):
    with open(filename) as f:
        data = f.read()
    n = len(data) - 1
    n -= n%2
    i = 0
    answer = 0
    position = 0
    amount = int(data[n])
    while i < n:
        match i%2:
            case 0:
                answer += (i//2)*((position + int(data[i]))*(position + int(data[i]) - 1) - (position*(position-1)))//2
                position += int(data[i])
                i += 1
            case 1:
                a = int(data[i])
                while a > 0:
                    if amount == 0:
                        n -= 2
                        amount = int(data[n])
                    x = min(a, amount)
                    if i < n:
                        answer += (n//2) * ((position + x)*(position + x - 1) - (position*(position-1)))//2
                        amount -= x
                        position += x
                        a -= x
                    else: break
                i+= 1
    if n == i:
        answer += (i//2) * ((position + amount)*(position + amount - 1) - (position*(position-1)))//2
    return answer


def part2(filename):
    with open(filename) as f:
        data = f.read()
    answer = 0
    n = len(data) - 1
    i = n - n % 2
    lis = [[ord(data[i]) - zero, ord(data[i]) - zero] for i in range(n+1)]
    while i >= 0:
        check = False
        for j in range(1, i, 2):
            if lis[i][1] <= lis[j][1]:
                check = True
                position = sum(x for x in (z[0] for z in lis[:j])) + lis[j][0] - lis[j][1]
                answer += (i*((position + lis[i][0])*(position + lis[i][0] -1) - position*(position-1)))//4
                lis[j][1] -= lis[i][1]
                break
        if not check:
            position = sum(x for x in (z[0] for z in lis[:i]))
            answer += (i * ((position + lis[i][0]) * (position + lis[i][0] - 1) - position * (position - 1))) // 4
        i -= 2
    return answer
