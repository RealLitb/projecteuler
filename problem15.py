import operator
from functools import reduce
r = (reduce(operator.mul, (i for i in range(21, 41))) //
     reduce(operator.mul, (i for i in range(2, 21))))
print("number of ways", r)

