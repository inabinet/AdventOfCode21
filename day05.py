import re

with open('inputs/day05','r') as f:
    inputs = [i.strip() for i in f]


def part1(lineList):
    map = {}
    myre = re.compile('(\d+),(\d+)\s->\s(\d+),(\d+)')
    for line in lineList:
        points = myre.match(line).groups()
        x1, y1, x2, y2 = (int(i) for i in points)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                pos = complex(x1, y)
                if pos in map:
                    map[pos] += 1
                else:
                    map[pos] = 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                pos = complex(x, y1)
                if pos in map:
                    map[pos] += 1
                else:
                    map[pos] = 1
        else:
            pass  # per instructions, ignorning for now

    allPos = list(map.values())
    posOnly1 = allPos.count(1)
    return len(allPos) - posOnly1



# Example
tmp = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

print(part1(exampleInputs))


# Part 1
print(part1(inputs))

# Part 2
