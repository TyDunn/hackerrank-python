#!/bin/python3

def bubble_sort(arr):
	for i in range(len(arr)):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

if __name__ == '__main__':

	lst = list(map(int, input().split()))

	result = bubble_sort(lst)

	print(result)