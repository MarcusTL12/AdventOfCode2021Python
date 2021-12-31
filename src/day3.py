import numpy as np


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


def single_out(m, inv):
    bits = np.shape(m)[0]
    filtered = np.ones(np.shape(m)[1], dtype=bool)

    for bit in range(bits):
        if np.count_nonzero(filtered) == 1:
            break
        buffer = m[bit, :] & filtered
        ones = np.count_nonzero(buffer)
        total = np.count_nonzero(filtered)

        bitval = 2 * ones >= total

        filtered &= buffer ^ bitval ^ inv

    for i in range(len(filtered)):
        if filtered[i]:
            index = i
            break

    n = 0
    for bit in m[:, index]:
        n = 2 * n + (1 if bit else 0)

    return n


def part2():
    m = np.genfromtxt("input/day3/input", dtype=int, delimiter=1).T == 1
    filtered = np.ones(np.shape(m)[1], dtype=bool)
    bits = np.shape(m)[0]

    ox = single_out(m, True)
    co2 = single_out(m, False)

    print(f"{ox * co2}")


part1()
part2()
