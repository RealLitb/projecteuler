from itertools import islice
from functools import reduce
import operator

def ngrams(seq, n):
    return zip(*[islice(seq, i, None) for i in range(n)])

line = open("input8.txt").read().replace("\n", "")
product = max(reduce(operator.mul, map(int, gram)) for gram in ngrams(line, 13))
print("maximal product", product)
