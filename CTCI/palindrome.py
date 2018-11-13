#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

def reverse_and_clone(node):
	head = None
	while node:
		new_node = Node(node.data)
		new_node.next = head
		head = new_node
		node = node.next
	return head

def is_equal(one, two):
	while one and two:
		if one.data != two.data:
			return False
		one = one.next
		two = two.next
	return one is None and two is None

def is_palindrome(head):
	reverse = reverse_and_clone(head)
	return is_equal(head, reverse)

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

	head = create_list()

	result = is_palindrome(head)

	print(result)