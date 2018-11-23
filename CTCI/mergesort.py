#!/bin/python3

def mergesort(arr):
	helper = [0] * len(arr)
	mergesort_helper(arr, helper, 0, len(arr) - 1)

def mergesort_helper(arr, helper, low, high):
	if low < high:
		mid = (low + high) // 2
		mergesort_helper(arr, helper, low, mid)
		mergesort_helper(arr, helper, mid + 1, high)
		merge(arr, helper, low, mid, high)

def merge(arr, helper, low, mid, high):
	for idx in range(low, high + 1):
		helper[idx] = arr[idx]

	helper_left = low
	helper_right = mid + 1
	current = low

	while helper_left <= mid and helper_right <= high:
		if helper[helper_left] <= helper[helper_right]:
			arr[current] = helper[helper_left]
			helper_left += 1
		else:
			arr[current] = helper[helper_right]
			helper_right += 1
		current += 1

	remaining = mid - helper_left

	for idx in range(remaining + 1):
		arr[current + idx] = helper[helper_left + idx]


if __name__ == '__main__':

	lst = list(map(int, input().split()))

	result = mergesort(lst)

	print(lst)