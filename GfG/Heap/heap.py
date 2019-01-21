#!/bin/python3

from heapq import heappush, heappop, heapify
import math

class MinHeap:

	def __init__(self):
		self.heap = []

	def parent(self, i):
		return (i - 1) // 2

	def insert_key(self, k):
		heappush(self.heap, k)

	def decrease_key(self, i, new_val):
		self.heap[i] = new_val
		while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
			self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

	def extract_min(self):
		return heappop(self.heap)

	def delete_key(self, i):
		self.decrease_key(i, -math.inf)
		self.extract_min()

	def get_min(self):
		return self.heap[0]

if __name__ == '__main__':
	heap = MinHeap()
	heap.insert_key(3)
	heap.insert_key(2)
	heap.delete_key(1)
	heap.insert_key(15)
	heap.insert_key(5)
	heap.insert_key(4)
	heap.insert_key(45)

	print(heap.extract_min())
	print(heap.get_min())
	heap.decrease_key(2, 1)
	print(heap.get_min())