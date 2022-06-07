#UNION ----
#evenNumbers = { 2,4,6,8,10}
#oddNumbers = {1,3,5,7,9}
#add to set
#evenNumbers.add(12)
#update set
#extenstion = [14,16,18,20,22]
#evenNumbers.update(extenstion)
#evenNumbers.remove(10) - will count an error
#evenNumbers.discard(10)
#evenNumbers.pop()
#evenNumbers.clear()
#oddNumbers = evenNumbers.copy()
#numbers = evenNumbers.union(oddNumbers)

#DIFFERENCE
numsOne = {1,2,3,4,5}
numsTwo = {1,2}
numDiff = numsOne.difference(numsTwo)

print(numDiff)
