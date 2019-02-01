#!/bin/python3

from collections import defaultdict

def find_majority(arr):
	counts = defaultdict(lambda: 0)
	for ele in arr:
		counts[ele] += 1
	for num in counts:
		if counts[num] > len(arr) / 2:
			return num
	return None

if __name__ == '__main__':
	arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
	print(find_majority(arr))
	arr = [1, 3, 2, 3, 5, 3, 2, 3, 3]
	print(find_majority(arr))