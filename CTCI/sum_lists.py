#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

def sum_lists(lst1, lst2, carry):

	if not lst1 and not lst2 and carry == 0:
		return None

	val = carry
	if lst1:
		val += lst1.data
	if lst2:
		val += lst2.data

	result = Node(val % 10)

	if lst1 or lst2:
		if lst1:
			lst1 = lst1.next
		if lst2:
			lst2 = lst2.next
		if val >= 10:
			val = 1
		else:
			val = 0
		more = sum_lists(lst1, lst2, val)
		result.next = more

	return result


def print_nodes(node):
	while node:
		print(node.data, end=" ")
		node = node.next

def create_list():

	lst = list(map(int, input().split()))

	prev = Node(lst[0])
	head = prev
	for idx in range(1, len(lst)):
		node = Node(lst[idx])
		prev.next = node
		prev = node

	return head

if __name__ == '__main__':

	lst1 = create_list()
	lst2 = create_list()

	result = sum_lists(lst1, lst2, 0)
	print_nodes(result)
	print()