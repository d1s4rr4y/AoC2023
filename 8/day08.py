import re

with open('day08.txt', 'r') as f:
    lines = f.read().splitlines()

network = {}
for l in lines[2:]:
    node, left, right = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', l)[0]
    network[node] = (left, right)


def directionSequence() -> str:
    seq = lines[0]
    while True:
        for dir in seq:
            yield dir


curNode = 'AAA'
counter = 0
instruction = directionSequence()
while curNode != 'ZZZ':
    nextL, nextR = network[curNode]
    curNode = nextL if next(instruction) == 'L' else nextR
    counter += 1

print(counter)