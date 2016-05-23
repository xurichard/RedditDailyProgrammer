from collections import defaultdict

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


def BronKerboschNoPivot(R, P, X, graph):
	if not P and not X:
		return R
	for v in P:
		n = graph.getNeighbors(v)
		BronKerboschNoPivot(R.copy().union({v}), P.intersection(n), X.intersection(n), graph)
		P = P.remove(v)
		X = X.add(v)

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























		