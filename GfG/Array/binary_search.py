#!/bin/python3

def binary_search(arr, low, high, key):

	if high < low:
		return -1

	mid = (low + high) // 2

	if key == arr[mid]:
		return mid

	if key > arr[mid]:
		return binary_search(arr, mid + 1, high, key)

	return binary_search(arr, low, mid - 1, key)

if __name__ == '__main__':
	arr = [5, 6, 7, 8, 9, 10]
	key = 9
	index = binary_search(arr, 0, len(arr), key)
	print(index)