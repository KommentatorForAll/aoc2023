def part_a():
    games = extract_game()

    i = 0
    s = 0
    while i < len(games):
        if games[i]["red"] <= 12 and games[i]["green"] <= 13 and games[i]["blue"] <= 14:
            s += i
        i += 1

    print(f"Part A: {s}")


def part_b():
    games = extract_game()

    p = 0
    for game in games:
        p += game["red"] * game["blue"] * game["green"]

    print(f"Part B: {p}")


def extract_game():
    with open("input.txt") as f:
        lines = f.readlines()
    games = [{"red": 0, "blue": 0, "green": 0}]
    for line in lines:
        games.append(games[0].copy())
        for draw in line.split(":")[1].split(";"):
            colors = draw.split(",")
            for color in colors:
                cnt, name = color.strip().split(" ")
                games[-1][name] = max(games[-1][name], int(cnt))
    return games


if __name__ == '__main__':
    part_a()
    part_b()
