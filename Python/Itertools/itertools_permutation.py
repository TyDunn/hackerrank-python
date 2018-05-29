from itertools import permutations

word, size = input().split()

lst = sorted(permutations(word, int(size)))

for perm in lst:
    print("".join(perm))