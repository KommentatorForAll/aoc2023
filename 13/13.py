def part_a():
    with open("input.txt") as f:
        areas = f.read().split("\n\n")

    rows = 0
    cols = 0
    for area in areas:
        area = area.split("\n")
        for i, row in enumerate(area):
            mirror = True
            for j in range(i-1, -1, -1):
                if i+(i-1-j) >= len(area):
                    break
                if area[j] != area[i+(i-1-j)]:
                    mirror = False
                    break
            if mirror:
                rows += i

        area = [list(x) for x in zip(*area)]
        for i, col in enumerate(area):
            mirror = True
            for j in range(i-1, -1, -1):
                if i+(i-1-j) >= len(area):
                    break
                if area[j] != area[i+(i-1-j)]:
                    mirror = False
                    break
            if mirror:
                cols += i

    print(f"Part A: {cols + (rows * 100)}")


def check_single_diff(arr1, arr2):
    diff = 0
    i = 0
    for a,b in zip(arr1, arr2):
        if a != b:
            diff += 1
        if diff > 1:
            return False
        i += 1
    return diff == 1


def part_b():
    with open("input.txt") as f:
        areas = f.read().split("\n\n")

    r = 0
    c = 0
    for area in areas:
        rows = 0
        cols = 0
        area = area.split("\n")
        for i, row in enumerate(area):
            mirror = True
            fixed = False
            for j in range(i-1, -1, -1):
                if i+(i-1-j) >= len(area):
                    break
                if area[j] != area[i+(i-1-j)]:
                    if fixed or not check_single_diff(area[j], area[i+(i-1-j)]):
                        mirror = False
                        break
                    fixed = True

            if mirror and fixed:
                rows += i

        area = [list(x) for x in zip(*area)]
        for i, col in enumerate(area):
            mirror = True
            fixed = False
            for j in range(i-1, -1, -1):
                if i+(i-1-j) >= len(area):
                    break
                if area[j] != area[i+(i-1-j)]:
                    if fixed or not check_single_diff(area[j], area[i+(i-1-j)]):
                        mirror = False
                        break
                    fixed = True
            if mirror and fixed:
                cols += i

        r += rows
        c += cols

    print(f"Part B: {c + (r * 100)}")


if __name__ == '__main__':
    part_a()
    part_b()
