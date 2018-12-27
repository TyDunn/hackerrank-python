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

if __name__ == '__main__':
	stack = Stack()
	stack.push(10)
	stack.push(20)
	stack.push(30)
	print(stack.pop())
	print(stack.peek())