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

def lca(root, n1, n2):

	if not root:
		return None

	if root.val > n1 and root.val > n2:
		return lca(root.left, n1, n2)

	if root.val < n1 and root.val < n2:
		return lca(root.right, n1, n2)

	return root.val

if __name__ == '__main__':
	r = Node(50) 
	
	insert(r, Node(20)) 
	insert(r, Node(8)) 
	insert(r, Node(22)) 
	insert(r, Node(4)) 
	insert(r, Node(12)) 
	insert(r, Node(10))
	insert(r, Node(14))

	n1 = 10
	n2 = 14
	print(lca(r, n1, n2))