class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next

if __name__ == '__main__':

	ll = LinkedList()

	ll.head = Node(1)
	second = Node(2)
	ll.head.next = second
	third = Node(3)
	second.next = third

	ll.print_list()