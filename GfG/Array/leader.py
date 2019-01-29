#!/bin/python3

def print_leaders(arr):
	max_ele = arr[len(arr)-1]
	print(max_ele, end=" ")
	for idx in range(len(arr)-2, 0, -1):
		if max_ele < arr[idx]:
			max_ele = arr[idx]
			print(max_ele, end=" ")

if __name__ == '__main__':
        arr = [16, 17, 4, 3, 5, 2]
        print_leaders(arr)
        print()