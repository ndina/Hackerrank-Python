a, b = (int, input()), input().split()
c, d = (int, input()), input().split()
aa = set(a)
bb = set(b)
p = bb.difference(aa)
q = aa.difference(bb)
r = p.union(q)
print ('\n'.join(sorted(r, key=int)))


