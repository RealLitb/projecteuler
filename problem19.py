
days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def sundays(y, mod7):
    num_sundays = 0
    leap_offset = y % 4 == 0
    for d in days:
        if mod7 == 0:
            num_sundays += 1
        mod7 = (mod7 + d + (leap_offset if d == 28 else 0)) % 7
    return num_sundays, mod7

num_sundays_global = 0
mod7_global = (1 + 365) % 7

for y in range(1901, 2001):
    num_sundays, mod7_global = sundays(y, mod7_global)
    num_sundays_global += num_sundays

print ("number sundays is", num_sundays_global)
