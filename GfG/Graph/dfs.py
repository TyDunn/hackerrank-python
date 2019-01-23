#!/bin/python3

from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def dfs(self, s):
		visited = [False] * len(self.graph)
		self.dfs_util(s, visited)

	def dfs_util(self, v, visited):
		visited[v] = True
		print(v, end=" ")
		for node in self.graph[v]:
			if not visited[node]:
				self.dfs_util(node, visited)

if __name__ == '__main__':
	g = Graph()
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)
	g.dfs(2)
	print()