
with open('inputs/day06','r') as f:
    inputs = [i.strip() for i in f]


def calcNumberFish(initialPopulation, nDays=80):
    # fish arrays
    oldFish = [0 for _ in range(7)]
    newFish = [0 for _ in range(9)]

    # initialalize oldFish array from initial population
    for fish in initialPopulation:
        oldFish[fish] += 1

    for day in range(nDays):
        oldFishSpawnDay = day % 7
        newFishSpawnDay = day % 9

        # find count of new fish spawned from new fish population (9-day reproduction)
        babyFishFromNew = newFish[newFishSpawnDay]

        # find count of new fish spawned from old fish population (7-day reproduction)
        babyFishFromOld = oldFish[oldFishSpawnDay]

        # these fish will now re-spawn with the old population
        oldFish[oldFishSpawnDay] += babyFishFromNew

        # these fish will now re-spawn with the new population
        newFish[newFishSpawnDay] += babyFishFromOld

    nOld = sum(oldFish)
    nNew = sum(newFish)
    total = nOld + nNew
    return(total)


# Example
tmp = """\
3,4,3,1,2"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

fishes = [int(f) for f in exampleInputs[0].split(',')]
print(calcNumberFish(fishes, nDays=80))
print(calcNumberFish(fishes, nDays=256))


# Part 1
fishes = [int(f) for f in inputs[0].split(',')]
print(calcNumberFish(fishes))


# Part 2
print(calcNumberFish(fishes, nDays=256))
