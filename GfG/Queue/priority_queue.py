#!/bin/python3

import heapq

if __name__ == '__main__':
	lst = [5, 7, 9, 1, 3]
	
	heapq.heapify(lst)
	print(list(lst))

	heapq.heappush(lst, 4)
	print(list(lst))

	sml_ele = heapq.heappop(lst)
	print(sml_ele)