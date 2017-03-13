from functools import reduce
import math

index = 2
a, b = 1, 1
while len(str(b)) < 1000:
    a, b = b, a + b
    index += 1

print (index, "=", b)
