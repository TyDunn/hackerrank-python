#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def create_min_bst(arr):
	return create_min_bst_help(arr, 0, len(arr)-1)

def create_min_bst_help(arr, start, end):
	if end < start:
		return None

	mid = (start + end) // 2

	node = Node(arr[mid])

	node.left = create_min_bst_help(arr, start, mid-1)
	node.right = create_min_bst_help(arr, mid+1, end)

	return node

def print_in_order(node):
	if node:
		print_in_order(node.left)
		print(node.data, end=' ')
		print_in_order(node.right)

if __name__ == '__main__':

	lst = list(map(int, input().split()))

	result = create_min_bst(lst)

	print_in_order(result)
	print()