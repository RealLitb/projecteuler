from functools import reduce
from itertools import islice

def ngrams(seq, n):
    return zip(*[islice(seq, i, None) for i in range(n)])

def combine(greatest, nextinput):
    return [nextinput[i] + max(left, right) for i, (left, right) in enumerate(ngrams(greatest, 2))]

def solve_triangle(triangle_reversed):
     return reduce(combine, triangle_reversed)[0]

numbers = [list(map(int, line.replace("\n", "").split())) for line in open("input18.txt").readlines()]
numbers.reverse()
print("maximum total", solve_triangle(numbers))
