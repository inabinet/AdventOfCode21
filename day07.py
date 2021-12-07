import numpy as np

with open('inputs/day07','r') as f:
    inputs = [i.strip() for i in f]


def getFuel(crabList, constantFuelRate=True, verbose=False):
    crabs = crabList[:]

    avg = crabs.mean()
    fuel = np.array([0 for _ in crabs])

    if verbose:
        print(crabs)

    while not all(crabs == avg):
        hi = crabs > avg
        lo = crabs < avg

        if constantFuelRate:
            fuelhi = np.where(hi, fuel + 1, fuel)
            fuello = np.where(lo, fuel + 1, fuel)
        else:
            n = np.floor(np.sqrt(2*fuel)) + 1   # find next n from current triangle number
            t = 0.5 * n * (n+1)                 # find triangle number for new n
            fuelhi = np.where(hi, t, fuel)
            fuello = np.where(lo, t, fuel)

        deltaFuelHi = fuelhi.sum() - fuel.sum()
        deltaFuelLo = fuello.sum() - fuel.sum()

        if 0 < deltaFuelHi < deltaFuelLo:
            crabs = np.where(hi, crabs - 1, crabs)
            fuel = fuelhi
        elif 0 < deltaFuelLo < deltaFuelHi:
            crabs = np.where(lo, crabs + 1, crabs)
            fuel = fuello
        elif deltaFuelHi > 0:
            crabs = np.where(hi, crabs - 1, crabs)
            fuel = fuelhi
        elif deltaFuelLo > 0:
            crabs = np.where(lo, crabs + 1, crabs)
            fuel = fuello
        else:
            print('hmmmmm....')


        avg = crabs.mean()
        if verbose:
            #print(crabs, avg, fuel, fuel.sum())
            print(list(crabs), avg, fuel.sum())

    return int(fuel.sum())


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
