import re

# this pattern returns true when only dots and digits found
PATTERN = r'^[.\d]+$'

sum = 0

with open("day03.txt") as f:
    lines = f.readlines()

    for line_index, currLine in enumerate(lines):
        currLine = ''.join(currLine)
        digitStartPos = None
        digitEndPos = None

        if line_index == 0:
            prevLine = currLine
        if line_index >= len(lines)-1:
            nextLine = currLine
        else:
            nextLine = lines[line_index+1]
           
        for pos, c in enumerate(currLine):

            # start of sequence
            if c.isdigit() and digitStartPos is None:
                digitStartPos = pos
                digitEndPos = pos

            # currently in sequence
            elif c.isdigit() and digitStartPos is not None:
                digitEndPos = pos

            # end of sequence
            elif not c.isdigit() and digitStartPos is not None:

                if digitStartPos > 0:
                    tmp = digitStartPos - 1
                else:
                    tmp = 0

                # now check for symbols in sequence surroundings, same for prev and next sequence
                if not bool(re.match(PATTERN, currLine[tmp:digitEndPos+2])) or \
                    not bool(re.match(PATTERN, prevLine[tmp:digitEndPos+2])) or \
                    not bool(re.match(PATTERN, nextLine[tmp:digitEndPos+2])):
                    partNumber = ''.join(currLine[digitStartPos:digitEndPos+1])
                    sum += int(partNumber)
                
                digitStartPos = None
                digitEndPos = None

        prevLine = currLine
    
print(sum)