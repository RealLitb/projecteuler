import itertools

primes=[2]
for i in range(3, 2000000):
    for p in itertools.takewhile((lambda p: p*p <= i), primes):
        if i % p == 0:
            break
    else:
        primes.append(i)
    i += 2
print("sum of primes < 2000000", sum(primes))
