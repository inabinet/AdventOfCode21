from copy import deepcopy

with open('inputs/day18','r') as f:
    inputs = [i.strip() for i in f]



class SnailfishNumber:
    def __init__(self, number):
        self.__value = None
        ncopy = deepcopy(number)
        self._value = ncopy
        self._magnitude = None

    @property
    def _value(self):
        return self.__value

    @_value.setter
    def _value(self, number):
        self.__value = number
        reduced = False
        while not reduced:
            reduced = True
            noexplode = False
            while not noexplode:
                #print(self.__value)
                noexplode = self._explode()
                reduced &= noexplode

            # split: if occurs, will re-loop to check for new reduces before more splits
            #print(self.__value)
            reduced &= self._split()

    @property
    def left(self):
        return SnailfishNumber(self._value[0])

    @property
    def right(self):
        return SnailfishNumber(self._value[1])

    @property
    def _leftVal(self):
        return self.left._value

    @property
    def _rightVal(self):
        return self.right._value

    @property
    def magnitude(self):
        if not self._magnitude:
            if isinstance(self._value, int):
                self._magnitude = self._value
            else:
                self._magnitude = 3*self.left.magnitude + 2*self.right.magnitude

        return self._magnitude

    def _explode(self, idx = None):
        if idx == None:
            idx = []
        val = self._get_val(idx)
        depth = len(idx)

        if isinstance(val, list):
            if depth == 4:  # explode
                left = val[0]
                right = val[1]
                self._add_left(idx, left)
                self._add_right(idx, right)
                self._set_val(idx, 0)  # set this pair to 0
                #complete &= False
                return False
            else:
                for lr in (0,1):
                    reduced = self._explode(idx=idx+[lr])
                    if not reduced:
                        return reduced
        return True

    def _split(self, idx = None):
        if idx == None:
            idx = []
        val = self._get_val(idx)

        if isinstance(val, list):
            for lr in (0,1):
                reduced = self._split(idx=idx+[lr])
                if not reduced:
                    return reduced

        elif val >= 10:      # split
            left = val//2
            right = (val+1)//2
            self._set_val(idx, [left,right])
            return False

        return True

    def _get_val(self, idx):    # deprecate?
        val = self._value
        for i in idx:
            val = val[i]
        return val

    def _get_val_reference(self, idx):
        # TODO: make sure this doesn't traverse too deep (even returning an int is problematic)
        ref = self.__value
        for i in idx:
            ref = ref[i]
        return ref

    def _set_val(self, idx, value):
        ref = self.__value
        for i in idx[:-1]:
            ref = ref[i]
        ref[idx[-1]] = value

    def _add_left(self, idx, value):
        self.__add_left_right(idx, value, lr=0)

    def _add_right(self, idx, value):
        self.__add_left_right(idx, value, lr=1)

    def __add_left_right(self, idx, value, lr):
        idx = self._findIndexRegularLeftRight(idx, lr)
        if idx:
            current = self._get_val(idx)
            self._set_val(idx, current+value)

    def _findIndexRegularLeftRight(self, idx, lr):
        opp = lr ^ 1    # get the opposite direction
        *parent, cur = idx
        while parent:
            #if cur == opp:
            if cur != lr:
                # current position is opposite direction from desired, so check sibling
                found = self._findFirstChildInt(parent, lr=opp, ignore=parent+[cur])
                return found
            else:
                # go up a level
                *parent, cur = parent
        # corner case
        if cur != lr:
            # current position is opposite direction from desired, so check sibling
            found = self._findFirstChildInt(parent, lr=opp, ignore=[cur])
            return found

        return None

    def _findFirstChildInt(self, idx, lr, ignore=None):
        #ref = self._get_val_reference(idx)
        ref = self._get_val(idx)

        # check children in this order
        for i in (lr, lr^1):
            if isinstance(ref[i], int):
                found = idx + [i]
                if found != ignore:
                    return found

            tmp = idx + [i]
            if tmp != ignore:
                idx = self._findFirstChildInt(tmp, lr)
                if idx:
                    return idx

        # no child found down this branch
        return None

    def __add__(self, other):
        return SnailfishNumber([self._value, other._value])

    def __repr__(self):
        return repr(self._value)

    #def __getitem__(self, item):
    #    return SnailfishNumber(self._value[item])

    def __eq__(self, other):
        return self._value == other._value




#a = SnailfishNumber([[[[[9,8],1],2],3],4])
#f = SnailfishNumber([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
#f2 = SnailfishNumber([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]])
#g = SnailfishNumber([[[[4,3],4],4],[7,[[8,4],9]]])
#h = SnailfishNumber([1,1])
#i = g+h
#k = SnailfishNumber([[9,1],[1,9]])
#kmag = k.magnitude


# Example
tmp = """\
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""


exampleInputs = [i.strip() for i in tmp.split('\n')]

#snums = [SnailfishNumber(i) for i in ([1,1],[2,2],[3,3],[4,4],[5,5],[6,6])]

snums = [SnailfishNumber(eval(i)) for i in exampleInputs]
res = snums[0]
for sn in snums[1:]:
    #print(res, sn)
    res += sn

print(res)
print(res.magnitude)


tmp = """\
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""

exampleInputs = [i.strip() for i in tmp.split('\n')]
snums = [SnailfishNumber(eval(i)) for i in exampleInputs]
res = snums[0]
for sn in snums[1:]:
    res += sn
print(res)
print(res.magnitude)


snums = [SnailfishNumber(eval(i)) for i in exampleInputs]
x = snums[0]+snums[1]

mags = []
for a in snums:
    for b in snums:
        if a!=b:
            tmpsum = a+b
            mags.append(tmpsum.magnitude)
print(max(mags))


# Part 1
snums = [SnailfishNumber(eval(i)) for i in inputs]
res = snums[0]
for sn in snums[1:]:
    res += sn
print(res)
print(res.magnitude)


# Part 2
mags = []
for a in snums:
    for b in snums:
        if a!=b:
            tmpsum = a+b
            mags.append(tmpsum.magnitude)
print(max(mags))
