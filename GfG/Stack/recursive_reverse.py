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

def insert_at_bottom(stack, item):
	if stack.is_empty():
		stack.push(item)
	else:
		temp = stack.pop()
		insert_at_bottom(stack, item)
		stack.push(temp)

def reverse(stack):
	if not stack.is_empty():
		temp = stack.pop()
		reverse(stack)
		insert_at_bottom(stack, temp)

if __name__ == '__main__':
	stack = Stack()
	stack.push(1)
	stack.push(2)
	stack.push(3)
	stack.push(4)
	stack.push(5)
	reverse(stack)
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())