import time
cache = [None]*65 # book passes cache as parameter in recDC

def recDC(coinValueList,change):  #,knownResults):
   minCoins = change
   if change in coinValueList:
      cache[change] = 1
      return 1
   elif cache[change] != None:
      return cache[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i)
         if numCoins < minCoins:
            minCoins = numCoins
            cache[change] = minCoins
   return minCoins

start = time.time()
print(recDC([1, 5, 10, 25], 63))
total_time = time.time() - start
print("total Time %.1f secs" % (total_time) )


