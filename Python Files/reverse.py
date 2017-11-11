def reverse(l):
    if len(l) == 0:
        return []
    return reverse(l[1:]) + [ l[0]]

assert  reverse([1,2,3]) == [ 3,2,1]
assert  reverse(["a", "b"]) == [ "b", "a"]
assert  reverse(list(range(1,101))) == list(range(100,0,-1))