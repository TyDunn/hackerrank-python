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

	def length(self):
		count = 0
		current = self.head
		while current:
			current = current.next
			count += 1
		return count

	def swap_nodes(self, x, y):

		if x == y:
			return

		prevX = None
		currX = self.head
		while currX and currX.data != x:
			prevX = currX
			currX = currX.next

		prevY = None
		currY = self.head
		while currY and currY.data != y:
			prevY = currY
			currY = currY.next

		if not currY or not currX:
			return

		if prevX:
			prevX.next = currY
		else:
			self.head = currY

		if prevY:
			prevY.next = currX
		else:
			self.head = currX

		temp = currX.next
		currX.next = currY.next
		currY.next = temp

	def reverse(self):
		prev_node = None
		curr_node = self.head
		while curr_node:
			next_node = curr_node.next
			curr_node.next = prev_node
			prev_node = curr_node
			curr_node = next_node

		self.head = prev_node

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next
		print()

if __name__ == '__main__':
	llist = LinkedList()
	llist.push(20)
	llist.push(4) 
	llist.push(15) 
	llist.push(85)
	print("Given Linked List:", end=" ")
	llist.print_list()
	llist.reverse() 
	print("Reversed Linked List:", end=" ")
	llist.print_list()