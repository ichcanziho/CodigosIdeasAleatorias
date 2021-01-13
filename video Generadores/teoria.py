
cosita = 10+7


#for i in range(19):

x = range
print(x) # x NO es una instancia de map NO hace falta poner type
#for atr in dir(x):
#    print(atr)

import sys

x = range(10000000000000)
print(sys.getsizeof(x))

#map()
#zip()
#open()
#range()

x = map
print(x) # x NO es una instancia de map NO hace falta poner type
#for atr in dir(x):
#    print(atr)

x = map(lambda x: x * 2, [1, 2, 3, 4, 5])
#x = range(10)
print(x)
print(type(x))
#print(x[1])
print(next(x))
print(next(x))