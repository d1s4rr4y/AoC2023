import re

f = open('day06.txt','r')
times = f.readline()
distances = f.readline()

timeNums = re.findall(r'\d+', times)
distNums = re.findall(r'\d+', distances)

i = 0
for i in range(len(timeNums)):
    time = int(timeNums[i]) 
    hold = time
    dist = int(distNums[i])
    count = 0
    while hold >= 0:
        distance = (time - hold) * hold
        if distance > dist:
            count += 1
        hold -= 1
    print(count)
    
