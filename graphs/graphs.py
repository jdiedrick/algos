class Vertex:
	def __init__(self, key):
		self.id = key
		self.connectedTo = {}
	
	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr] = weight

	def __str__(self):
		return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self, nbr):
		return self.connectedTo[nbr]

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0
	
	def addVertex(self, key):
		self.numVertices = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self, n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None
	
	def __contains__(self, n):
		return n in self.vertList

	def addEdge(self, f, t, cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())



g  = Graph()

'''
for i in range(6):
	g.addVertex(i)

g.vertList

g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)


for v in g:
	for w in v.getConnections():
		print( "(%s, %s)" % (v.getId(), w.getId()) )
'''

with open("graph.txt", "r") as f:
	for line in f:
#		print line
		splitted = line.strip().split("	")
		startVertex = splitted[0]
		g.addVertex(startVertex)
		splitted.pop(0)
	for line in f:
		splitted = line.strip().split("	")
		startVertex = splitted[0]
		splitted.pop(0)
		for v in splitted:
			splitEdge = v.split(",")
#			print startVertex
#			print splitEdge
			g.addEdge(startVertex, splitEdge[0], splitEdge[1])

#print g.getVertices()


def dijkstra(graph, initial):
	visited = {initial: 0}
	path = {}
	vertices = set()
	for v in g.getVertices():
		vertices.add(v)
	print vertices
	
	while vertices:
		min_vertex = None
		for vertex in vertices:
			if vertex in visited:
				if min_vertex is None:
					min_vertex  = vertex
				elif visited[vertex] < visited[min_vertex]:
					min_vertex = vertex
		if min_vertex is None:
			break

		vertices.remove(min_vertex)
		current_weight = visited[min_vertex]

	print "ok"

dijkstra(g, '1')
