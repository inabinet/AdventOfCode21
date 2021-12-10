from numpy import median

with open('inputs/day10','r') as f:
    inputs = [i.strip() for i in f]


close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def getCorruptedAndEndingDicts(lines):
    corrupted = {}
    endings = {}
    for i,line in enumerate(lines):
        stack = []
        for char in line:
            if char in close.keys():    # keys are the start characters :-|
                stack.append(char)
            else:
                strt = stack.pop()
                if close[strt] != char:
                    corrupted[i] = char
                    break
        if i not in corrupted:
            endings[i] = [close[i] for i in reversed(stack)]
    return corrupted, endings


def calculateSyntaxErrorScore(lines):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    corrupted, _ = getCorruptedAndEndingDicts(lines)
    vals = [points[c] for c in corrupted.values()]
    return sum(vals)


def calculateAutocompleteScore(lines):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    _, endings = getCorruptedAndEndingDicts(lines)
    scores = []
    for ending in endings.values():
        score = 0
        for char in ending:
            score *= 5
            score += points[char]
        scores.append(score)
    return int(median(scores))



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

print(calculateSyntaxErrorScore(exampleInputs))
print(calculateAutocompleteScore(exampleInputs))


# Part 1
print(calculateSyntaxErrorScore(inputs))


# Part 2
print(calculateAutocompleteScore(inputs))
