n = int(input())
s = set(map(int, input().split()))
e = int(input())

for _ in range(e):
    op = input().split()
    if (op[0] == 'pop'):
        s.pop()
    elif (op[0] == 'remove'):
        s.remove(int(op[1]))
    elif (op[0] == 'discard'):
        s.discard(int(op[1]))

sum = 0
for ele in s:
    sum += ele
print(sum)