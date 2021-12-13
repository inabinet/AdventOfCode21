
with open('inputs/day12','r') as f:
    inputs = [i.strip() for i in f]


def getConnectionDict(inputList):
    connections = {}
    for ln in inputList:
        pnt1, pnt2 = ln.split('-')
        if pnt1 not in connections:
            connections[pnt1] = set()
        connections[pnt1].add(pnt2)
        if pnt2 not in connections:
            connections[pnt2] = set()
        connections[pnt2].add(pnt1)
    return connections


def walk(connections, pnt='start', path=('start',)):
    # at the end, have 1 point (valid path)
    if pnt == 'end':
        #print(path)
        return 1

    conns = connections[pnt]
    tmp = [p for p in path if p.islower()]
    conns = conns.difference(tmp)

    # no conns left (you cannot go anywhere); 0
    if not conns:
        return 0

    n = 0
    for c in conns:
        newpath = list(path)
        #if c.islower():
        newpath.append(c)
        n += walk(connections, c, newpath)

    return n


# Example 1
tmp = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

exampleInputs = [i.strip() for i in tmp.split('\n')]
conn1 = getConnectionDict(exampleInputs)

# Example 2
tmp = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

exampleInputs = [i.strip() for i in tmp.split('\n')]
conn2 = getConnectionDict(exampleInputs)

# Example 3
tmp = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

exampleInputs = [i.strip() for i in tmp.split('\n')]
conn3 = getConnectionDict(exampleInputs)


print(walk(conn1))
print(walk(conn2))
print(walk(conn3))



# Part 1
conns = getConnectionDict(inputs)
print(walk(conns))


# Part 2

