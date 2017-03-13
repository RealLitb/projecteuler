import re

num = 2*10**2000
cycle = re.compile(r"([0-9]+?)\1+")
longest_cycle_d, longest_cycle_length = 0, 0
for d in range(2, 1001):
    digs = str(num // d)
    matched_cycle = cycle.match(digs)
    if matched_cycle is not None:
        cycle_length = len(matched_cycle.group(1))
        if cycle_length > longest_cycle_length:
            longest_cycle_d, longest_cycle_length = d, cycle_length

print("d is", longest_cycle_d, "with cycle length", longest_cycle_length)
