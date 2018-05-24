s1n = int(input())
s1 = set(map(int, input().split()))
s2n = int(input())
s2 = set(map(int, input().split()))

sydi = len(s1.symmetric_difference(s2))

print(sydi)