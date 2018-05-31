from itertools import combinations_with_replacement

word, size = input().split()

lst = combinations_with_replacement(sorted(word), int(size))

for comb in lst:
    print("".join(comb))