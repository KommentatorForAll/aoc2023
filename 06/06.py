def part_a():
    with open("input.txt") as f:
        times, distances = f.readlines()
    times = [int(i) for i in times.split(":")[1].strip().split(" ") if i != '']
    distances = [int(i) for i in distances.split(":")[1].strip().split(" ") if i != '']

    p = 1
    for i in range(len(times)):
        possibilities = 0
        was_winning = False
        for t in range(1, times[i]):
            if t*(times[i]-t) > distances[i]:
                was_winning = True
                possibilities += 1
            elif was_winning:
                break
        p *= possibilities
    print(f"Part A: {p}")


def part_b():
    with open("input.txt") as f:
        times, distances = f.readlines()
    time = int(times.split(":")[1].replace(" ", ""))
    distance = int(distances.split(":")[1].replace(" ", ""))

    possibilities = 0
    was_winning = False
    for t in range(1, time):
        if t*(time-t) > distance:
            was_winning = True
            possibilities += 1
        elif was_winning:
            break
    print(f"Part B: {possibilities}")


if __name__ == '__main__':
    part_a()
    part_b()
