s1n = int(input())
s1 = set(map(int, input().split()))
s2n = int(input())
s2 = set(map(int, input().split()))

diff = len(s1.difference(s2))

print(diff)