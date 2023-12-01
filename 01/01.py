import re


def part_a():
    with open('input.txt') as f:
        lines = f.readlines()

    s = 0
    for line in lines:
        i = 0
        while not re.match(r"\d", line[i]):
            i += 1
        j = -1
        while not re.match(r"\d", line[j]):
            j -= 1
        s += int(line[i] + line[j])

    print(s)


def part_b():
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open('input.txt') as f:
        lines = f.readlines()

    s = 0
    for line in lines:
        lfind = {}
        rfind = {}
        for digit in digits:
            lfind[line.find(digit)] = digit
            rfind[line.rfind(digit)] = digit

        lfind = {k: v for k, v in lfind.items() if k != -1}
        rfind = {k: v for k, v in rfind.items() if k != -1}

        i = 0
        while not re.match(r"\d", line[i]):
            i += 1
        j = -1
        while not re.match(r"\d", line[j]):
            j -= 1
        j += len(line)

        index = 999 if len(lfind.keys()) == 0 else min(lfind.keys())
        if i < index:
            s += int(line[i])*10
        else:
            s += digits.index(lfind[index])*10

        index = -1 if len(rfind.keys()) == 0 else max(rfind.keys())
        if j > index:
            s += int(line[j])
        else:
            s += digits.index(rfind[index])

    print(s)


if __name__ == '__main__':
    part_a()
    part_b()
