import time


def part_a():
    with open("input.txt") as f:
        content = f.readlines()

    starting_position = (0, 0)
    for i, line in enumerate(content):
        if line.find("S") != -1:
            starting_position = (i, line.find("S"))
            break

    visited = set()
    to_visit = set()
    visiting = set()
    if content[starting_position[0] - 1][starting_position[1]] in ["7", "F", "|"]:
        to_visit.add((starting_position[0]-1, starting_position[1]))

    if content[starting_position[0] + 1][starting_position[1]] in ["L", "J", "|"]:
        to_visit.add((starting_position[0] + 1, starting_position[1]))

    if content[starting_position[0]][starting_position[1] - 1] in ["L", "F", "-"]:
        to_visit.add((starting_position[0], starting_position[1] - 1))

    if content[starting_position[0]][starting_position[1] + 1] in ["J", "7", "-"]:
        to_visit.add((starting_position[0], starting_position[1] + 1))

    steps = 1
    while len(to_visit) > 0:
        visiting = to_visit
        to_visit = set()
        steps += 1
        # print(f"{visiting=}, {visited=}")
        for pos in visiting:
            up = False
            down = False
            left = False
            right = False

            if content[pos[0]][pos[1]] == "7":
                left = True
                down = True
            if content[pos[0]][pos[1]] == "|":
                up = True
                down = True
            if content[pos[0]][pos[1]] == "F":
                right = True
                down = True
            if content[pos[0]][pos[1]] == "J":
                up = True
                left = True
            if content[pos[0]][pos[1]] == "L":
                up = True
                right = True
            if content[pos[0]][pos[1]] == "-":
                left = True
                right = True

            if left and (pos[0], pos[1]-1) not in visited:
                to_visit.add((pos[0], pos[1]-1))
            if right and (pos[0], pos[1]+1) not in visited:
                to_visit.add((pos[0], pos[1]+1))
            if up and (pos[0]-1, pos[1]) not in visited:
                to_visit.add((pos[0]-1, pos[1]))
            if down and (pos[0]+1, pos[1]) not in visited:
                to_visit.add((pos[0]+1, pos[1]))

        visited |= visiting

    print(f"Part A: {steps-1}")

    in_bounds = set()
    for y in range(len(content)):
        on_line = False
        entered_top = False
        in_line = 0
        for x in range(len(content[0])):
            if (y, x) in visited:
                sym = content[y][x]
                if sym == "S":
                    sym = "L"
                if sym == "|":
                    in_line += 1
                elif sym == "F":
                    entered_top = False
                elif sym == "L":
                    entered_top = True
                elif sym in ["J", "7"]:
                    if (sym == "J") != entered_top:
                        in_line += 1

            elif in_line % 2 == 1:
                in_bounds.add((y, x))

    # for y in range(len(content)):
    #     for x in range(len(content[0])):
    #         if (y, x) in visited:
    #             print(content[y][x], end="")
    #         elif (y, x) in in_bounds:
    #             print("O", end="")
    #         else:
    #             print(".", end="")
    #     print()

    print(f"Part B: {len(in_bounds)}")


if __name__ == '__main__':
    t0 = time.time()
    for i in range(1000):
        part_a()
    t1 = time.time()
    print(f"Avg Time: {(t1-t0)/1000}")
