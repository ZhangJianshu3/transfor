import itertools
a = [1,2,3,4,5]

iter = itertools.combinations(a, 2)
b = list(iter)
for i in b:
    print i


