
def part1():
    with open("input/day3/input") as f:
        amt_lines = 0
        first = True
        for line in f:
            amt_lines += 1
            if first:
                collector = [0 for _ in line.strip()]
                first = False
            for i, c in enumerate(line.strip()):
                if c == '1':
                    collector[i] += 1
    n = 0
    for d in collector:
        n = 2 * n + (1 if 2 * d > amt_lines else 0)
    mask = 0xffffffff >> (32 - len(collector))
    print(n * (~n & mask))


part1()
