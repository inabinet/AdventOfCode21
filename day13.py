import re

with open('inputs/day13','r') as f:
    inputs = [i.strip() for i in f]



def processInputs(inputList):
    sep = inputList.index('')

    points = set()
    for point in inputList[:sep]:
        x,y = point.split(',')
        pnt = complex(int(x),int(y))
        points.add(pnt)

    folds = []
    myre = re.compile('^fold along ([x|y])=(\d+)$')
    for ln in inputList[sep+1:]:
        if m := myre.match(ln):
            dim, loc = m.groups()
            loc = int(loc)
            if dim == 'y':
                loc *= 1j
            #print(ln, loc)
            folds.append(loc)

    return points, folds


def fold(points, fold):
    folded = set(points)
    vert = fold.real
    horz = fold.imag

    if vert:
        for pnt in points:
            if pnt.real > vert:
                folded.discard(pnt)
                newDim = 2*vert - pnt.real
                flip = complex(newDim, pnt.imag)
                folded.add(flip)
    else:
        for pnt in points:
            if pnt.imag > horz:
                folded.discard(pnt)
                newDim = 2*horz - pnt.imag
                flip = complex(pnt.real, newDim)
                folded.add(flip)

    return folded


def visiualize(points):
    dims = [(p.real, p.imag) for p in points]
    xpnts,ypnts = list(zip(*dims))
    xmax = int(max(xpnts))+1
    ymax = int(max(ypnts))+1
    for y in range(ymax):
        for x in range(xmax):
            if complex(x,y) in points:
                char = '#'
            else:
                char = '.'
            print(char, sep='', end='')
        print()



# Example
tmp = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

points, folds = processInputs(exampleInputs)
points = fold(points, folds[0])
print(len(points))


# Part 1
points, folds = processInputs(inputs)
points = fold(points, folds[0])
print(len(points))


# Part 2

