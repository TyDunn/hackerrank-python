#!/bin/python3

class StackNode:

	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:

	def __init__(self):
		self.root = None

	def is_empty(self):
		return True if not self.root else False

	def push(self, data):
		new_node = StackNode(data)
		new_node.next = self.root
		self.root = new_node

	def pop(self):
		if self.is_empty():
			print("Stack empty!")
			return
		temp = self.root
		self.root = self.root.next
		return temp.data

	def peek(self):
		if self.is_empty():
			print("Stack empty!")
			return
		return self.root.data

	def sorted_insert(self, val):
		if self.is_empty() or val > self.peek():
			self.push(val)
			return
		temp = self.pop()
		self.sorted_insert(val)
		self.push(temp)

	def sort_stack(self):
		if not self.is_empty():
			temp = self.pop()
			self.sort_stack()
			self.sorted_insert(temp)

if __name__ == '__main__':
	stack = Stack()
	stack.push(-3)
	stack.push(14)
	stack.push(18)
	stack.push(-5)
	stack.push(30)
	stack.sort_stack()
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())