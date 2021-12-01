import numpy as np

with open('inputs/day01','r') as f:
    inputs = [int(i) for i in f]


# Example
tmp = """\
199
200
208
210
200
207
240
269
260
263"""

exampleInputs = [int(i.strip()) for i in tmp.split('\n')]
d = np.diff(exampleInputs, n=1)
p = np.nonzero(d>0)[0]
print(len(p))

w = np.convolve(exampleInputs, [1,1,1])[2:-2]
d = np.diff(w, n=1)
p = np.nonzero(d>0)[0]
print(len(p))

# Part 1
d = np.diff(inputs, n=1)
p = np.nonzero(d>0)[0]
print(len(p))

# Part 2
w = np.convolve(inputs, [1,1,1])[2:-2]
d = np.diff(w, n=1)
p = np.nonzero(d>0)[0]
print(len(p))
