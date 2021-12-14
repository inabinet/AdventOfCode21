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
            rules[pair] = insertion
    return template, rules


def step(template, rules):
    n = len(template)
    out = ''
    for i in range(n-1):
        pair = template[i:i+2]
        if pair in rules:
            insertion = pair[0] + rules[pair]# + pair[1]
            out += insertion
        else:
            out += pair[0]
    out += template[-1]
    return out


def getCharCount(chain):
    chars = set(chain)
    countDict = {chain.count(c):c for c in chars}
    return countDict



def part1(template, rules):
    chain = template
    for _ in range(10):
        chain = step(chain, rules)
    countDict = getCharCount(chain)
    counts = sorted(list(countDict.keys()), reverse=True)
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
print(part1(template, rules))



# Part 1
template, rules = processInputs(inputs)
print(part1(template, rules))


# Part 2

