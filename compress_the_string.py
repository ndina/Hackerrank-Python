from itertools import groupby
n = input()
for i, j in groupby(n):
    print((len(list(j)), int(i)), end=' ')

#30