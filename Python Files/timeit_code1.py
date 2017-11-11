import timeit

# create Timer object
#                   | what to time     | setup before timing runs
t1 = timeit.Timer( "print('action')", "print('setup')")

n = 5  # time how long 5 action's take
secs = t1.timeit(number=n)  # setup and then doit 5 times

print("\n%d times took %.8f Seconds " % (n, secs))

print("\n\n", "-"*20, "\n\n")


# --------------------- the repeat method:
#      do setup and then time repeat of action 2 actions,
#      do this over and over 10 times and put all times in list
times = t1.repeat(10,2)  # setup and doit twice, time 10 of these and put in list
for t in times:
    print("%.8f Seconds: "%(t))

