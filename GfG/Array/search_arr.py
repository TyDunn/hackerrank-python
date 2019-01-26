#!/bin/python3

def find_element(arr, key):
	for idx in range(len(arr)):
		if arr[idx] == key:
			return idx
	return -1

if __name__ == '__main__':
	arr = [12, 34, 10, 6, 40]
	key = 40
	index = find_element(arr, key)
	print(index)