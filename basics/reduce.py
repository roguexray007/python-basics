# The reduce() function takes three arguments:
# A function that takes two arguments
# An iterable to reduce
# An optional initial value

from functools import reduce

myList = [1,2,3,4,5]

myValue = reduce(lambda x,y: x+y, myList, 10)

print(myValue)



