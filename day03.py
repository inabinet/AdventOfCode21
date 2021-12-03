
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


# Part 1
print(calculatePowerConsumption(inputs))

# Part 2
