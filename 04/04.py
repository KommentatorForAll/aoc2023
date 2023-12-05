def part_a():
    with open("input.txt") as f:
        cards = f.readlines()

    points = 0
    for card in cards:
        lists = card.split(":")[1].split("|")
        winning_numbers = {int(i) for i in lists[1].strip().split(" ") if i != ''}
        your_numbers = {int(i) for i in lists[0].strip().split(" ") if i != ''}

        matching_numbers = winning_numbers & your_numbers

        if len(matching_numbers) != 0:
            points += 2 ** (len(matching_numbers)-1)

    print(f"Part A: {points}")


def part_b():
    with open("input.txt") as f:
        cards = f.readlines()

    card_instances = {i: 1 for i in range(len(cards))}
    card_instances[0] = 1

    for i, card in enumerate(cards):
        lists = card.split(":")[1].split("|")
        winning_numbers = {int(i) for i in lists[1].strip().split(" ") if i != ''}
        your_numbers = {int(i) for i in lists[0].strip().split(" ") if i != ''}

        matching_numbers = winning_numbers & your_numbers

        for j in range(i+1, i+len(matching_numbers)+1):
            card_instances[j] += card_instances[i]

    print(f"Part B: {sum(card_instances.values())}")


if __name__ == '__main__':
    part_a()
    part_b()
