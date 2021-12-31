#! /usr/local/bin/python3.10
from time import time
import sys

if __name__ == "__main__":
    if sys.argv[1] in ['-t', '--time']:
        timing = True
        off = 1
    else:
        timing = False
        off = 0

    if len(sys.argv) >= off + 3:
        day = int(sys.argv[off + 1])
        part = int(sys.argv[off + 2])
    else:
        print("give day and part as parameters")
        exit(0)

    with open("day.py", "w") as day_file:
        day_file.write(f"from src.day{day} import part1, part2")

    from day import part1, part2

    f = part1 if part == 1 else part2

    if not timing:
        print(f())
    else:
        ans = f()
        t0 = time()

        runs = 0

        if len(sys.argv) >= off + 4:
            time_target = float(sys.argv[off + 3])
        else:
            time_target = 1

        while time() - t0 < time_target:
            f()
            runs += 1
        
        t = time() - t0

        at = t / runs

        s = int(at)
        ms = int((at - s) * 1000)
        µs = int((at - s - ms / 1000) * 1000000)

        print(f"Average time: {s} s, {ms} ms, {µs} µs per run")
        print(f"Total time: {t:.3f} s over {runs} iterations")
        print(ans)

