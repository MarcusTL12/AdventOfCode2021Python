
def part1():
    x = y = 0
    with open("input/day2/input") as f:
        for line in f:
            d, l = line.split()
            l = int(l)
            match d:
                case "forward": x += l
                case "down": y += l
                case "up": y -= l
    print(x * y)


def part2():
    x = y = tilt = 0
    with open("input/day2/input") as f:
        for line in f:
            d, l = line.split()
            l = int(l)
            match d:
                case "forward":
                    x += l
                    y += tilt * l
                case "down": tilt += l
                case "up": tilt -= l
    print(x * y)


part1()
part2()
