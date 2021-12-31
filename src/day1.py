from collections import deque
from time import time


def part1():
    with open("input/day1/input") as f:
        prev = 2**63
        ans = 0
        for l in f:
            n = int(l)
            if n > prev:
                ans += 1
            prev = n
    return ans


def part2():
    with open("input/day1/input") as f:
        q = deque()
        ans = 0
        for l in f:
            n = int(l)
            q.append(n)
            if len(q) > 3:
                prev = q.popleft()
                if n > prev:
                    ans += 1
    return ans


if __name__ == "__main__":
    print(part1())
    print(part2())
