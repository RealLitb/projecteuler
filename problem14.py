from itertools import takewhile

def generate(x, f):
    while True:
       yield x;
       x = f(x)

collatz = (lambda n: (3 * n + 1) if (n % 2) else (n // 2))
allchains = (list(takewhile((lambda x: x > 1), generate(start, collatz)))
             for start in range(1, 1000000))
longestchain = max(allchains, key = len)

print ("longest chain start", longestchain[0], "len", len(longestchain))
