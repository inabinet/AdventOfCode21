import numpy as np

with open('inputs/day20','r') as f:
    inputs = [i.strip() for i in f]


def process(inputList):
    tmp = inputList[0]
    algo = set([i for i,c in enumerate(tmp) if c=='#'])

    map = set()
    for y,row in enumerate(inputList[2:]):
        for x,col in enumerate(row):
            if col=='#':
                map.add(complex(x,y))

    return algo, map


def visualize(points):
    dims = [(p.real, p.imag) for p in points]
    xpnts,ypnts = list(zip(*dims))
    xmin = int(min(xpnts))
    xmax = int(max(xpnts))+1
    ymin = int(min(ypnts))
    ymax = int(max(ypnts))+1
    for y in range(ymin,ymax):
        for x in range(xmin,xmax):
            if complex(x,y) in points:
                char = '#'#'\u2588'
            else:
                char = '.'# '
            print(char, sep='', end='')
        print()


def applyAlgoToPoint(point, algo, map):
    positions = np.array([1+1j, 0+1j, -1+1j, 1+0j, 0+0j, -1+0j, 1-1j, 0-1j, -1-1j])
    points = point + positions

    val = 0
    for i in range(9):
        if points[i] in map:
            val += (1<<i)

    return int(val in algo)


def applyAlgoToMap(algo, map, cnt=2):
    noFlip = 0 not in algo
    for step in range(cnt):
        #find corners
        xList = [c.real for c in map]
        yList = [c.imag for c in map]
        offset = 4 if (noFlip or (step+1)%2) else -1
        minX = int(min(xList))-offset
        maxX = int(max(xList))+offset
        minY = int(min(yList))-offset
        maxY = int(max(yList))+offset

        newMap = set()
        # apply algo to all points in map
        for row in range(minY, maxY+1):
            for col in range(minX, maxX+1):
                point = complex(col,row)
                if applyAlgoToPoint(point, algo, map):
                    newMap.add(point)
        map = newMap

    return map


def part1(algo, map):
    out = applyAlgoToMap(algo, map, cnt=2)
    return(len(out))


def part2(algo, map):
    out = applyAlgoToMap(algo, map, cnt=50)
    return(len(out))



# Example
tmp = """\
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##\
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###\
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.\
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....\
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..\
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....\
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""


exampleInputs = [i.strip() for i in tmp.split('\n')]
example1 = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']

algo, map = process(exampleInputs)
#visualize(map)
print(part1(algo, map))
print(part2(algo, map))



# Part 1
algo, map = process(inputs)
print(part1(algo, map))


# Part 2
print(part2(algo, map))
