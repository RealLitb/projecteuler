from itertools import count
import math

found = False
for i in count(1):
    isquare = i*i
    remain = (1000 - i) / 2
    for j in count(i+1):
        if j > remain:
            break
        square = isquare + j*j
        sqrt = math.sqrt(square)
        if i + j + sqrt == 1000:
            print ("solution", i * j * sqrt)
            break
    if found:
        break

