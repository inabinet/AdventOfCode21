import numpy as np

with open('inputs/day08','r') as f:
    inputs = [i.strip() for i in f]


def process(inputList):
    tmp = [i.split(' | ') for i in inputList]
    signal_patterns, output_values = zip(*tmp)

    signal_patterns = [[convert(patt) for patt in row.split(' ')] for row in signal_patterns]
    output_values = [[convert(val) for val in row.split(' ')] for row in output_values]

    #print(signal_patterns)
    #print(output_values)
    return signal_patterns, output_values


def convert(signal):
    # convert letter into binary bit position
    val = lambda c: 1<<(ord(c)-97)
    return sum([val(c) for c in signal])


def part1(inputList):
    _, output_values = process(inputList)

    flatten = [bin(v) for row in output_values for v in row]

    return sum([int( (b.count('1') in (2,3,4,7)) ) for b in flatten])


def part2(inputList):
    signal_patterns, output_values = process(inputList)
    output = []

    for i, patts in enumerate(signal_patterns):
        binpatts = [bin(p) for p in patts]
        cntones = [b.count('1') for b in binpatts]

        # get known values
        one = patts[cntones.index(2)]
        seven = patts[cntones.index(3)]
        four = patts[cntones.index(4)]
        eight = 0b111_1111

        # find 'a' (bit 0) by comparing 1 to 7
        a = seven - one
        #mask = seven - one
        #a = np.log2(mask)
        #print(a)

        # get 5 segment options (2, 3, 5)
        idxs = [cntones.index(5)]
        idxs.append(cntones.index(5, idxs[-1]+1))
        idxs.append(cntones.index(5, idxs[-1]+1))
        opts = [patts[i] for i in idxs]

        # find 3 by using one as mask
        mask = ~one & eight
        three = None
        for opt in opts:
            if opt | mask == eight:
                three = opt
        opts.remove(three)

        # find bd with one mask
        bd = (four & mask)

        # find be
        mask = ~three & eight
        be = 0
        for opt in opts:
            be |= (opt & mask)

        # find b
        #b = np.log2(bd & be)
        b = bd & be

        # find five (using b loc)
        mask = ~b & eight
        five = None
        for opt in opts:
            if opt | mask == eight:
                five = opt
        opts.remove(five)

        # find two (only option left)
        two = opts[0]

        # find d and e (knowing b)
        d = bd - b
        e = be - b

        # find nine by combining five and one
        nine = five | one

        # find six by combining five and e
        six = five | e

        # find zero from process of elimination
        idxs = [cntones.index(6)]
        idxs.append(cntones.index(6, idxs[-1] + 1))
        idxs.append(cntones.index(6, idxs[-1] + 1))
        opts = [patts[i] for i in idxs]
        opts.remove(nine)
        opts.remove(six)
        zero = opts[0]

        cypher = {zero: 0, one: 1,
                  two: 2, three: 3,
                  four: 4, five: 5,
                  six: 6, seven: 7,
                  eight: 8, nine: 9}

        out = 0
        for place,v in enumerate(reversed(output_values[i])):
            out += cypher[v] * 10**place

        output.append(out)

    return sum(output)



# Example
tmp = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

exampleInputs = [i.strip() for i in tmp.split('\n')]
example1 = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']

print(part1(exampleInputs))

print(part2(example1))
print(part2(exampleInputs))


# Part 1
print(part1(inputs))


# Part 2
print(part2(inputs))
