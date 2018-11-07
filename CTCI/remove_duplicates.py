#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

def remove_duplicates(node):
	nodes = set()
	start = node
	prev = None
	while node:
		if node.data in nodes:
			prev.next = node.next
		else:
			nodes.add(node.data)
			prev = node
		node = node.next
	return start

def print_nodes(node):
	while node:
		print(node.data, end=" ")
		node = node.next

if __name__ == '__main__':

	lst = list(map(int, input().split()))

	prev = Node(lst[0])
	head = prev
	for idx in range(1, len(lst)):
		node = Node(lst[idx])
		prev.next = node
		prev = node

	result = remove_duplicates(head)
	print_nodes(result)