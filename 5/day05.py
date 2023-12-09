import re

with open('day05.txt', 'r') as f:
    lines = f.read().splitlines()

maps = []
for line in lines[2:]:
    if 'map' in line:
        maps.append(dict())
    elif line != '':
        destination, source, length = [int(value) for value in line.split()]
        maps[-1][range(source, source + length)] \
            = range(destination, destination + length)

def lookupLocation(initVal: int) -> int:
    val = initVal
    for curMap in maps:
        val = next(
            (destinationRange.start + (val - sourceRange.start) 
            for sourceRange, destinationRange in curMap.items() 
            if val in sourceRange),
            val
        )
    return val

seeds = [int(seed) for seed in re.findall(r'\d+', lines[0])]
locations = [lookupLocation(seed) for seed in seeds]
print(min(locations))