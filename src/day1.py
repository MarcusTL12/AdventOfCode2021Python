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
    print(ans)


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
    print(ans)


t0 = time()
part1()
t1 = time()
part2()
t2 = time()

print(
    f"""Timing:
p1:  {t1 - t0:.5f} s
p2:  {t2 - t1:.5f} s
tot: {t2 - t0:.5f} s""")
