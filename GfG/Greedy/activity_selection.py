#!/bin/python3

def print_max_activities(start, finish):
	i = 0
	print(i, end=" ")
	for j in range(len(finish)):
		if start[j] >= finish[i]:
			print(j, end=" ")
			i = j
	print()

if __name__ == '__main__':
	start = [1 , 3 , 0 , 5 , 8 , 5]
	finish = [2 , 4 , 6 , 7 , 9 , 9]
	print_max_activities(start, finish)