class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        return self.insert_helper(self.root, val)
    
    def insert_helper(self, root, val):
        if not root:
            root = Node(val)
        elif root.info > val:
            root.left = insert_helper(root.left, val)
        elif root.info < val:
            root.right = insert_helper(root.right, val)
        return root

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)