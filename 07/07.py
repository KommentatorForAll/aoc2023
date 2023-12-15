card_values = ['2','3','4','5','6','7','8','9','T', 'J', 'Q', 'K', 'A']


class Hand:
    def __init__(self, cards, bid):
        self.cards = []
        self.bid = bid
        self.cnt_map = {cv: 0 for cv in range(len(card_values))}
        for card in cards:
            v = card_values.index(card)
            self.cards.append(v)
            self.cnt_map[v] += 1

        self.native_value = max(self.cnt_map.values())
        if self.native_value == 3 and 2 in self.cnt_map.values():
            self.native_value = 3.5
        elif self.native_value == 2 and list(self.cnt_map.values()).count(2) == 2:
            self.native_value = 2.5

    def __lt__(self, other):
        if other.native_value > self.native_value:
            return True
        if other.native_value < self.native_value:
            return False
        for i in range(5):
            if self.cards[i] != other.cards[i]:
                return self.cards[i] < other.cards[i]
        return False


def part_a():
    with open("input.txt") as f:
        games = f.readlines()

    hands = []
    for game in games:
        cards, bid = game.split(" ")
        hands.append(Hand(cards, int(bid)))

    hands.sort()
    s = 0
    for i, hand in enumerate(hands):
        s += hand.bid * (i+1)

    print(f"Part A: {s}")


class HandB:
    def __init__(self, cards, bid):
        self.cards = []
        self.bid = bid
        self.cnt_map = {cv: 0 for cv in range(len(card_values))}
        self.joker = 0
        for card in cards:
            v = card_values.index(card)
            self.cards.append(v)
            self.cnt_map[v] += 1
        self.joker = self.cnt_map[9]
        self.cnt_map[9] = 0

        self.native_value = max(self.cnt_map.values()) + self.joker
        if (3 in self.cnt_map.values() and 2 in self.cnt_map.values()) or (self.joker == 1 and list(self.cnt_map.values()).count(2) == 2):
            self.native_value = 3.5
        elif self.native_value == 2 and list(self.cnt_map.values()).count(2) == 2:
            self.native_value = 2.5

    def __lt__(self, other):
        if other.native_value > self.native_value:
            return True
        if other.native_value < self.native_value:
            return False
        for i in range(5):
            if self.cards[i] != other.cards[i]:
                return self.cards[i] < other.cards[i]
        return False


def part_b():
    with open("input.txt") as f:
        games = f.readlines()

    hands = []
    for game in games:
        cards, bid = game.split(" ")
        hands.append(HandB(cards, int(bid)))

    hands.sort()
    s = 0
    for i, hand in enumerate(hands):
        print(f"{hand.bid=} {hand.cards}, {hand.native_value}")
        s += hand.bid * (i+1)

    print(f"Part B: {s}")


if __name__ == '__main__':
    part_a()
    part_b()
