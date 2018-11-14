#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

def get_tail_and_size(head):
	if not head:
		return None

	size = 1
	while head.next:
		head = head.next
		size += 1

	return { 'node': head, 'size': size }

def intersect(one, two):
	if not one or not two:
		return None

	tail_one = get_tail_and_size(one)
	tail_two = get_tail_and_size(two)

	if tail_one['node'] != tail_two['node']:
		return None

	short_lst = one
	long_lst = two
	if tail_one['size'] > tail_two['size']:
		short_lst = two
		long_lst = one

	diff = abs(tail_one['size'] - tail_two['size'])

	for _ in range(diff):
		long_lst = long_lst.next

	while short_lst != long_lst:
		short_lst = short_lst.next
		long_lst = long_lst.next

	return long_lst

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

	result = intersect(lst1, lst2)

	print(result)