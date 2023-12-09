from functools import reduce

with open('day09.txt', 'r') as f:
    lines = [list(map(int, line.strip().split())) for line in f.readlines()]
    input = lines

def findNextValue(seq):
    lastVal = seq[-1]
    lastVals = [lastVal]
    while lastVal:
        reducedSeq = [y-x for x, y in list(zip(seq[:-1], seq[1:]))]
        lastVal = reducedSeq[-1]
        lastVals.append(lastVal)
        seq = reducedSeq
    return sum(lastVals)

def findPrevVal(seq):
    firstVal = seq[0]
    firstVals = [firstVal]
    lastVal = seq[-1]
    lastVals = [lastVal]

    while lastVal:
        reducedSeq = [y-x for x, y in list(zip(seq[:-1], seq[1:]))]
        firstVal = reducedSeq[0]
        firstVals.append(firstVal)
        lastVal = reducedSeq[-1]
        lastVals.append(lastVal)
        seq = reducedSeq
    firstVals = list(reversed(firstVals))
    predicted = reduce(lambda x, y: y - x, firstVals)
    return predicted

def part1(input):
    solution = 0
    for seq in input:
        solution += findNextValue(seq)
    print("Part One: " + str(solution))
    return solution

def part2(input):
    solution = 0
    for seq in input:
        solution += findPrevVal(seq)
    print("Part Two: " + str(solution))
    return solution

part1(input)
part2(input)