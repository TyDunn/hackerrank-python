#!/bin/python3

class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def print_in_order(root):
	current = root
	stack = []
	done = 0

	while not done:
		if current:
			stack.append(current)
			current = current.left
		else:
			if len(stack) > 0:
				current = stack.pop()
				print(current.val, end= " ")
				current = current.right
			else:
				done = 1


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	print_in_order(root)
	print()