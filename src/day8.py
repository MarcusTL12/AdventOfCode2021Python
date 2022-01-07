import itertools
from multiprocessing import Pool


def part1():
    with open("input/day8/input") as f:
        return sum(sum(1 for d in l.strip().split(' | ')[1].split()
                       if len(d) in (2, 3, 4, 7)) for l in f)


def findnum(args):
    valid_segments, l = args
    firstparts, secondparts = l.strip().split(' | ')
    for perm in itertools.permutations(range(7)):
        is_valid = True
        for part in firstparts.split():
            segments = [0] * 7
            for c in part:
                i = ord(c) - ord('a')
                segments[perm[i]] = 1
            is_valid &= tuple(segments) in valid_segments
        if is_valid:
            break

    num = 0

    for part in secondparts.split():
        segments = [0] * 7
        for c in part:
            i = ord(c) - ord('a')
            segments[perm[i]] = 1
        num = 10 * num + valid_segments[tuple(segments)]

    return num


def part2():
    valid_segments = {
        (1, 1, 1, 0, 1, 1, 1): 0,
        (0, 0, 1, 0, 0, 1, 0): 1,
        (1, 0, 1, 1, 1, 0, 1): 2,
        (1, 0, 1, 1, 0, 1, 1): 3,
        (0, 1, 1, 1, 0, 1, 0): 4,
        (1, 1, 0, 1, 0, 1, 1): 5,
        (1, 1, 0, 1, 1, 1, 1): 6,
        (1, 0, 1, 0, 0, 1, 0): 7,
        (1, 1, 1, 1, 1, 1, 1): 8,
        (1, 1, 1, 1, 0, 1, 1): 9,
    }

    with open("input/day8/input") as f:
        with Pool() as p:
            ans = sum(p.map(findnum, ((valid_segments, l) for l in f)))

    return ans


if __name__ == "__main__":
    print(part1())
    print(part2())
