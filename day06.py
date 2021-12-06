
with open('inputs/day06','r') as f:
    inputs = [i.strip() for i in f]



# Example
tmp = """\
3,4,3,1,2"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

fishes = [int(f) for f in exampleInputs[0].split(',')]
#fishType = {f:0 for f in range(-2,7)}

# fish arrays
oldFish = [0 for f in range(7)]
newFish = [0 for f in range(9)]

# initial array
for fish in fishes:
    oldFish[fish] += 1

#print(0, oldFish)
#print(0, newFish)
#print()

for day in range(80):
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

    #print(oldFishSpawnDay+1,oldFish)
    #print(newFishSpawnDay+1,newFish)
    #print()
print(sum(oldFish)+sum(newFish))


# Part 1



# Part 2

