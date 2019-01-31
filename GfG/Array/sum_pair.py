#!/bin/python3

def print_pairs(arr, size, target):

	s = set()

	for i in range(0, size):
		temp = target - arr[i]
		if temp >= 0 and temp in s:
			print("Pair with sum of {} is {} and {}".format(target, arr[i], temp))
		s.add(arr[i])

if __name__ == '__main__':
	arr = [1, 4, 45, 6, 10, 8, 12, -29]
	target = 16
	print_pairs(arr, len(arr), target)