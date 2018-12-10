#!/bin/python3

def insertion_sort(arr):
	for i in range(1, len(arr)):
		ele = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > ele:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = ele
	return arr

if __name__ == '__main__':

	lst = list(map(int, input().split()))

	result = insertion_sort(lst)

	print(result)