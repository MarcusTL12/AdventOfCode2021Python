import itertools
import numpy as np


def won_at(crosses, i, j):
    return np.all(crosses[i, :]) or np.all(crosses[:, j])


def part1():
    with open("input/day4/input") as f:
        draws = [int(x) for x in next(f).split(',')]
        boards = [np.array([int(x) for x in x.split()]).reshape(5, 5)
                  for x in f.read().strip().split("\n\n")]

    crossed = [np.zeros((5, 5), dtype=bool) for _ in range(len(boards))]

    for n in draws:
        for board, crossmat in zip(boards, crossed):
            for i, j in itertools.product(range(5), range(5)):
                if board[i, j] == n:
                    crossmat[i, j] = True
                    if won_at(crossmat, i, j):
                        return n * np.sum((1 - crossmat) * board)


def part2():
    with open("input/day4/input") as f:
        draws = [int(x) for x in next(f).split(',')]
        boards = [np.array([int(x) for x in x.split()]).reshape(5, 5)
                  for x in f.read().strip().split("\n\n")]

    crossed = [np.zeros((5, 5), dtype=bool) for _ in range(len(boards))]

    winners = [False for _ in range(len(boards))]

    for n in draws:
        for k, (board, crossmat) in enumerate(zip(boards, crossed)):
            if not winners[k]:
                for i, j in itertools.product(range(5), range(5)):
                    if board[i, j] == n:
                        crossmat[i, j] = True
                        if won_at(crossmat, i, j):
                            winners[k] = True
                            last_score = n * np.sum((1 - crossmat) * board)

    return last_score


if __name__ == "__main__":
    print(part1())
    print(part2())
