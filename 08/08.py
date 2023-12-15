import math
import time


def part_a():
    with open("input.txt") as f:
        content = f.readlines()

    instructions = content[0][:-1]

    map = content[2:]
    network = {}
    for line in map:
        pos, connections = line.split(" = ")
        connections = connections[1:-2].split(", ")
        network[pos] = connections

    # print(network)

    pos = 'AAA'
    i = 0
    while pos != 'ZZZ':
        # print(f"{pos=}, {i=} {instructions[i % len(instructions)]}")
        pos = network[pos][instructions[i % len(instructions)] == 'R']

        i += 1

    print(f"Part A: {i}")


def part_b():
    t0 = time.time()
    with open("input.txt") as f:
        content = f.readlines()

    instructions = content[0][:-1]

    map = content[2:]
    network = {}
    for line in map:
        pos, connections = line.split(" = ")
        connections = connections[1:-2].split(", ")
        network[pos] = connections

    positions = [n for n in network.keys() if n.endswith("A")]
    to_reach_z = {}

    for spos in positions:
        visited = {}
        i = 0
        pos = spos
        inst_i = i
        while pos not in visited or visited[pos] != inst_i:
            visited[pos] = inst_i
            if pos.endswith("Z"):
                to_reach_z[spos] = i
            pos = network[pos][instructions[inst_i] == 'R']

            i += 1
            inst_i = i % len(instructions)

    steps = math.lcm(*to_reach_z.values())
    print(f"{time.time()-t0} sekunden")
    print(f"Part B: {steps}")


if __name__ == '__main__':
    part_a()
    part_b()
