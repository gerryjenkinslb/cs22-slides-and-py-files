
data = [2, 3, 5, 12, 26, 33, 43, 91, 98]

def binarySearch( alist, item ):
    first = 0
    last = len(alist)-1
    while first <= last:
        mid = (first+last)//2 # int divide
        if alist[mid] == item: # found!
            return True
        else:
            if item < alist[mid]:
                last = mid-1
            else:
                first = mid+1
    return False

print("search for 91", binarySearch(data,91))
print("search for 92", binarySearch(data,92))

assert( binarySearch(data,91) == True)
assert( binarySearch(data,2) == True)
assert( binarySearch(data,99) == False)
