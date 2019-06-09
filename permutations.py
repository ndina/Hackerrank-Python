from itertools import permutations

s, n = input().split()
n = int(n)
for i in permutations(sorted(s), n):
    print(''.join(i))