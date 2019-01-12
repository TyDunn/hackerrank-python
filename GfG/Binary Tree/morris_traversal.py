#!/bin/python3

class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def morris_traversal(root):
	current = root
	while current:
		if not current.left:
			print(current.val, end= " ")
			current = current.right
		else:
			pred = current.left
			while pred.right and pred.right != current:
				pred = pred.right
			if not pred.right:
				pred.right = current
				current = current.left
			else:
				pred.right = None
				print(current.val, end= " ")
				current = current.right


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	morris_traversal(root)
	print()