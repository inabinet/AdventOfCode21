import numpy as np

with open('inputs/day11','r') as f:
    inputs = [i.strip() for i in f]


def part1(inputList):
    octopuses = np.array([np.array([int(p) for p in row]) for row in inputList])
    flashes = 0
    for i in range(100):
        octopuses, n = step(octopuses)
        flashes += n
    return flashes


def step(octopuses):
    # add 1 to all
    octopuses += 1

    flashed = []
    flashing = octopuses > 9
    while np.any(flashing):
        # get indexes of octopuses that flashed
        idxs = np.where(flashing)
        pairs = np.argwhere(flashing)
        # set those octopuses to 0
        octopuses[idxs] = 0
        # add the flashed octopuses to flashed (they will not absorb any more energy)
        flashed.extend(pairs)

        neighbors = np.pad(flashing, 1, constant_values=False).astype(int)
        neighbors += np.pad(flashing, ((1, 1), (0, 2)))  # left
        neighbors += np.pad(flashing, ((1, 1), (2, 0)))  # right
        neighbors += np.pad(flashing, ((0, 2), (1, 1)))  # up
        neighbors += np.pad(flashing, ((2, 0), (1, 1)))  # down
        neighbors += np.pad(flashing, ((0, 2), (0, 2)))  # left-up
        neighbors += np.pad(flashing, ((0, 2), (2, 0)))  # right-up
        neighbors += np.pad(flashing, ((2, 0), (0, 2)))  # left-down
        neighbors += np.pad(flashing, ((2, 0), (2, 0)))  # right-down
        neighbors = neighbors[1:-1, 1:-1]  # remove padding
        neighbors[tuple(zip(*flashed))] = 0  # remove already flashed

        # add energy to all neighbor octopuses (not already flashed)
        octopuses = np.add(octopuses, neighbors)

        # check if any new octopuses are flashing from added energy
        flashing = (octopuses > 9)

    return octopuses, len(flashed)



# Example
tmp = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

exampleInputs = [i.strip() for i in tmp.split('\n')]


print(part1(exampleInputs))



# Part 1
print(part1(inputs))


# Part 2

