import numpy as np

with open('inputs/day07','r') as f:
    inputs = [i.strip() for i in f]


def getFuel(crabList, verbose=False):
    crabs = crabList[:]
    # ncrabs = len(crabs)
    avg = crabs.mean()
    fuel = 0

    if verbose:
        print(crabs)

    while not all(crabs == avg):
        target = int(avg.round())
        hi = crabs > target
        lo = crabs < target
        nhi = hi.sum()
        nlo = lo.sum()

        if 0 < nhi < nlo:
            crabs = np.where(hi, crabs - 1, crabs)
            fuel += nhi
        elif 0 < nlo < nhi:
            crabs = np.where(lo, crabs + 1, crabs)
            fuel += nlo
        elif nhi > 0:
            crabs = np.where(hi, crabs - 1, crabs)
            fuel += nhi
        elif nlo > 0:
            crabs = np.where(lo, crabs + 1, crabs)
            fuel += nlo
        else:
            print('hmmmmm....')

        avg = crabs.mean()
        if verbose:
            print(crabs, target, avg, fuel)

    return fuel


# Example
tmp = """\
16,1,2,0,4,2,7,1,2,14"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

crabs = np.array([int(f) for f in exampleInputs[0].split(',')])
print(getFuel(crabs))



# Part 1

crabs = np.array([int(f) for f in inputs[0].split(',')])
print(getFuel(crabs))


# Part 2

