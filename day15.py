import numpy as np
import heapq
from collections import defaultdict

with open('inputs/day15','r') as f:
    inputs = [i.strip() for i in f]



def getMap(inputValues):
    return np.array([[int(p) for p in row] for row in inputValues])


def expandMap(cave):
    tiles = [cave]
    for i in range(8):
        nxt = tiles[-1] + 1
        nxt = np.where(nxt == 10, 1, nxt)
        tiles.append(nxt)

    rows = []
    for i in range(5):
        row = np.concatenate(tiles[i:i+5], axis=1)
        rows.append(row)

    expandedCave = np.concatenate(rows, axis=0)

    return expandedCave


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


def getNeighbors(point, min, max):
    neighbors = []
    x, y = point
    xm = x - 1
    xp = x + 1
    ym = y - 1
    yp = y + 1

    if xm >= min:
        neighbors.append((xm, y))
    if xp <= max:
        neighbors.append((xp, y))
    if ym >= min:
        neighbors.append((x, ym))
    if yp <= max:
        neighbors.append((x, yp))

    return neighbors


def dijkstra(cave):
    start = (0, 0)
    caveMax = len(cave)-1

    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0    # start = (0,0)

    pq = [(distances[start], start)]
    while len(pq) > 0:
        dist, point = heapq.heappop(pq)

        if dist > distances[point]:
            continue

        for neighbor in getNeighbors(point, 0, caveMax):
            path = cave[neighbor]
            newDist = dist + path

            if newDist < distances[neighbor]:
                distances[neighbor] = newDist
                heapq.heappush(pq, (newDist, neighbor))

    #return distances
    return distances[(caveMax, caveMax)]



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
#dist = getDistMap(cave)
#print(dist[0,0] - cave[0,0])
print(dijkstra(cave))

bigcave = expandMap(cave)
#bigdist = getDistMap(bigcave)
#print(bigdist[0,0] - bigcave[0,0])
print(dijkstra(bigcave))


# Part 1
cave = getMap(inputs)
#dist = getDistMap(cave)
#print(dist[0,0] - cave[0,0])
print(dijkstra(cave))


# Part 2
bigcave = expandMap(cave)
#bigdist = getDistMap(bigcave)
#print(bigdist[0,0] - bigcave[0,0], '2870 is too big')
'''
My method was not general enough to solve this problem. (Seems to only work for right and down moves). I guessed the
correct answer by subtracting 2 from my solution. However, I wanted to go back and get a working algorithm before
moving on with new AOC puzzles. Learned Dijkstra's algorithm and about the binary heap class in Python. My function
heavily referenced https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
'''
print(dijkstra(bigcave))
