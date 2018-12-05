#!/bin/python3

def binary_search(arr, item):
	low = 0
	high = len(arr) - 1
	
	while (low <= high):
		mid = (low + high) // 2
		if arr[mid] < item:
			low = mid + 1
		elif arr[mid] < item:
			high = mid - 1
		else:
			return mid

	return -1


if __name__ == '__main__':

	lst = list(map(int, input().split()))
	item = int(input())

	result = binary_search(lst, item)

	print(result)