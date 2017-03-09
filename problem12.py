from itertools import count, takewhile

def num_factors(n):
    return sum(0 if n % d != 0 else 1 if d*d == n else 2
               for d in takewhile(
                    (lambda d: d*d<=n),
                    (i for i in range(1, n//2))))

for n in ((n*(n+1))//2 for n in count(1)):
    if num_factors(n) > 500:
        print ("first with >500 factors", n)
        break