import numpy as np

with open('inputs/day07','r') as f:
    inputs = [i.strip() for i in f]


def getFuel(crabList, verbose=False):
    crabs = crabList[:]

    avg = crabs.mean()
    fuel = np.array([0 for _ in crabs])

    if verbose:
        print(crabs)

    while not all(crabs == avg):
        target = int(avg.round())
        hi = crabs > target
        lo = crabs < target

        fuelhi = np.where(hi, fuel + 1, fuel)
        fuello = np.where(lo, fuel + 1, fuel)
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
            print(crabs, target, avg, fuel, fuel.sum())

    return fuel.sum()


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

