import re

with open('day05.txt', 'r') as f:
    inputDat = f.read().splitlines()

maps = []
for line in inputDat[2:]:
    if 'map' in line:
        maps.append(dict())
    elif line != '':
        destination, source, length = [int(value) for value in line.split()]
        maps[-1][range(source, source + length)] \
            = range(destination, destination+length)

def reverseLookupSeed(location: int) -> int:
    value = location
    for curMap in reversed(maps):
        value = next(
            (srcRange.start + (value - destRange.start)
             for srcRange, destRange in curMap.items()
             if value in destRange),
            value
        )
    return value


initSeedDat = [int(seed) for seed in re.findall(r'\d+', inputDat[0])]
seedRanges = []
for index in range(0, len(initSeedDat) - 1, 2):
    start, length = initSeedDat[index:index + 2]
    seedRanges.append(range(start, start + length))

location = 0
while True:
    potentialSeed = reverseLookupSeed(location)
    if any(potentialSeed in seedRange for seedRange in seedRanges):
        print(location)
        break
    location += 1