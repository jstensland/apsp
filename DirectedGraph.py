#refactor to make some methods private, that should never be called on a graph alone.
#refactor to re-order i, j and k such that in the end you can just find the mine for the last
#2D matrix

import pprint
class DirectedGraph(object):
 #   import pprint

    def __init__(self, edgeList, nodeCount, edgeCount):
        self.edgeList = edgeList
        self.nodeCount = nodeCount
        self.edgeCount = edgeCount
        self.pathLengthsMatrix = []

    def __str__(self):
        edgeStrList = list(map(str, self.edgeList))
        nodeCount = 'Node Count: ' + str(self.nodeCount) + ' \n'
        edgeCount = 'Edge Count: ' + str(self.edgeCount) + ' \n'
        edges = 'Edges List: \n' + '\n'.join(edgeStrList) + '\n'
        objectId = self.__repr__()
        return nodeCount + edgeCount + edges + objectId

    def findShortestShortestPath(self):
        self.asapFloydWarshall()
        if self.negativeCycleCheck():
            return "negative Cycle!"
        else:
            return self.shortestShortestPathFW()

    def negativeCycleCheck(self):
        negativeCycle = False
        for i in range(self.nodeCount):
            if self.pathLengthsMatrix[i][i][self.nodeCount-1] != 0:
                negativeCycle = True
        return negativeCycle

    def shortestShortestPathFW(self):
        shortest = 100000000
        for i in range(self.nodeCount):
            for j in range(self.nodeCount):
                if self.pathLengthsMatrix[i][j][self.nodeCount-1] != None:
                    if self.pathLengthsMatrix[i][j][self.nodeCount-1] < shortest:
                        shortest = self.pathLengthsMatrix[i][j][self.nodeCount-1]
        return shortest

    def asapFloydWarshall(self):
        #initialize Matrix
        self.pathLengthsMatrix = [[[self.initializeArrayValue(i, j, k)
                              for k in range(self.nodeCount)]
                             for j in range(self.nodeCount)]
                            for i in range(self.nodeCount)]
        self.addInitialEdgeValues()
        self.calculatePathLengthsMatrix()
        
        pprint.pprint(self.pathLengthsMatrix)

    def initializeArrayValue(self, i, j, k):
        initialValue = None
        if i == j and k == 0:
            initialValue = 0
        return initialValue

    def addInitialEdgeValues(self):
        for edge in self.edgeList:
            self.pathLengthsMatrix[edge[0]][edge[1]][0] = edge[2]

    def calculatePathLengthsMatrix(self):
        for k in range(1, self.nodeCount):
            for i in range(self.nodeCount):
                for j in range(self.nodeCount):
                    #print ([i, j, k])
                    self.pathLengthsMatrix[i][j][k] = self.newPathLength(i, j, k)

    def newPathLength(self, i, j, k):
        #if nodes not connected and k doesn't connect them, still unconnected.
        if self.pathLengthsMatrix[i][j][k-1] != None:
            case1 = self.pathLengthsMatrix[i][j][k-1]
        else:
            case1 = None
                
        if self.pathLengthsMatrix[i][k][k-1] != None and self.pathLengthsMatrix[k][j][k-1] != None:
            case2 = self.pathLengthsMatrix[i][k][k-1] + self.pathLengthsMatrix[k][j][k-1]
        else:
            case2 = None

        if case1 == None and case2 == None:
            return None
        elif case1 == None:
            return case2
        elif case2 == None:
            return case1
        else:
            return min(case1, case2)
        
