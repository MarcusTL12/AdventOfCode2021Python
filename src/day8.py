import numpy as np


def part1():
    with open("input/day8/input") as f:
        return sum(sum(1 for d in l.strip().split(' | ')[1].split()
                       if len(d) in (2, 3, 4, 7)) for l in f)


# def gen_segment_matrix(nums):
#     segs = np.zeros((10, 7), dtype=bool)
#     for i, num in enumerate(nums):
#         for c in num:
#             j = c - ord('a')
#             segs[i, j] = True
#     return segs


def find_perm(nums):
    segs = np.zeros((10, 7), dtype=bool)
    for i, num in enumerate(nums):
        for c in num:
            j = ord(c) - ord('a')
            segs[i, j] = True

    perm = [i for i in range(7)]
    perm.sort(key=lambda i: np.sum(segs[:, i]))
    perm = np.array(perm)[[4, 1, 5, 2, 0, 6, 3]]

    print(segs)
    print(perm)
    print(segs[:, perm])

    rsums = [sum(r) for r in segs[:, perm]]
    print(rsums)
    one_ind = next(i for i in range(len(rsums)) if rsums[i] == 2)
    four_ind = next(i for i in range(len(rsums)) if rsums[i] == 4)

    if segs[one_ind, perm[1]]:
        perm = perm[[2, 1, 0, 3, 4, 5, 6]]

    if segs[four_ind, perm[4]]:
        perm = perm[[0, 1, 2, 6, 4, 5, 3]]

    return perm


s = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab"
perm = find_perm(s.split())
print(perm)


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

    total = 0

    with open("input/day8/input") as f:
        for l in f:
            firstparts, secondparts = l.strip().split(" | ")

            perm = find_perm(firstparts.split())

            num = 0

            for part in secondparts.split():
                segments = np.zeros(7, dtype=int)
                for c in part:
                    i = ord(c) - ord('a')
                    segments[i] = 1
                segments = tuple(segments[perm])
                num = 10 * num + valid_segments[segments]

            total += num

    return total


# if __name__ == "__main__":
#     print(part1())
#     print(part2())
