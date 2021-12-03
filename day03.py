
with open('inputs/day03','r') as f:
    inputs = [i.strip() for i in f]


def calculatePowerConsumption(report):
    rowCnt = len(report)
    cmdCnt = len(report[0])
    mask = (2 ** cmdCnt) - 1
    gamma = 0
    for pos in range(cmdCnt):
        cnt = sum([int(code[pos]) for code in report])
        gamma ^= (int(cnt > rowCnt / 2) << (cmdCnt - pos - 1))
    epsilon = gamma ^ mask
    powerComp = gamma * epsilon
    return powerComp, gamma, epsilon


def filterList(values, pos=0, mostCommon=True):
    zeros = []
    ones = []
    for row in values:
        if int(row[pos]):
            ones.append(row)
        else:
            zeros.append(row)

    out = None
    if mostCommon:
        if len(zeros) > len(ones):
            out = zeros
        else:
            out = ones
    else:
        if len(ones) < len(zeros):
            out = ones
        else:
            out = zeros

    if len(out) == 1:
        return out[0]
    else:
        cmdCnt = len(values[0])
        pos += 1
        pos %= cmdCnt
        return filterList(out, pos=pos, mostCommon=mostCommon)


def calculateLifeSupportRating(report):
    oxgen = filterList(report, mostCommon=True)
    oxgen = int(oxgen, 2)
    co2scrub = filterList(report, mostCommon=False)
    co2scrub = int(co2scrub, 2)
    lifeRate = oxgen * co2scrub
    return lifeRate, oxgen, co2scrub



# Example
tmp = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

print(calculatePowerConsumption(exampleInputs))
print(calculateLifeSupportRating(exampleInputs))


# Part 1
print(calculatePowerConsumption(inputs))

# Part 2
print(calculateLifeSupportRating(inputs))
