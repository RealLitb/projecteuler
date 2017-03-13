names = open("input22.txt").read().split(",")
names.sort()

scores = 0
for index, name in enumerate(names, start=1):
    scores += index * sum(map(lambda c: ord(c)-ord('A')+1, name))
print("total score", scores)