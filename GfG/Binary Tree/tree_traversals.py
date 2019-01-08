#!/bin/python3

class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def print_in_order(root):
	if root:
		print_in_order(root.left)
		print(root.val, end= " ")
		print_in_order(root.right)

def print_pre_order(root):
	if root:
		print(root.val, end= " ")
		print_pre_order(root.left)
		print_pre_order(root.right)

def print_post_order(root):
	if root:
		print_post_order(root.left)
		print_post_order(root.right)
		print(root.val, end= " ")


if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	print("In Order")
	print_in_order(root)
	print()
	print("Pre Order")
	print_pre_order(root)
	print()
	print("Post Order")
	print_post_order(root)
	print()