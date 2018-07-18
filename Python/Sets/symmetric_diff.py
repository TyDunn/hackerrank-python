a, b = (int(input()), set(input().split()))
c, d = (int(input()), set(input().split()))

p = d.difference(b)
q = b.difference(d)
r = p.union(q)

print ('\n'.join(sorted(r, key=int)))