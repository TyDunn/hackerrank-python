#!/bin/python3

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

    def peek(self):
        return self.items[-1]

    def print(self):
        for item in self.items:
            print(item, end=' ')
        print()

def sort(stack):
	new_stack = Stack()
	while not stack.empty():
		temp = stack.pop()
		while not new_stack.empty() and new_stack.peek() > temp:
			stack.push(new_stack.pop())
		new_stack.push(temp)
	while not new_stack.empty():
		stack.push(new_stack.pop())
	return stack

if __name__ == '__main__':
	stack = Stack()
	stack.push(5)
	stack.push(7)
	stack.push(3)
	stack.push(2)
	stack.push(4)
	stack.print()
	sorted_stack = sort(stack)
	stack.print()