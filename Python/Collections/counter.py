from collections import Counter

numShoes = int(input())
shoes = Counter(list(map(int, input().split())))
numCust = int(input())

total = 0

for _ in range(numCust):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        shoes[size] -= 1
        total += price

print(total)