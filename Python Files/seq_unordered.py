
data = [43, 91, 3, 33, 26, 12, 2, 98, 5]
print(data)

def seqSearch( alist, item ):  # return True if item in alist
    i = 0
    while i < len(alist):
        if alist[i] == item:
            return True # direct return technique
        i += 1
    return False


assert( seqSearch(data,91) == True)
assert( seqSearch(data,2) == True)
assert( seqSearch(data,99) == False)