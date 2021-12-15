import numpy as np

with open('inputs/day15','r') as f:
    inputs = [i.strip() for i in f]



def getMap(inputValues):
    return np.array([[int(p) for p in row] for row in inputValues])


def getDistMap(cave):
    dist = np.copy(cave)
    diagMax = len(cave)

    diag = diagMax - 1
    while diag > 0:
        r = diag - 1
        # find down dist
        for c in range(diagMax - 1, diag - 1, -1):
            dist[r, c] += dist[diag, c]
        # find min dist
        for c in range(diagMax - 1, diag - 1, -1):
            left = dist[r, c - 1] if c > diag else 9999
            right = dist[r, c + 1] if c < diagMax - 1 else 9999
            dist[r, c] = cave[r, c] + min(left, right, dist[diag, c])
        c = diag - 1
        # find right dist
        for r in range(diagMax - 1, diag - 1, -1):
            dist[r, c] += dist[r, diag]
        # find min dist
        for r in range(diagMax - 1, diag - 1, -1):
            up = dist[r - 1, c] if r > diag else 9999
            down = dist[r + 1, c] if r < diagMax - 1 else 9999
            dist[r, c] = cave[r, c] + min(down, up, dist[r, diag])
        # find diag corner dist
        minAdj = min(dist[diag - 1, diag], dist[diag, diag - 1])
        dist[diag - 1, diag - 1] += minAdj
        diag -= 1

    return dist



# Example
tmp = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

cave = getMap(exampleInputs)
dist = getDistMap(cave)
print(dist[0,0] - cave[0,0])



# Part 1
cave = getMap(inputs)
dist = getDistMap(cave)
print(dist[0,0] - cave[0,0])


# Part 2

