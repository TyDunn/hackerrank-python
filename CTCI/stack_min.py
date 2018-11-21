#!/bin/python3

import sys

class Stack:
    
    def __init__(self):
    	self.items = []
    	self.min_stack = []

    def push(self, item):
    	if item <= self.min():
    		self.min_stack.append(item)
    	self.items.append(item)

    def pop(self):
    	val = self.items.pop()
    	if val == self.min():
    		self.min_stack.pop()
    	return val

    def min(self):
    	if not self.min_stack:
    		return sys.maxsize
    	else:
    		return self.min_stack[-1]

if __name__ == '__main__':
	stack = Stack()
	stack.push(2)
	stack.push(3)
	stack.push(2)
	stack.push(1)
	stack.push(4)
	stack.push(0)
	stack.push(6)
	stack.push(2)
	print(stack.min())
	stack.pop()
	print(stack.min())
	stack.pop()
	print(stack.min())
	stack.pop()
	print(stack.min())
	stack.pop()
	print(stack.min())
	stack.pop()
	print(stack.min())
	stack.pop()
	print(stack.min())
	stack.pop()
	print(stack.min())
	stack.pop()