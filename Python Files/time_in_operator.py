# do a comparison of the in operator
# in a list vs a dict
# this is the best starter code to use for assignment

from timeit import Timer


def build_list(n):
    return list(range(n))  # create list of 1 to n


def build_dict(n):  # build dict = { 0:"0", 1:"1", 2:"2", ... n:"n" }
    return {i: str(i) for i in range(n)}  # from last listing in this chapter


def inx(x,n):  # do in front, middle, end, and not found
    str(0) in x
    str(n//2) in x
    str(n-1) in x
    str("a") in x  # not in x

timeList = Timer(
    "inx(x,n)",  # time this
    "from __main__ import n,build_list,inx; x = build_list(n)")  # setup

timeDict = Timer(
    "inx(x,n)",  # time this
    "from __main__ import n,build_dict,inx; x = build_dict(n)")  # setup

# print min of 5 runs of 5
print("N", "\t", "List", "\t", "Dict") # print headers
for size in range(1000, 100000+1, 5000):  # sizes to graph for n:
    n = size # copy size to __main__ module variable n
    list_secs = timeList.repeat(5,5)
    dict_sect = timeDict.repeat(5,5)
    print(n, "\t", min(list_secs), "\t", min(dict_sect))