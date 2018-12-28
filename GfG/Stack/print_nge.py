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

def print_nge(arr):
	
	stack = Stack()
	ele = next = 0
	
	stack.push(arr[0])

	for idx in range(1, len(arr)):
		next = arr[idx]
		if not stack.is_empty():
			ele = stack.pop()
			while ele < next:
				print(ele, '|', next)
				if stack.is_empty():
					break
				ele = stack.pop()
			if ele > next:
				stack.push(ele)
		stack.push(next)

	while not stack.is_empty():
		ele = stack.pop()
		next = -1
		print(ele, '|', next)



if __name__ == '__main__':
	arr = [11, 13, 21, 3] 
	print_nge(arr)