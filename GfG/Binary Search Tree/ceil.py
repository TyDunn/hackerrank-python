#!/bin/python3

class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def insert(root, node):
	if not root:
		root = node
	else:
		if root.val < node.val:
			if not root.right:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if not root.left:
				root.left = node
			else:
				insert(root.left, node)

def ceil(root, val):
	if not root:
		return -1

	if root.val == val:
		return root.val

	if root.val < val:
		return ceil(root.right, val)

	l_val = ceil(root.left, val)
	return l_val if l_val >= val else root.val

if __name__ == '__main__':

	root = Node(8)
	insert(root, Node(4))
	insert(root, Node(12))
	insert(root, Node(2))
	insert(root, Node(6))
	insert(root, Node(10))
	insert(root, Node(14))

	for i in range(16):
		print("{}: {}".format(i, ceil(root, i)))