def part_a():
    with open("input.txt") as f:
        platform = f.read().split("\n")

    v = 0
    m = len(platform[0])
    stops = [len(platform)] * m
    for j, row in enumerate(platform):
        for i, c in enumerate(row):
            if c == "#":
                stops[i] = m-j-1
            elif c == "O":
                v += stops[i]
                stops[i] -= 1

    print(f"Part A: {v}")


def part_b():
    with open("input.txt") as f:
        platform = f.read().split("\n")

    platform = [list(x) for x in platform]

    def rotate(plat):
        for _ in range(1):
            plat = [list(x) for x in zip(*plat[::-1])]
        return plat

    def to_key(plat):
        f = ""
        for l in plat:
            f += "".join(l) + "\n"
        return f

    m = len(platform[0])

    cache = {}
    cycle_size = 0
    it = 0

    for cycle in range(1_000_000_000):
        k = to_key(platform)
        if k in cache:
            v = cache[k]
            cycle_size = cycle - v
            it = v
            break
        else:
            cache[k] = cycle
        if cycle % 10000 == 0:
            print(cycle)
        for direction in range(4):
            stops = [0] * m
            for j, row in enumerate(platform):
                for i, c in enumerate(row):
                    if c == "#":
                        stops[i] = j+1
                    elif c == "O":
                        platform[j][i] = "."
                        platform[stops[i]][i] = "O"
                        stops[i] += 1

            platform = rotate(platform)

    reversed_cache = {v: k for k, v in cache.items()}
    remaining = (1_000_000_000 - it) % cycle_size
    platform = reversed_cache[it + remaining]

    v = 0
    for j, row in enumerate(platform.split("\n")):
        for c in row:
            if c == "O":
                v += m-j

    print(f"Part B: {v}")


if __name__ == '__main__':
    part_a()
    part_b()
