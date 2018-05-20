s1n = int(input())
s1 = set(map(int, input().split()))
s2n = int(input())
s2 = set(map(int, input().split()))

union = len(s1.union(s2))

print(union)