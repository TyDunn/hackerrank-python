#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

def partition(node, val):
	head = node
	tail = node

	while node:
		next_node = node.next
		node.next = None
		if node.data < val:
			node.next = head
			head = node
		else:
			tail.next = node
			tail = node
		node = next_node

	tail.next = None

	return head

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

	val = int(input())

	result = partition(head, val)
	print_nodes(result)