#!/bin/python3

import random

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def print_random(self):

		if self.head is None:
			return

		random.seed()

		result = self.head.data

		current = self.head
		n = 2
		while current:
			if random.randrange(n) == 0:
				result = current.data
			current = current.next
			n += 1

		print(result)

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':
	llist = LinkedList()
	llist.push(5) 
	llist.push(20) 
	llist.push(4) 
	llist.push(3) 
	llist.push(30)
	llist.print_random()