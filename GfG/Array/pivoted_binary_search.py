#!/bin/python3

def pivoted_binary_search(arr, n, key):

	pivot = find_pivot(arr, 0, n-1)

	if pivot == -1:
		return binary_search(arr, 0, n-1, key)

	if arr[pivot] == key:
		return pivot
	if arr[0] <= key:
		return binary_search(arr, 0, pivot-1, key)
	return binary_search(arr, pivot+1, n-1, key)

def find_pivot(arr, low, high):
	if high < low:
		return -1
	if high == low:
		return low

	mid = (low + high) // 2

	if mid < high and arr[mid] > arr[mid + 1]:
		return mid
	if mid > low and arr[mid] < arr[mid - 1]:
		return mid - 1
	if arr[low] >= arr[mid]:
		return find_pivot(arr, low, mid - 1)
	return find_pivot(arr, mid + 1, high)

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
	arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
	x = 5
	arr = arr[-x:] + arr[:-x]
	key = 7
	index = pivoted_binary_search(arr, len(arr), key)
	print('Element: {}'.format(arr[index]))
	print('Index: {}'.format(index))