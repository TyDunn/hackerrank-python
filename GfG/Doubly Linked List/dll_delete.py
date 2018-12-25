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

	def delete_node(self, node):
		if not self.head or not node:
			return

		if self.head == node:
			self.head = node.next

		if node.next:
			node.next.prev = node.prev

		if node.prev:
			node.prev.next = node.next

	def print_list(self, node):
		while node:
			print(node.data, end=" ")
			node = node.next
		print()

if __name__ == '__main__':
	dll = DoublyLinkedList()
	dll.push(2)
	dll.push(4)
	dll.push(8)
	dll.push(10)
	dll.print_list(dll.head)
	dll.delete_node(dll.head)
	dll.delete_node(dll.head.next) 
	dll.delete_node(dll.head.next) 
	dll.print_list(dll.head)