#!/bin/python3

class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def trav_in_order(node):
	if node:
		trav_in_order(node.left)
		print(node.val)
		trav_in_order(node.right)


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	trav_in_order(root)