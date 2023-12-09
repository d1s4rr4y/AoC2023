import re
lines = open('day04.txt').read().strip().splitlines()
listCards = [1] * len(lines)

p1 = 0
# p2 = [1] * len(lines)

for l in lines:
    res = list(map(int, re.findall(r'\d+', l)))
    cardNo = res[0]
    res.pop(0)

    matches = len(res) - len(set(res))

    if matches == 0:
        p1 += 0
    else:
        p1 += 2**(matches - 1)

    for copy in range(listCards[lines.index(l)]):
        a = 1
        for i in range(matches):
            listCards[lines.index(l) + a] += 1
            a += 1

print("Part One: " + str(p1))
print("Part Two: " + str(sum(listCards)))
