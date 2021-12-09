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



# Example
tmp = """\
2199943210
3987894921
9856789892
8769896789
9899965678"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

print(part1(exampleInputs))


# Part 1
print(part1(inputs))


# Part 2

