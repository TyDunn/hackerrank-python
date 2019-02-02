#!/bin/python3

def get_odd_occurence(arr):
	res = 0
	for ele in arr:
		res = res ^ ele
	return res

if __name__ == '__main__':
	arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
	print(get_odd_occurence(arr))