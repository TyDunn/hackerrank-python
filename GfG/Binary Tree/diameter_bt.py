#!/bin/python3

class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def height(node):
	if not node:
		return 0
	return 1 + max(height(node.left), height(node.right))

def diameter(root):
	if not root:
		return 0

	l_ht = height(root.left)
	r_ht = height(root.right)

	l_dr = diameter(root.left)
	r_dr = diameter(root.right)

	return max(l_ht + r_ht + 1, max(l_dr, r_dr))

if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	print(diameter(root))