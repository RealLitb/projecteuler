from itertools import islice
from functools import reduce

def primes_eratosthenes(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, prime) in enumerate(a):
        if prime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

# prime number theorem
primes = primes_eratosthenes(10000000)
factors = [[p, 1, p*p] for p in islice(primes, 500500)]

def bubble_insertion(seq, index, key):
    item_key = key(seq[index])
    for i in range(index + 1, len(seq)):
        if key(seq[i]) >= item_key:
            break
        seq[i], seq[i-1] = seq[i-1], seq[i]

def sink_insertion(seq, index, key):
    item_key = key(seq[index])
    for i in range(index, 0, -1):
        if key(seq[i-1]) < item_key:
            break
        seq[i], seq[i-1] = seq[i-1], seq[i]

#  left: index of first prime with power 1
#  right: index of last prime with power 1
# returns: the left_right for the next call, or None if we are finished
def step(factors, left_right):
    left, right = left_right
    if factors[left][2] < factors[0][2]:
        factors[left][1] = 3
        factors[left][2] *= factors[left][2]
        sink_insertion(factors, left, lambda p: p[2])
        return (left + 1, right)
    elif factors[0][2] < factors[right][0]:
        factors[0][1] = factors[0][1] * 2 + 1
        factors[0][2] *= factors[0][2]
        bubble_insertion(factors, 0, lambda p: p[2])
        return (left, right - 1)
    return None

left_right = (0, len(factors) - 1)
while True:
    new_left_right = step(factors, left_right)
    if new_left_right is None:
        break
    left_right = new_left_right

mod = 500500507
powers = map(lambda p: pow(p[0], p[1]), factors[:(left_right[1]+1)])
print("smallest number is", reduce((lambda a, b: (a * (b % mod)) % mod), powers))
