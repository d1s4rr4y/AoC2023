import re
import math

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


counters = []
startingNodes = [node for node in network.keys() if node.endswith('A')]
for startNode in startingNodes:
    curNode = startNode
    counter = 0
    instruction = directionSequence()
    while not curNode.endswith('Z'):
        nextL, nextR = network[curNode]
        curNode = nextL if next(instruction) == 'L' else nextR
        counter += 1
    counters.append(counter)

print(math.lcm(*counters))