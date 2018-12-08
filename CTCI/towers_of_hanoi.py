#!/bin/python3

class Stack:
    
    def __init__(self):
    	self.items = []

    def empty(self):
    	return not self.items

    def peek(self):
    	return self.items[-1]

    def push(self, item):
    	self.items.append(item)

    def pop(self):
    	val = self.items.pop()
    	return val

class Tower:

	def __init__(self, idx):
		self.disks = Stack()
		self.idx = idx

	def index(self):
		return self.idx

	def add(self, d):
		if not self.disks.empty() and self.disks.peek() <= d:
			print('Error placing disk', d)
		else:
			self.disks.push(d)

	def move_top_to(self, t):
		top = self.disks.pop()
		t.add(top)

	def move_disks(self, n, dest, buff):
		if n > 0:
			self.move_disks(n-1, buff, dest)
			self.move_top_to(dest)
			buff.move_disks(n-1, dest, self)

if __name__ == '__main__':
	num = 5
	towers = []
	for i in range(num):
		towers.append(Tower(i))
	for i in range(num-1, -1, -1):
		towers[0].add(i)
	towers[0].move_disks(num, towers[2], towers[1])
	print(towers[2].disks.items)