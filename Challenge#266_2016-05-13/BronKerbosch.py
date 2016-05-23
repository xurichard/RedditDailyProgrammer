from collections import defaultdict

class graph(object):
	def __init__(self, connections, directed=False):
		self._graph = defaultdict(set)
		self._directed = directed
		self.add_connections(connections)

	def add_connections(self, connections):
		for node1, node2 in connections:
			self._graph[node1].add(node2)
			if not self._directed:
				self._graph[node2].add(node1)

	def addNode(self, node1, node2):
		self._graph[node1].add(node2)
		if not self._directed:
			self._graph[node2].add(node1)

	def allNodes(self):
		return set(self._graph.keys())

	def getNeighbors(self, node):
		return self._graph[node]


def BronKerboschNoPivot(clique, candidates, excluded, graph):
	if not candidates and not excluded:
		return clique
	for v in list(candidates):
		n = graph.getNeighbors(v)
		# newClique = clique | {v}
		# newCandidates = candidates & n
		# newExcluded = excluded & n
		# BronKerboschNoPivot(newClique, newCandidates, newExcluded, graph)
		BronKerboschNoPivot(clique | {v}, candidates & n, excluded & n, graph)
		candidates.remove(v)
		excluded.add(v)

if __name__ == '__main__':
	f = open('graph.txt','r')
	numNodes = f.next()
	connections = []
	for line in f:
		#Every line will have two numbers
		numbers = line[0:len(line)-1].split(" ")
		connections.append(tuple(numbers[:2]))
	graph = graph(connections)
	print(BronKerboschNoPivot(set(), graph.allNodes(), set(), graph))













class node(object):
	def __init__(self, neighbors):
		if neighbors:
			self.__neighbors = neighbors
		else:
			self.__neighbors = set()

	def addNeighbor(neighbor):
		self.__neighbors.add(neighbor)

	def removeNeighbor(neighbor):
		self.__neighbors.remove(neighbor)

	def numNeighbors():
		return len(self.__neighbors)

	def getNeighbors():
		return self.__neighbors









		