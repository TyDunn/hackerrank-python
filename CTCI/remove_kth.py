#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

def remove_duplicates(node, k):

	if k == 1:
		return node.next

	head = node
	prev = None

	while node and k > 1:
		prev = node
		node = node.next
		k -= 1

	if node:
		prev.next = node.next

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

	num = int(input())

	result = remove_duplicates(head, num)
	print_nodes(result)