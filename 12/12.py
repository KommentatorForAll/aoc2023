import re
from typing import List


def check_line(state, sol):
    actual_state = []
    i = 0
    cnt = 0
    is_damaged = False
    for chr in state:
        if chr == ".":
            if is_damaged:
                if cnt != sol[i]:
                    return False
                i += 1
                actual_state.append(cnt)
                cnt = 0
                is_damaged = False
        else:
            cnt += 1
            is_damaged = True
    if is_damaged:
        actual_state.append(cnt)
    return actual_state == sol


def part_a():
    with open("input.txt") as f:
        springs = f.readlines()

    possibilities = 0

    for i, spring in enumerate(springs):
        if i% 100 == 0:
            print(i)
        state, pos = spring.split(" ")
        state:str
        pos = [int(i) for i in pos.split(",")]
        orig_state = state[:]
        for i in range(2**state.count("?")):
            state = orig_state[:]
            j = i
            while j > 0:
                if j % 2 == 0:
                    state = state.replace("?", "#", 1)
                else:
                    state = state.replace("?", ".", 1)
                j = j >> 1
            state = state.replace("?", "#")
            possibilities += check_line(state, pos)
    print(f"Part A: {possibilities}")


def solve(groups, sol):
    if len(sol) == 0:
        return 1
    poss = 0
    for g in groups[0]:
        i = 0
        valid = True
        for el in g:
            if sol[i] != el:
                valid = False
                break
            i += 1
        if valid:
            poss += solve(groups[1:], sol[i+1:])
    return poss


def part_b():
    with open("test.txt") as f:
        springs = f.read().split("\n")

    possibilities = 0

    for i, spring in enumerate(springs):
        if i % 100 == 0:
            print(i)
        state, pos = spring.split(" ")
        state:str
        pos = [int(i) for i in pos.split(",")]
        pos = pos * 5
        state = ((state[:] + "?")*5)[:-1]

        groups = []
        for g in re.split(r"\.+", state):
            if g == "":
                continue

            orig = g[:]
            grp = []
            for k in range(2**g.count("?")):
                g = orig[:]
                j = k
                while j > 0:
                    if j % 2 == 0:
                        g = g.replace("?", "#", 1)
                    else:
                        g = g.replace("?", ".", 1)
                    j = j >> 1
                g = g.replace("?", "#")
                p = [len(x) for x in g.split(".") if len(x) != 0]
                if p not in grp and p != []:
                    grp.append(p)
            groups.append(grp)
            #print(grp)
        poss = solve(groups, pos)
        print(pos, poss)
        possibilities += poss

    print(f"Part B: {possibilities}")


if __name__ == '__main__':
    #part_a()
    part_b()
