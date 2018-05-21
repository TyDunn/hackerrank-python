s1n = int(input())
s1 = set(map(int, input().split()))
s2n = int(input())
s2 = set(map(int, input().split()))

itsc = len(s1.intersection(s2))

print(itsc)