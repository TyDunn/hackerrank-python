#!/bin/python3

def quicksort(lst, left, right):
	idx = partition(lst, left, right)
	if left < idx - 1:
		quicksort(lst, left, idx - 1)
	if idx < right:
		quicksort(lst, idx, right)

def partition(lst, left , right):
	pivot = lst[(left + right) // 2]
	while left <= right:
		while lst[left] < pivot:
			left += 1
		while lst[right] > pivot:
			right -=1
		if left <= right:
			lst[left], lst[right] = lst[right], lst[left]
			left += 1
			right -= 1
	return left


if __name__ == '__main__':

	lst = list(map(int, input().split()))

	result = quicksort(lst, 0,len(lst) - 1)

	print(lst)