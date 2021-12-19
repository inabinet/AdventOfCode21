import re
import numpy as np

with open('inputs/day17','r') as f:
    inputs = [i.strip() for i in f]



'''
def step(position, velocity):
    position[0] += velocity[0]
    position[1] += velocity[1]
    velocity[0] = max(velocity[0]-1, 0)
    velocity[1] -= 1
    return position, velocity


def run(position, velocity, n=10):
    for _ in range(n):
        print(position, velocity)
        position, velocity = step(position, velocity)


def getXStops(xrange):
    xArray = np.array(xrange)
    nArray = np.floor(np.sqrt(2*xArray))    # inverse triangle number; find n from partial sum
    return set(nArray)
'''


def getXYRanges(inputArray):
    xmin, xmax, ymin, ymax = re.findall('(-?\d+)', inputArray[0])
    xrange = range(int(xmin), int(xmax) + 1)
    yrange = range(int(ymin), int(ymax) + 1)
    return xrange, yrange


def getYHits(yrange):
    yArray = np.abs(np.array(yrange))
    yMax = np.max(yArray)
    n = int(np.floor(np.sqrt(2*yMax)))  # inverse triangle number; find n from partial sum
    n *= 10  # double to make sure range is covered
    nList = np.array(range(n))

    valid = []
    yVelocity = 0
    yPos = [True]
    while len(yPos):    # potentially inefficient (can I just see when the first step is larger than range?)
        yVelocity += 1
        yPos = (nList * (nList + 1)) / 2 - (yVelocity * (yVelocity + 1)) / 2
        yPos = yPos.astype(int)[yVelocity:]
        if set(yPos).intersection(yArray):
            valid.append(yVelocity)

    return max(valid)




# Example
tmp = """\
target area: x=20..30, y=-10..-5"""

exampleInputs = [i.strip() for i in tmp.split('\n')]


xrange, yrange = getXYRanges(exampleInputs)
yVelocity = getYHits(yrange)
maxHeight = int((yVelocity*(yVelocity+1))/2)
print(maxHeight)



# Part 1
xrange, yrange = getXYRanges(inputs)
yVelocity = getYHits(yrange)
maxHeight = int((yVelocity*(yVelocity+1))/2)
print(maxHeight)


# Part 2

