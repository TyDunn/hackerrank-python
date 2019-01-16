#!/bin/python3

class Node:

	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def search(root, key):
	if not root or root.val == key:
		return root

	if root.val < key:
		return search(root.right, key)

	return search(root.left, key)

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

def min_value_node(node):
	current = node
	while current.left:
		current = current.left
	return current

def delete(root, key):
	if not root:
		return root

	if key < root.val:
		root.left = delete(root.left, key)
	elif key > root.val:
		root.right = delete(root.right, key)
	else:
		if not root.left:
			temp = root.right
			root = None
			return temp
		elif not root.right:
			temp = root.left
			root = None
			return temp
		else:
			temp = min_value_node(root.right)
			root.val = temp.val
			root.right = delete(root.right, temp.val)
	return root

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val, end=" ")
		inorder(root.right)

if __name__ == '__main__':
	r = Node(50) 
	
	insert(r, Node(30)) 
	insert(r, Node(20)) 
	insert(r, Node(40)) 
	insert(r, Node(70)) 
	insert(r, Node(60)) 
	insert(r, Node(80)) 

	inorder(r)
	print()

	r = delete(r, 40)

	inorder(r)
	print()