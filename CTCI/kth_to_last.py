#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

def kth_to_last(node, k):

	front = node

	while front and k > 0:
		front = front.next
		k -= 1

	if k == 0:
		ktolast = node
	else:
		return None

	while front and ktolast:
		front = front.next
		ktolast = ktolast.next

	return ktolast

def print_node(node):
	if node:
		print(node.data)
	else:
		print('ktolast does not exist')

if __name__ == '__main__':

	lst = list(map(int, input().split()))

	prev = Node(lst[0])
	head = prev
	for idx in range(1, len(lst)):
		node = Node(lst[idx])
		prev.next = node
		prev = node

	num = int(input())

	result = kth_to_last(head, num)
	print_node(result)