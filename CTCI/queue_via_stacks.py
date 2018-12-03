#!/bin/python3

import sys

class Stack:
    
    def __init__(self):
    	self.items = []

    def empty(self):
    	return not self.items

    def push(self, item):
    	self.items.append(item)

    def pop(self):
    	val = self.items.pop()
    	return val

class Queue:

	def __init__(self):
		self.new_stack = Stack()
		self.old_stack = Stack()

	def size(self):
		return len(self.new_stack) + len(self.old_stack)

	def add(self, item):
		self.new_stack.push(item)

	def _shift_stacks(self):
		if self.old_stack.empty():
			while not self.new_stack.empty():
				self.old_stack.push(self.new_stack.pop())

	def peek(self):
		self._shift_stacks()
		return self.old_stack[-1]

	def remove(self):
		self._shift_stacks()
		return self.old_stack.pop()

if __name__ == '__main__':
	queue = Queue()
	queue.add(1)
	queue.add(2)
	queue.add(3)
	print(queue.remove())
	print(queue.remove())
	print(queue.remove())