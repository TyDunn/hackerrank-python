#!/bin/python3

def find_missing_number(arr):
	n = len(arr)
	total = (n) * (n+1) / 2
	arr_sum = sum(arr)
	return total - arr_sum

if __name__ == '__main__':
        
        arr = []
        n = 100
        for i in range(0, n+1):
        	arr.append(i)
        arr.remove(34)

        print(find_missing_number(arr))
        print()