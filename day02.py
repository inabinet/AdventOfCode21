import numpy as np

with open('inputs/day02','r') as f:
    inputs = [i for i in f]

dirDict = {
    'forward': 1,
    'up': -1j,
    'down': 1j,
}

# Example
tmp = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2"""

exampleInputs = [i.strip() for i in tmp.split('\n')]
pos = 0+0j
for cmd in exampleInputs:
    dir, amt = cmd.split(' ')
    pos += dirDict[dir] * int(amt)

ans = int(pos.real*pos.imag)
print(ans)

pos = 0+0j
aim = 0
for cmd in exampleInputs:
    dir, amt = cmd.split(' ')
    if dir == 'forward':
        pos += complex(int(amt), aim * int(amt))
    else:
        aim += dirDict[dir].imag * int(amt)

ans = int(pos.real*pos.imag)
print(ans)


# Part 1
pos = 0+0j
for cmd in inputs:
    dir, amt = cmd.split(' ')
    pos += dirDict[dir] * int(amt)

ans = int(pos.real*pos.imag)
print(ans)


# Part 2
pos = 0+0j
aim = 0
for cmd in inputs:
    dir, amt = cmd.split(' ')
    if dir == 'forward':
        pos += complex(int(amt), aim * int(amt))
    else:
        aim += dirDict[dir].imag * int(amt)

ans = int(pos.real*pos.imag)
print(ans)
