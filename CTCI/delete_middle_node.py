#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

def print_nodes(node):
	while node:
		print(node.data, end=" ")
		node = node.next

def delete_middle_node(node):
	if not node or not node.next:
		return False

	next_node = node.next
	node.data = next_node.data
	node.next = next_node.next

	return True

if __name__ == '__main__':

	lst = list(map(int, input().split()))

	prev = Node(lst[0])
	head = prev
	for idx in range(1, len(lst)):
		node = Node(lst[idx])
		prev.next = node
		prev = node

	num = int(input())

	node = head
	for _ in range(num-1):
		node = node.next

	result = delete_middle_node(node)
	print(result)
	print_nodes(head)