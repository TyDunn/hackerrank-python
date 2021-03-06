#!/bin/python3

def median(arr, n):
    if n % 2 == 0: 
        return (arr[n // 2] + arr[(n // 2) - 1]) / 2
    else: 
        return arr[n // 2] 

def get_median(arr1, arr2, n):

	if n == 0:
		return -1
	elif n == 1:
		return(arr[0] + arr[1]) / 2
	elif n == 2:
		return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
	else:
		m1 = median(arr1, n)
		m2 = median(arr2, n)

		if m1 > m2:
			if n % 2 == 0:
				return get_median(arr1[:(n // 2) + 1], arr2[(n // 2) - 1:], (n // 2) + 1)
			else:
				return get_median(arr1[:(n // 2) + 1], arr2[(n // 2):], (n // 2) + 1)
		else:
			if n % 2 == 0:
				return get_median(arr1[(n // 2) - 1:], arr2[:(n // 2) + 1], (n // 2) + 1)
			else:
				return get_median(arr1[(n // 2):], arr2[0:(n // 2) + 1], (n // 2) + 1)

if __name__ == '__main__':
	arr1 = [1, 2, 3, 6]
	arr2 = [4, 6, 8, 10]
	n = len(arr1)
	median = get_median(arr1, arr2, n)
	print(median)