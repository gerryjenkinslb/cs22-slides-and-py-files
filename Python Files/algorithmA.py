
import time

# cleaned up version to sum 1 + 2 + 3 up to n
def sum_of_n(n):
    start = time.time() # system time in miliseconds
    the_sum = 0              # 1 assignment to the_sum
    for i in range(1,n+1):   # n assignments to i
        the_sum += i         # n assignments to the_sum
    stop = time.time() # stop time

    return the_sum, stop-start

print("times for n = ", 100000)
for times in range(5):
    print( "Sum is %d required %10.7f seconds"%(sum_of_n(10000)))

print("\ntimes for n = 10,000, 100,000, 1,000,000, 100,000,000")
for times in [10000, 100000, 1000000, 100000000]:
    print( "Sum up to %10d required %10.7f seconds"%(times, sum_of_n(times)[1]))


