#!/bin/python3

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

class Queue:

	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def enqueue(self, val):
		while not self.s1.is_empty():
			self.s2.push(self.s1.pop())

		self.s1.push(val)

		while not self.s2.is_empty():
			self.s1.push(self.s2.pop())

	def dequeue(self):
		if self.s1.is_empty():
			print("queue is empty")
			return
		return self.s1.pop()

if __name__ == '__main__':
	queue = Queue()
	queue.enqueue(1)
	queue.enqueue(2)
	queue.enqueue(3)
	print(queue.dequeue())
	print(queue.dequeue())
	print(queue.dequeue())