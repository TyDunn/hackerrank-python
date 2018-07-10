from itertools import combinations

num_total = int(input())
letters = input().split()
num_indicies = int(input())

all_comb = list(combinations(letters, num_indicies))
comb_with_a = [comb for comb in all_comb if 'a' in comb]

print(len(comb_with_a) / len(all_comb))