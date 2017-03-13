from functools import reduce
import operator
sum_of_digits = sum(map(int, str(reduce(operator.mul, range(1, 101)[::-1]))))
print("sum of digits is", sum_of_digits)