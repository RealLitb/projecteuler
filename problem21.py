from itertools import takewhile, product, cycle, starmap, islice
from functools import reduce
import operator

# "primes" shall be a list of cached primes, shared by all calls
def prime_factorize(n, primes):
    ps = {}
    for p in primes:
        if n % p == 0:
            ps[p] = 1
            n //= p
            while n % p == 0:
                ps[p] += 1
                n //= p

    if n != 1:
        len_primes = len(primes)
        for i in range(primes[-1], n + 1, 2):
            for p in takewhile(lambda p: p * p <= i, primes):
                if i % p == 0:
                    break
            else:
                primes.append(i)
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

cached_primes = [2, 3]
sum_amicable = 0
for a in range(2, 10000):
    b = d(a, cached_primes)
    if b != a and d(b, cached_primes) == a:
        sum_amicable += a

print("sum amicables", sum_amicable)
