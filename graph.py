class Graph:
    def __init__(self):
        self.nodeCount = 0
        self.adjacentList = {}
    
    def __str__(self):
        return str(self.__dict__)
    
    def addVertex(self, node):
        self.adjacentList[node] = []
        self.nodeCount += 1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
    
    def showConnection(self):
        for i in self.adjacentList:
            print(i, end = '-->')
            for j in self.adjacentList[i]:
                print(j, end = '')
            print()

newGraph = Graph()
newGraph.addVertex('0')
newGraph.addVertex('1')
newGraph.addVertex('2')
newGraph.addVertex('3')
newGraph.addEdge('3', '1')
print(newGraph)
newGraph.showConnection()