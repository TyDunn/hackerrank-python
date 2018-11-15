#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

def detect_loop(head):
	slow = head
	fast = head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow == fast:
			break

	if fast is None or fast.next is None:
		return None

	slow = head
	while slow != fast:
		slow = slow.next
		fast - fast.next

	return fast