
def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount
   return minCoins[change]

amt = 63
coinCount = [0]*(amt+1)

dpMakeChange( [1,5,10,25], amt, coinCount)

for change in range(1,amt+1):
    print("change for ", change, " is ", coinCount[change], " coins")

