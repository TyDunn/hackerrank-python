#!/bin/python3

def get_avg(x, n, total):
	total = total + x
	return total / n

def stream_avg(arr, n):
	avg = 0
	total = 0
	for i in range(n):
		avg = get_avg(arr[i], i + 1, total)
		total = avg * (i + 1)
		print('Avg of {} numbers is {}'.format(i+1, avg))

if __name__ == '__main__':
	arr = [10, 20, 30, 40, 50, 60]
	n = len(arr)
	stream_avg(arr, n)