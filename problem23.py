from itertools import takewhile, product, cycle, starmap, islice
from functools import reduce
import operator

def extend_primes(primes, limit):
    for i in range(primes[-1] + 2, limit, 2):
        for p in takewhile(lambda p: p * p <= i, primes):
            if i % p == 0:
                break
        else:
            primes.append(i)

# this and d's definition is the same as in problem21.py
def prime_factorize(n, primes):
    ps = {}
    for p in primes:
        if n % p == 0:
            ps[p] = 1
            n //= p
            while n % p == 0:
                ps[p] += 1
                n //= p
        if n == 1:
            break
    if n != 1:
        len_primes = len(primes)
        extend_primes(primes, n + 1)
        ps.update(prime_factorize(n, islice(primes, len_primes, None)))
    return ps

def d(a, primes):
    factorization = prime_factorize(a, primes)
    exp_cartesian = product(*map(lambda p: range(p+1), factorization.values()))
    divisors=set()
    for bases, exps in zip(cycle([factorization.keys()]), exp_cartesian):
        divisors.add(reduce(operator.mul, starmap(pow, zip(bases, exps)), 1))
    divisors.remove(a)
    return sum(divisors)

def is_abundant(a, cached_primes):
    return d(a, cached_primes) > a

def is_abundant_composable(a, abundant_numbers):
    for b in abundant_numbers:
        m = a - b
        if m in abundant_numbers:
            return True
    return False

cached_primes = [2, 3]
abundant_numbers = set()
sum_uncomposable_numbers = 0

for a in range(1, 28124):
    if not is_abundant_composable(a, abundant_numbers):
        sum_uncomposable_numbers += a
    if is_abundant(a, cached_primes):
        abundant_numbers.add(a)

print ("sum of uncomposables", sum_uncomposable_numbers)

