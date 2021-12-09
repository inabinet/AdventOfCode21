import numpy as np

with open('inputs/day09','r') as f:
    inputs = [i.strip() for i in f]


def getHeightMap(inputValues):
    return np.array([np.array([int(p) for p in row]) for row in inputValues])


def findMinIndexes(heightmap):
    # pad map and get directional shifted maps
    padded  = np.pad(heightmap,((1,1),(1,1)),constant_values=99)
    left    = np.pad(heightmap,((1,1),(0,2)),constant_values=99)
    right   = np.pad(heightmap,((1,1),(2,0)),constant_values=99)
    up      = np.pad(heightmap,((0,2),(1,1)),constant_values=99)
    down    = np.pad(heightmap,((2,0),(1,1)),constant_values=99)

    # calculate the max delta between each location and it's neighbor
    delta = padded - left
    delta = np.maximum(delta, padded-right)
    delta = np.maximum(delta, padded-up)
    delta = np.maximum(delta, padded-down)
    delta = delta[1:-1,1:-1]  # remove padding

    # get indexes where delta < 0 and return
    idxs = np.where(delta < 0)
    return idxs


def part1(inputValues):
    heightmap = getHeightMap(inputValues)
    idxs = findMinIndexes(heightmap)
    minheights = heightmap[idxs]
    risklevels = minheights + 1
    return risklevels.sum()


def part2(inputValues):
    heightmap = getHeightMap(inputValues)
    idxs = findMinIndexes(heightmap)
    lowpoints = list(zip(*idxs))

    basins = []
    for low in lowpoints:
        basin = climb(heightmap, low)
        basins.append(basin)

    sizes = [len(basin) for basin in basins]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def climb(map, start, path=None):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    xvalid = range(len(map))
    yvalid = range(len(map[0]))

    if path is None:
        path = {start}

    for dir in directions:
        x = start[0] + dir[0]
        y = start[1] + dir[1]
        point = (x,y)

        if (x in xvalid) and (y in yvalid):
            if point not in path:
                val = map[point]
                if val != 9:
                    path.add(point)
                    path = climb(map, point, path)

    return path



# Example
tmp = """\
2199943210
3987894921
9856789892
8767896789
9899965678"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

print(part1(exampleInputs))
print(part2(exampleInputs))


# Part 1
print(part1(inputs))


# Part 2
print(part2(inputs))
