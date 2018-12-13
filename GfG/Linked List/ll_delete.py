#!/bin/python3

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insertAfter(self, prev_node, new_data):
		if not prev_node:
			print("The given previous node must be in Linked List")
			return
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def append(self, new_data):
		new_node = Node(new_data)
		
		if self.head is None:
			self.head = new_node
			return
		
		last = self.head
		while last.next:
			last = last.next

		last.next = new_node

	def deleteNode(self, key):
		temp = self.head

		if temp:
			if temp.data == key:
				self.head = temp.next
				temp = None
				return

		while temp:
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		if not temp:
			return

		prev.next = temp.next

		temp = None

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':
	llist = LinkedList() 
	llist.push(7) 
	llist.push(1) 
	llist.push(3) 
	llist.push(2) 
	print("Created Linked List:")
	llist.print_list() 
	llist.deleteNode(1)  
	print("Linked List after Deletion of 1:")
	llist.print_list()