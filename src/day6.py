
def part1():
    counters = [0] * 9
    with open("input/day6/input") as f:
        for n in next(f).split(','):
            counters[int(n)] += 1
    
    for _ in range(80):
        amt_new = counters[0]
        for i in range(1, 9):
            counters[i - 1] = counters[i]
        counters[6] += amt_new
        counters[8] = amt_new

    return sum(counters)


def part2():
    counters = [0] * 9
    with open("input/day6/input") as f:
        for n in next(f).split(','):
            counters[int(n)] += 1
    
    for _ in range(256):
        amt_new = counters[0]
        for i in range(1, 9):
            counters[i - 1] = counters[i]
        counters[6] += amt_new
        counters[8] = amt_new

    return sum(counters)


if __name__ == "__main__":
    print(part1())
    print(part2())
