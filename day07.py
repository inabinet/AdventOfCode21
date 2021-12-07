import numpy as np

with open('inputs/day07','r') as f:
    inputs = [i.strip() for i in f]


def getFuelNew(crabList, constantFuelRate=True, verbose=False):
    crabs = crabList[:]
    pos = list(range(crabs.min(), crabs.max()+1))
    fuel = []

    for p in pos:
        dist = abs(crabs-p)
        if not constantFuelRate:
            dist = 0.5 * dist * (dist+1)
        req = dist.sum()
        fuel.append(req)

    if verbose:
        print(fuel, min(fuel))

    return int(min(fuel))


# Example
tmp = """\
16,1,2,0,4,2,7,1,2,14"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

crabs = np.array([int(f) for f in exampleInputs[0].split(',')])
print(getFuelNew(crabs))
print(getFuelNew(crabs, constantFuelRate=False))


# Part 1
crabs = np.array([int(f) for f in inputs[0].split(',')])
print(getFuelNew(crabs))


# Part 2
print(getFuelNew(crabs, constantFuelRate=False))
