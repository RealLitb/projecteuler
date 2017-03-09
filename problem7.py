import math
from itertools import count

def isprime(n):
    if n % 2 == 0:
        return False
    for x in count(start = 3, step = 2):
        if x * x > n:
            return True
        if n % x == 0:
            return False

for i, p in enumerate(filter(isprime, count())):
    if i == 10000:
        print ("10001st prime", p)
        break
