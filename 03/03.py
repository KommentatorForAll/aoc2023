import re


def part_a():
    with open("input.txt") as f:
        schematic = f.readlines()

    matches = []
    for line in schematic:
        matches.append(re.finditer(r"(\d+)", line))

    s = 0
    for i, line_matches in enumerate(matches):
        for match in line_matches:
            area = [0, 0]
            area[0] = match.start()
            area[1] = match.end()

            value = int(match.group())

            is_part = False

            if i > 0:
                print(schematic[i - 1][max(0, area[0] - 1):min(len(schematic[i]) - 1, area[1] + 1)])
            print(schematic[i][
                                          max(0, area[0] - 1):min(len(schematic[i]) - 1, area[1] + 1)])
            if i < len(schematic)-1:
                print(schematic[i + 1][
                                          max(0, area[0] - 1):min(len(schematic[i]) - 1, area[1] + 1)])

            if i > 0 and not re.match(r"^(\.|\d)*$",
                                      schematic[i - 1][max(0, area[0] - 1):min(len(schematic[i]) - 1, area[1] + 1)]):
                print(f"found upper: {value}")
                is_part = True
            if i < len(schematic) - 1 and not re.match(r"^(\.|\d)*$", schematic[i + 1][
                                          max(0, area[0] - 1):min(len(schematic[i]) - 1, area[1] + 1)]):
                print(f"found lower: {value}")
                is_part = True
            if not re.match(r"^(\.|\d)*$", schematic[i][
                                          max(0, area[0] - 1):min(len(schematic[i]) - 1, area[1] + 1)]):
                print(f"found same: {value}")
                is_part = True
            if is_part:
                s += value
            else:
                print(f"skipped {value}")

    print(f"Part A: {s}")


def part_b():
    with open("input.txt") as f:
        schematic = f.readlines()

    s = 0
    for i, line in enumerate(schematic):
        start_at = 0
        while line.find("*", start_at) != -1:
            numbers = []
            idx = line.find("*", start_at)
            start_at = idx + 1
            if idx > 0 and re.match(r"\d", line[idx - 1]):
                numbers.append(int(re.findall(r"(\d+)", line[:idx])[-1]))
            if idx < len(line) - 2 and re.match(r"\d", line[idx + 1]):
                numbers.append(int(re.findall(r"(\d+)", line[idx:])[0]))

            matches = []
            if i > 0:
                matches = re.finditer(r"(\d+)", schematic[i-1])
                for match in matches:
                    if idx - 1 <= match.start() <= idx + 1 or idx - 1 <= match.end()-1 <= idx:
                        numbers.append(int(match.group()))

            if i < len(schematic) - 1:
                matches = re.finditer(r"(\d+)", schematic[i+1])
                for match in matches:
                    if idx - 1 <= match.start() <= idx + 1 or idx - 1 <= match.end()-1 <= idx:
                        numbers.append(int(match.group()))

            if len(numbers) == 2:
                s += numbers[0] * numbers[1]
    print(f"Part B: {s}")


if __name__ == '__main__':
    part_a()
    part_b()
