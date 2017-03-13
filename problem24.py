from itertools import permutations, islice
print("millionth permutation",
      "".join(list(islice(permutations("0123456789"), 999999, 1000000))[0]))
