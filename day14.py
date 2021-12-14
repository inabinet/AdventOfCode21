import re

with open('inputs/day14','r') as f:
    inputs = [i.strip() for i in f]



def processInputs(inputList):
    template = inputList[0]
    rules = {}
    myre = re.compile('^(\w{2}) -> (\w)$')
    for ln in inputList[2:]:
        if m := myre.match(ln):
            pair, insertion = m.groups()
            p1 = f'{pair[0]}{insertion}'
            p2 = f'{insertion}{pair[1]}'
            rules[pair] = [p1, p2]
    return template, rules


def getInitialPairsDict(template, rules):
    unique = set(rules.keys())
    unique = unique.union([pair for pairs in rules.values() for pair in pairs])
    pairDict = {pair:0 for pair in unique}

    n = len(template)
    for i in range(n-1):
        pair = template[i:i+2]
        pairDict[pair] += 1

    return pairDict


def step(pairDict, rules):
    delta = {k:0 for k in pairDict.keys()}

    # find changes
    for pair, cnt in pairDict.items():
        if cnt > 0:
            p1,p2 = rules[pair]
            delta[pair] -= cnt
            delta[p1] += cnt
            delta[p2] += cnt

    # apply changes
    out = {k:cnt+delta[k] for k,cnt in pairDict.items()}

    return out


def getCharCount(pairDict):
    chars = set((char for keys in pairDict for char in keys))
    countDict = {c:0 for c in chars}
    for pair, cnt in pairDict.items():
        char1, char2 = pair
        countDict[char1] += cnt
        countDict[char2] += cnt
    # divide by 2 needed to not double-count characters (though I don't fully understand how this works)
    countDict = {k:(v+1)//2 for k,v in countDict.items()}
    return countDict


def part1(pairDict, rules):
    for _ in range(10):
        pairDict = step(pairDict, rules)
    countDict = getCharCount(pairDict)
    counts = sorted(list(countDict.values()), reverse=True)
    return counts[0] - counts[-1]



# Example
tmp = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

template, rules = processInputs(exampleInputs)
pairDict = getInitialPairsDict(template, rules)
print(part1(pairDict, rules))



# Part 1
template, rules = processInputs(inputs)
pairDict = getInitialPairsDict(template, rules)
print(part1(pairDict, rules))


# Part 2

