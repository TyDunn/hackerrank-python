#!/bin/python3

from collections import defaultdict

class Graph:

	def __init__(self, nodes):
		self.nodes = nodes 
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def is_cyclic_util(self, v, visited, parent):
		visited[v] = True
		for i in self.graph[v]:
			if not visited[i]:
				if self.is_cyclic_util(i, visited, v):
					return True
			elif parent != i:
				return True
		return False

	def is_cyclic(self):
		visited = [False] * (self.nodes)
		for i in range(self.nodes):
			if not visited[i]:
				if self.is_cyclic_util(i, visited, -1):
					return True
		return False

if __name__ == '__main__':
	g1 = Graph(5)
	g1.add_edge(1, 0)
	g1.add_edge(0, 2)
	g1.add_edge(2, 0)
	g1.add_edge(0, 3)
	g1.add_edge(3, 4)
	print(g1.is_cyclic())
	g2 = Graph(3)
	g2.add_edge(0, 1)
	g2.add_edge(1, 2)
	print(g2.is_cyclic())