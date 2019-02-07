#!/bin/python3

def merge(arr1, arr2):
	arr1_ptr = 0
	arr2_ptr = 0

	arr = []
	while arr1_ptr < len(arr1) and arr2_ptr < len(arr2):
		if arr1[arr1_ptr] < arr2[arr2_ptr]:
			arr.append(arr1[arr1_ptr])
			arr1_ptr += 1
		else:
			arr.append(arr2[arr2_ptr])
			arr2_ptr += 1

	if arr1_ptr < len(arr1):
		for idx in range(arr1_ptr, len(arr1)):
			arr.append(arr1[arr1_ptr])

	if arr2_ptr < len(arr2):
		for idx in range(arr2_ptr, len(arr2)):
			arr.append(arr2[arr2_ptr])

	return arr


if __name__ == '__main__':
	arr1 = [2, 8, 13, 15, 20]
	arr2 = [5, 7, 9, 25]

	arr = merge(arr1, arr2)
	print(arr)