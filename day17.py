import re
import numpy as np
from collections import defaultdict

with open('inputs/day17','r') as f:
    inputs = [i.strip() for i in f]



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


def getValidX(xrange):
    xArray = np.array(xrange)
    xMax = int(max(xArray))
    # all velocities in xrange are valid and will reach xcoor of target in one step
    xValid = defaultdict(list, {v:[1] for v in set(xArray)})

    # find 'n' for partial sums that are in xrange; these are valid and will stall (due to drag) in the xcoor of target
    # will use negative number as dict val to note that at or after this step, it will be in the range
    nArray = np.floor(np.sqrt(2*xArray))    # inverse triangle number; find n from partial sum
    nArray = np.array([n for n in nArray if int((n*(n+1))/2) in xArray])
    #nList = sorted(list(set(nArray)))       # find set of unique n's and cast to a sorted list
    for n in set(nArray.astype(int)):
        v = n
        p = 0
        #step = 0
        while p not in xrange:
            p += v
            v -= 1
            if v<=0 or p>xMax:
                break
            #step += 1
        xValid[n].append(-(n-v))  #step

    # finally, find velocities that will pass through xrange for step>1, but do not stall out within the xrange
    vstrt = int(max(nArray)) + 1
    vstop = int(min(xArray))
    for n in range(vstrt, vstop):
        v = n
        p = 0
        while p<=max(xrange):
            p += v
            v -= 1
            if p in xrange:
                xValid[n].append(n-v)

    return dict(xValid)


def getValidVelocities(xrange, yrange):
    valid = []
    yArray = np.array(yrange)
    yMin = min(yArray)
    yValid = getYHits(yrange)
    xValid = getValidX(xrange)
    for xVel, steps in xValid.items():
        for step in steps:
            if step<0:
                step = -step
                yVelocity = yMin-1
                yNeg = [True]
                while len(yNeg):
                    yVelocity += 1
                    yNeg = getYLocs(yVelocity, steps=-3*yMin+step)[step-1:]
                    if yVelocity>0:
                        tmp = np.where(yNeg==0)
                        if np.any(tmp):
                            idx = tmp[0][0]+1
                        else:
                            idx = 0
                        if yNeg[idx] < yMin:
                            break
                    if set(yNeg).intersection(yArray):
                        valid.append((xVel,yVelocity))
            elif step==1:
                valid.extend([(xVel,yVel) for yVel in yArray])
            else:
                yVelocity = yMin-1
                while True:
                    yVelocity += 1
                    yNeg = getYLocs(yVelocity, steps=step)[-1]
                    if yVelocity>0 and yNeg < yMin or yNeg > 0:
                        break
                    if yNeg in yArray:
                        valid.append((xVel,yVelocity))
    return set(valid)



def getXYRanges(inputArray):
    xmin, xmax, ymin, ymax = re.findall('(-?\d+)', inputArray[0])
    xrange = range(int(xmin), int(xmax) + 1)
    yrange = range(int(ymin), int(ymax) + 1)
    return xrange, yrange


def getYLocs(yVelocity, steps=50):
    stepList = np.array(range(-yVelocity, steps-yVelocity))
    yLocs = (yVelocity * (yVelocity + 1)) / 2 - (stepList * (stepList + 1)) / 2
    return yLocs.astype(int)


def getYHits(yrange):
    yArray = np.array(yrange)
    yMin = np.min(yArray)

    valid = []
    yVelocity = 0
    yNeg = [True]
    while len(yNeg):
        yVelocity += 1

        yNeg = getYLocs(yVelocity, steps=-3*yMin)[2*yVelocity+1:]
        if yNeg[0] < yMin:
            break
        if set(yNeg).intersection(yArray):
            valid.append(yVelocity)

    return valid




# Example
tmp = """\
target area: x=20..30, y=-10..-5"""

exampleInputs = [i.strip() for i in tmp.split('\n')]


xrange, yrange = getXYRanges(exampleInputs)
yVelocity = max(getYHits(yrange))
maxHeight = int((yVelocity*(yVelocity+1))/2)
print(maxHeight)
allVs = getValidVelocities(xrange, yrange)
print(len(allVs))


# Part 1
xrange, yrange = getXYRanges(inputs)
yVelocity = max(getYHits(yrange))
maxHeight = int((yVelocity*(yVelocity+1))/2)
print(maxHeight)


# Part 2
allVs = getValidVelocities(xrange, yrange)
print(len(allVs))
