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
		self._graph = dict(set())
		self._directed = directed
		self.add_connections()

	def add_connections():
		for node1, node2 in connections:
			self._graph[node1].add(node2)
			if not directed:
				self._graph[node2].add(node1)

	def 

def BronKerboschNoPivot(R, P, X, graph):
	if not P and not X:
		return R
	for v in P:
		BronKerboschNoPivot(R.add(v), P.intersect(v.getNeighbors()), X.intersect(v.getNeighbors()), graph)
		P = P.remove(v)
		X = X.add(v)









if __name__ == '__main__':
	f = open('graph.txt','r')
	numNodes = f.next()
	nodes = dict()
	for line in f:
		#Every line will have two numbers
		numbers = line.split()





		