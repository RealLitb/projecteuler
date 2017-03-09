lines = list(map(int, (line.replace("\n", "") for line in open("input13.txt").readlines())))

print ("sum is", sum(lines))
print ("first ten digits", str(sum(lines))[:10])

