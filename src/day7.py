import numpy as np


def part1():
    inp = np.loadtxt("input/day7/input", dtype=int, delimiter=',')
    mid = int(np.median(inp))
    return np.sum(np.abs(inp - mid))


def trig_num(x):
    return x * (x + 1) // 2


def part2():
    inp = np.loadtxt("input/day7/input", dtype=int, delimiter=',')
    mid = np.mean(inp)
    l = int(np.floor(mid))
    h = int(np.ceil(mid))

    return min(sum(trig_num(np.abs(inp - l))), sum(trig_num(np.abs(inp - h))))


if __name__ == "__main__":
    print(part1())
    print(part2())
