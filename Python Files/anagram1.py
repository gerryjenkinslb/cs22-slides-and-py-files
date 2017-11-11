# Solution -Checking Off

def anagramSolution1(s1,s2):
    if len(s1) != len(s2): return False # quick test if fail

    n = len(s1) # 1 countdown checkoffs
    s2_list = list(s2)     # 1 convert to list

    for c1 in s1:          # n
        for i in range(len(s2_list)): # n squared
            if c1 == s2_list[i]:      # n squared
                s2_list[i] = None # (0 to n squared) check off
                n -= 1 # n squared - remove from count
                break # found c1, just to next one

    return n == 0 # found all needed matches

# 2 +  n + n^2 + n^2 =  2n^2 + n + 2 = O(n^2)

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
    assert anagramSolution1(s1,s2)==e,"'%s' '%s' returned %s"%(s1,s2,str(anagramSolution1(s1,s2)))
