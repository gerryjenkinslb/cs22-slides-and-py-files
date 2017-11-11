from timeit import Timer


def build_list(n):
    return list(range(n)) # create list of 1 to n


def access(l): # do access at 0 n//2 and n-1
    l[0]     # we do three access to get a little more of the actual time and
    l[n//2]  # get average of times at different places in list
    l[n-1]

n = 100
t1 = Timer("access(l1)",      # side note, don't need timeit. prefix
           "from __main__ import access,build_list,n; l1 = build_list(n)" )

times = t1.repeat(25,1)

secs = [ x/3 for x in times]
for t in secs:
    print("%.10f secs" % (t))

print("best time %.8f" % (min(secs)))




