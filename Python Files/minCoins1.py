import time
def minChange(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + minChange(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

start = time.time()
print(minChange([1,5,10,25],61)) # WARNING: this takes a long time, wait for it.
total_time = time.time() - start
print("total Time %.1f secs" % (total_time) )
