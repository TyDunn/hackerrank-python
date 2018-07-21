from itertools import product

num_lst, max_val = map(int, input().split())

all_lst = (list(map(int, input().split()))[1:] for _ in range(num_lst))

results = map(lambda lst: sum(itm**2 for itm in lst) % max_val, product(*all_lst))

print(max(results))