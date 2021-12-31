from collections import defaultdict
import re
import numpy as np

reg = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")


def part1():
    board = defaultdict(int)
    with open("input/day5/input") as f:
        for l in f:
            m = reg.match(l)
            x0, y0, x1, y1 = (int(m.group(i)) for i in range(1, 5))
            if x0 == x1:
                y0, y1 = (y0, y1) if y0 <= y1 else (y1, y0)
                for y in range(y0, y1 + 1):
                    board[(x0, y)] += 1
            elif y0 == y1:
                x0, x1 = (x0, x1) if x0 <= x1 else (x1, x0)
                for x in range(x0, x1 + 1):
                    board[(x, y0)] += 1

    return sum(1 for v in board.values() if v >= 2)


def part2():
    board = defaultdict(int)
    with open("input/day5/input") as f:
        for l in f:
            m = reg.match(l)
            x0, y0, x1, y1 = (int(m.group(i)) for i in range(1, 5))
            dx = np.sign(x1 - x0)
            dy = np.sign(y1 - y0)
            while x0 != x1 or y0 != y1:
                board[(x0, y0)] += 1
                x0 += dx
                y0 += dy
            board[(x1, y1)] += 1

    return sum(1 for v in board.values() if v >= 2)


if __name__ == "__main__":
    print(part1())
    print(part2())
