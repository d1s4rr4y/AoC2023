import re

f = open('day01.txt', 'r')
lines = f.readlines()

total = 0
for l in lines:
    re.sub()
    l = l.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
    numLeft = False
    i = 0
    while numLeft != True:
        while i < len(l):
            if l[i].isdigit():
                intLeft = l[i]
                numLeft = True
                break
            else:
                i = i + 1

    numRight = False
    j = len(l) - 1
    while numRight != True:
        while j >= 0:
            if l[j].isdigit():
                intRight = l[j]
                numRight = True
                break
            else:
                j = j - 1
    thisInt = int(intLeft + intRight)
    total = total + thisInt


print("Part Two: " + str(total))