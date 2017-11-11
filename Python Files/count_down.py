# simple recursions

def count_down(n):  # print n, n-1, n-2, ... , 3, 2, 1
    print(n, end=" ")
    if n > 1:       # check for end case
        count_down(n-1) # do smaller problem

print("-"*5, "count down from 10")
count_down(10)
print()

print("-"*5, "count down from 5")
count_down(5)
print()
