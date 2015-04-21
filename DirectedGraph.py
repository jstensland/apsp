import pprint
class DirectedGraph(object):
 #   import pprint

    def __init__(self, edgeList, nodeCount, edgeCount):
        self.edgeList = edgeList
        self.nodeCount = nodeCount
        self.edgeCount = edgeCount
        self.pathLengths = []

    def __str__(self):
        edgeStrList = list(map(str, self.edgeList))
        nodeCount = 'Node Count: ' + str(self.nodeCount) + ' \n'
        edgeCount = 'Edge Count: ' + str(self.edgeCount) + ' \n'
        edges = 'Edges List: \n' + '\n'.join(edgeStrList) + '\n'
        objectId = self.__repr__()
        return nodeCount + edgeCount + edges + objectId

    def asapFloydWarshall(self):
        self.pathLengths = [[[self.initializeArrayValue(i, j, k)
                              for k in range(self.nodeCount)]
                             for j in range(self.nodeCount)]
                            for i in range(self.nodeCount)]
        self.addInitialEdgeValues()
        
        pprint.pprint(self.pathLengths)

    def initializeArrayValue(self, i, j, k):
        initialValue = None
        if i == j and k == 0:
            initialValue = 0
        return initialValue

    def addInitialEdgeValues(self):
        for edge in self.edgeList:
            self.pathLengths[edge[0]][edge[1]][0] = edge[2]
        
