
with open('inputs/day10','r') as f:
    inputs = [i.strip() for i in f]


close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def getCorruptedDict(lines):
    corrupted = {}
    for i,line in enumerate(lines):
        stack = []
        for char in line:
            if char in close.keys():    # keys are the start characters :-|
                stack.append(char)
            else:
                if len(stack) == 0:
                    print('ummm...')
                strt = stack.pop()
                if close[strt] != char:
                    corrupted[i] = char
                    break
    return corrupted


def calculateScore(lines):
    corrupted = getCorruptedDict(lines)
    vals = [points[c] for c in corrupted.values()]
    return sum(vals)



# Example
tmp = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

exampleInputs = [i.strip() for i in tmp.split('\n')]

print(calculateScore(exampleInputs))


# Part 1
print(calculateScore(inputs))


# Part 2
