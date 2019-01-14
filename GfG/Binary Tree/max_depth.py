#!/bin/python3

class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def max_depth(node):
	if not node:
		return 0
	else:
		l_depth = max_depth(node.left)
		r_depth = max_depth(node.right)

		if l_depth > r_depth:
			return l_depth + 1
		else:
			return r_depth + 1

if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	root.right.left.left = Node(8)
	print(max_depth(root))