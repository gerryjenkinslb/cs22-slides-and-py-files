
data = [2, 3, 5, 12, 26, 33, 43, 91, 98]

# note the data must be sorted from smallest to largest
# this is a pre-condition for binary search to work

def binarySearch( alist, item ):
    return binarySearchHelper( alist, item, 0, len(alist)-1)

def binarySearchHelper( alist, item, first, last):
    pass  # replace pass with your code here,
    # you can not slice or copy alist in any way
    # use recursion and pass a new first and last every recursive step
    # this will involve using the techniques shown in the first
    # binary search listing, but using it in a recursive solution
    # simular in structure to the second binary search listing

print("search for 91", binarySearch(data,91))
print("search for 92", binarySearch(data,92))

assert( binarySearch(data,91) == True)
assert( binarySearch(data,2) == True)
assert( binarySearch(data,99) == False)
