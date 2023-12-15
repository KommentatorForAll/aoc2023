import time


def part_a():

    with open("input.txt") as f:
        content = f.read()

    seeds = [int(i) for i in content.split("\n")[0].split(": ")[1].split(" ")]

    conversions = [conv.split(":\n")[1] for conv in content.split("\n\n")[1:]]

    for conversion in conversions:
        rules = [[int(i) for i in r.split(" ")] for r in conversion.split("\n")]

        for i, seed in enumerate(seeds):

            for rule in rules:
                if 0 <= seed - rule[1] <= rule[2]:
                    seeds[i] = rule[0] + (seed - rule[1])
                    break
    print(f"Part A: {min(seeds)}")


def compact_seeds(seeds):
    compacted = []
    for seed in seeds:
        did_compact = False
        for i, comp in enumerate(compacted):
            if comp[0] + comp[1] + 1 == seed[0]:
                compacted[i][1] = comp[1] + seed[1]
                did_compact = True
                break
            elif seed[0] + seed[1] + 1 == comp[0]:
                did_compact = True
                compacted[i][0] = seed[0]
                compacted[i][1] = comp[1] + seed[1]
                break
        if not did_compact:
            compacted.append(seed)
    return compacted


def do_overlap(range_a, range_b):
    return range_b[0] <= range_a[0] <= range_b[0] + range_b[1] or range_b[0] <= range_a[0] + range_a[1] <= range_b[0] + range_b[1]


def part_b():
    t_0 = time.time()
    with open("input.txt") as f:
        content = f.read()

    seeds = [int(i) for i in content.split("\n")[0].split(": ")[1].split(" ")]
    tmp = []
    for i in range(0, len(seeds), 2):
        tmp.append([seeds[i], seeds[i+1]-1])
    seeds = tmp
    # print(seeds)

    conversions = [conv.split(":\n")[1] for conv in content.split("\n\n")[1:]]
    cnt = len(conversions) - 1
    for ruleset_id, conversion in enumerate(conversions):
        print(f"running ruleset {ruleset_id}/{cnt}")
        rules = [[int(i) for i in r.split(" ")] for r in conversion.split("\n")]
        for i in range(len(rules)):
            rules[i][2] -= 1
        new_seed = []
        i = 0
        while i < len(seeds):
            seed = seeds[i]
            # print(i)
            i += 1
            found_rule = False
            for rule in rules:
                if do_overlap(seed, rule[1:]):
                    found_rule = True
                    lower = max(seed[0], rule[1])
                    upper = min(seed[0]+seed[1], rule[1]+rule[2])

                    new_seed.append([rule[0] + (lower - rule[1]), upper-lower])

                    # print(f"{rule=}")
                    if lower > seed[0]:
                        # print(f"adding lower {lower=}, {seed[0]=}")
                        seeds.append([seed[0], lower - seed[0] - 1])
                    if upper < seed[0] + seed[1]:
                        # print(f"adding upper {upper=}, {seed[0]+seed[1]=}")
                        seeds.append([upper+1, seed[0]+seed[1]-upper-1])
                    # print(new_seed)
                    # print(seeds)
                    # print()

            if not found_rule:
                new_seed.append(seed)
        # print(new_seed)
        print(len(new_seed))
        seeds = compact_seeds(new_seed)
        print(len(seeds))
        # print(seeds)
        # print()
        # print()
    print(len(seeds))
    print(f"Part B: {min([seed[0] for seed in seeds])}")
    t_1 = time.time()
    print(f"ran in {t_1 - t_0} seconds")


if __name__ == '__main__':
    part_a()
    part_b()
