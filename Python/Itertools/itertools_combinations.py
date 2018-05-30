from itertools import combinations

word, size = input().split()

for i in range(1, int(size)+1):
    for j in combinations(sorted(word), i):
        print(''.join(j))