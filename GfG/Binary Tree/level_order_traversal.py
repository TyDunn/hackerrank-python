#!/bin/python3

class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def print_level_order(root):
	ht = height(root)
	for i in range(1, ht+1):
		print_given_level(root, i)

def print_given_level(root, level):
	if not root:
		return
	if level == 1:
		print(root.val, end=" ")
	elif level > 1:
		print_given_level(root.left, level-1)
		print_given_level(root.right, level-1)

def height(node):
	if not node:
		return 0
	else:
		l_ht = height(node.left)
		r_ht = height(node.right)

		if l_ht > r_ht:
			return l_ht + 1
		else:
			return r_ht + 1

if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	print_level_order(root)
	print()