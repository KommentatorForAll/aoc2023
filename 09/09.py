def reducer(history):
    cng = []
    for i in range(1, len(history)):
        cng.append(history[i]-history[i-1])

    if len(set(cng)) == 1:
        return cng[0]
    else:
        return cng[-1] + reducer(cng)


def reducel(history):
    cng = []
    for i in range(1, len(history)):
        cng.append(history[i]-history[i-1])

    if len(set(cng)) == 1:
        return cng[0]
    else:
        v = cng[0] - reducel(cng)
        return v


def part_a():
    with open("input.txt") as f:
        histories = f.readlines()

    histories = [[int(i) for i in h.split(" ")] for h in histories]

    next_vals = [h[-1] + reducer(h) for h in histories]

    print(f"Part A: {sum(next_vals)}")


def part_b():
    with open("input.txt") as f:
        histories = f.readlines()

    histories = [[int(i) for i in h.split(" ")] for h in histories]

    next_vals = [h[0] - reducel(h) for h in histories]

    print(f"Part B: {sum(next_vals)}")


if __name__ == '__main__':
    part_a()
    part_b()
