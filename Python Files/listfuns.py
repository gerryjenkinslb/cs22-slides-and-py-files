def test1(): # use concatenation
    l = []
    for i in range(1000):
        l = l + [i]


def test2(): # use append
    l = []
    for i in range(1000):
        l.append(i)


def test3(): # use list comprehension of range
    l = [i for i in range(1000)]


def test4(): # convert range to list with list constructor
    l = list(range(1000))


# ---------------------------
from timeit import Timer

#          | time this  | setup prior to test (need access to this file.test1)
t1 = Timer("test1()", "from __main__ import test1")
# ^timer object

#                     | call timeit , set number of times to do it
print("concatenate", t1.timeit(number=500)/500, "seconds for one")
print("concatenate", t1.timeit(number=2000)/2000, "seconds for one")

l = t1.repeat(100,1)
print("\n", min(l))  # best time is the one we want.

