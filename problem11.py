from itertools import islice
from functools import reduce
import operator

lines = [list(map(int, line.split())) for line in open("input11.txt").readlines()]

def ngrams(seq, n):
    return zip(*[islice(seq, i, None) for i in range(n)])

w = len(lines[0])
h = len(lines)
prodlen = 4

# horizontal
hmax = max(
    reduce(operator.mul, ngram)
        for line in lines
        for ngram in ngrams(line, prodlen))

# vertical
vmax = max(
    reduce(operator.mul, ngram)
        for x in range(w)
        for ngram in ngrams(
            (lines[y][x] for y in range(h)), prodlen))

# diagonal \
dnmax = max(
    reduce(operator.mul, ngram)
        for y in range(h-prodlen)
        for ngram in zip(
            *[islice(lines[y+i], i, None) for i in range(prodlen)]))

# diagonal /
dpmax = max(
    reduce(operator.mul, ngram)
        for y in range(prodlen, h)
        for ngram in zip(
            *[islice(lines[y-i], i, None) for i in range(prodlen)]))

print("max product is", max(hmax, vmax, dnmax, dpmax))
