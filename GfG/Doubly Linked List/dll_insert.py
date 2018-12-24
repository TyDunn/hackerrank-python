#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		if self.head:
			self.head.prev = new_node
		self.head = new_node

	def insert_after(self, prev_node, new_data):
		if not prev_node:
			print("The given node cannot be None.")
			return
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node
		new_node.prev = prev_node
		if new_node.next:
			new_node.next.prev = new_node

	def append(self, new_data):
		new_node = Node(new_data)
		if not self.head:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node
		new_node.prev = last

	def print_list(self, node):
		while node:
			print(node.data, end=" ")
			node = node.next
		print()

if __name__ == '__main__':
	llist = DoublyLinkedList()
	llist.append(6)
	llist.push(7)
	llist.push(1)
	llist.append(4)
	llist.insert_after(llist.head.next, 8)
	llist.print_list(llist.head)