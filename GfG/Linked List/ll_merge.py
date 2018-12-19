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

def merge_sorted(lla, llb):
	ll = LinkedList()

	curr_lla = lla.head
	curr_llb = llb.head

	while curr_lla and curr_llb:
		if curr_lla.data < curr_llb.data:
			ll.append(curr_lla.data)
			curr_lla = curr_lla.next
		else:
			ll.append(curr_llb.data)
			curr_llb = curr_llb.next

	while curr_lla:
		ll.append(curr_lla.data)
		curr_lla = curr_lla.next

	while curr_llb:
		ll.append(curr_llb.data)
		curr_llb = curr_llb.next

	return ll

if __name__ == '__main__':
	
	lla = LinkedList()
	lla.push(8)
	lla.push(7)
	lla.push(5)
	lla.push(3)
	lla.push(1)

	llb = LinkedList()
	llb.push(9)
	llb.push(6)
	llb.push(4)
	llb.push(2)

	ll = merge_sorted(lla, llb)

	ll.print_list()