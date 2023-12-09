with open('day07.txt', 'r') as f:
    lines = f.read().splitlines()


def handType(hand: str) -> int:
    orderedTypes = [
        [5],             # Five of a kind
        [4, 1],          # Four of a kind
        [3, 2],          # Full house
        [3, 1, 1],       # Three of a kind
        [2, 2, 1],       # Two pair
        [2, 1, 1, 1],    # One pair
        [1, 1, 1, 1, 1]  # High card
    ]
    labelCounts = [hand.count(card) for card in set(hand)]
    labelCounts.sort(reverse=True)
    return orderedTypes.index(labelCounts)


def cardsAsInt(hand: str) -> tuple:
    orderedLabels = 'AKQJT98765432'
    return (orderedLabels.index(card) for card in hand)


hands = []  # (sortable) tuples of type, card values and bid
for line in lines:
    hand, bid = line.split(' ')
    encodedHand = (
        handType(hand),
        *cardsAsInt(hand),
        int(bid)
    )
    hands.append(encodedHand)

hands.sort(reverse=True)
winnings = sum(rank * hand[-1] for rank, hand in enumerate(hands, start=1))

print(winnings)