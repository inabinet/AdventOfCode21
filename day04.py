import numpy as np

with open('inputs/day04','r') as f:
    inputs = [i.strip() for i in f]


def splitInput(inputList):
    drawnNumbers = list(eval(inputList[0]))
    boards = []
    tmpboard = []
    for row in inputList[2:]:
        if row == '':
            boards.append(np.array(tmpboard))
            tmpboard = []
        else:
            tmpboard.append([int(i) for i in row.split(' ') if i])
    boards.append(np.array(tmpboard))

    return drawnNumbers, boards


def part1(drawnNumbers, boards):
    finalBoard = None
    finalNumber = None
    while drawnNumbers:
        bingo = set(drawnNumbers).issuperset
        remove = []
        for idx, board in enumerate(boards):
            bCol = np.apply_along_axis(bingo, 0, board)
            bRow = np.apply_along_axis(bingo, 1, board)
            if not (any(bCol) or any(bRow)):
                remove.append(idx)
        for idx in sorted(remove, reverse=True):
            # boards.remove(board)    # need to debug...
            boards.pop(idx)
        if len(boards) == 1:
            finalBoard = boards[0]
            finalNumber = drawnNumbers.pop()
        elif len(boards) == 0:
            break
        else:
            drawnNumbers.pop()

    drawnNumbers.append(finalNumber)
    flat = finalBoard.flatten()
    unmarked = [i for i in flat if i not in drawnNumbers]
    return sum(unmarked) * finalNumber


def part2(drawnNumbers, boards):
    # reuse of part one, but just return first board that doesn't win instead of removing and continuing
    finalBoard = None
    finalNumber = None
    while drawnNumbers:
        bingo = set(drawnNumbers).issuperset
        for idx, board in enumerate(boards):
            bCol = np.apply_along_axis(bingo, 0, board)
            bRow = np.apply_along_axis(bingo, 1, board)
            if not (any(bCol) or any(bRow)):
                finalBoard = board
        if finalBoard is not None:
            break
        else:
            finalNumber = drawnNumbers.pop()

    drawnNumbers.append(finalNumber)
    flat = finalBoard.flatten()
    unmarked = [i for i in flat if i not in drawnNumbers]
    return sum(unmarked) * finalNumber


# Example
tmp = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

exampleInputs = [i.strip() for i in tmp.split('\n')]


drawnNumbers, boards = splitInput(exampleInputs)
print(part1(drawnNumbers,boards))
drawnNumbers, boards = splitInput(exampleInputs)
print(part2(drawnNumbers,boards))


# Part 1
drawnNumbers, boards = splitInput(inputs)
print(part1(drawnNumbers,boards))

# Part 2
drawnNumbers, boards = splitInput(inputs)
print(part2(drawnNumbers,boards))
