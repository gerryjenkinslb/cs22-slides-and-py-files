# Solution 2 - sort and compare
def anagramSolution2(s1,s2):
    n = len(s1) # 1
    if n != len(s2): return False

    list1 = list(s1)
    list2 = list(s2)

    list1.sort() # n log n
    list2.sort()

    for i in range(n): # n
        if list1[i] != list2[i]:
            return False
    return True


# example of testing
test_cases = ( ('abc','abc',True),
          ('earth','heart',True),
          ("abc","",False),
          ("","",True),
          ("","abc",False),
          ("abc","a",False),
          ("a","abc",False),
          ("aaa","a",False),
          ("a","aaa",False),
          ("apple","leppa",True))

for s1,s2,e in test_cases:
    assert anagramSolution2(s1,s2)==e,"'%s' '%s' returned %s"%(s1,s2,str(anagramSolution1(s1,s2)))
