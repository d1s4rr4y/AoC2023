import re

f = open('day02.txt', 'r')
lines = f.readlines()

total = 0
for l in lines:
    valid = True
    temp = re.findall(r'\d+', l)
    res = list(map(int, temp))
    gameNo = res[0] 

    listRed = list(map(int, re.findall(r'(\d+) red', l)))
    listGreen = list(map(int, re.findall(r'(\d+) green', l)))
    listBlue = list(map(int, re.findall(r'(\d+) blue', l)))
    for i in range (0, len(listRed)):
        if int(listRed[i]) > 12:
            valid = False
    for j in range (0, len(listGreen)):
        if int(listGreen[j]) > 13:
            valid = False
    for k in range (0, len(listBlue)):
        if int(listBlue[k]) > 14:
            valid = False
    if valid == True:
        total = total + gameNo
    
    
print(total)
print(sum(max(list(map(int, re.findall(r'(\d+) red', l)))) * max(list(map(int, re.findall(r'(\d+) green', l)))) * max(list(map(int, re.findall(r'(\d+) blue', l)))) for l in open('day02.txt', 'r').readlines()))

