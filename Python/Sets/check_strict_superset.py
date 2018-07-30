A = set(input().split())

result = True
for _ in range(int(input())):
    test = set(input().split())
    if not A.issuperset(test) or A == test:
        result = False

print(result)