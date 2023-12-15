def part_a():
    with open("input.txt") as f:
        lines = f.readlines()

    galaxies = set()
    empty_cols = []

    lines = [line[:-1] for line in lines]

    i = 0
    add_y = 0
    while i < len(lines):
        if set(lines[i]) == {"."}:
            add_y += 1
            i += 1
            continue
        for j, c in enumerate(lines[i]):
            if c == ".":
                if i == 0 and set([lines[y][j] for y in range(len(lines))]) == {"."}:
                    empty_cols.append(j)
            else:
                galaxies.add((i + add_y, j + len([c for c in empty_cols if c < j])))
        i += 1

    distance = 0
    pairs = 0

    gall = list(galaxies)

    for i, gal in enumerate(gall):
        j = i+1
        while j < len(gall):
            gal2 = gall[j]
            j += 1
            pairs += 1
            distance += abs(gal[0]-gal2[0]) + abs(gal[1]-gal2[1])

    print(f"Part A: {distance}, {pairs=}")


def part_b():
    with open("input.txt") as f:
        lines = f.readlines()

    galaxies = set()
    empty_cols = []

    lines = [line[:-1] for line in lines]

    i = 0
    add_y = 0
    while i < len(lines):
        if set(lines[i]) == {"."}:
            add_y += 999999
            i += 1
            continue
        for j, c in enumerate(lines[i]):
            if c == ".":
                if i == 0 and set([lines[y][j] for y in range(len(lines))]) == {"."}:
                    empty_cols.append(j)
            else:
                galaxies.add((i + add_y, j + (len([c for c in empty_cols if c < j])*999999)))
        i += 1

    distance = 0
    pairs = 0

    gall = list(galaxies)

    for i, gal in enumerate(gall):
        j = i + 1
        while j < len(gall):
            gal2 = gall[j]
            j += 1
            pairs += 1
            distance += abs(gal[0] - gal2[0]) + abs(gal[1] - gal2[1])

    print(f"Part B: {distance}, {pairs=}")


if __name__ == '__main__':
    part_a()
    part_b()
