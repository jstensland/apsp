import GraphReader
import DirectedGraph


graphReader = GraphReader.GraphReader()

#cases: 'test_cases/1test_-10003.txt'
#       'test_cases/2test_-6.txt'
#       'test_cases/3test_negcycle.txt'
#       'test_cases/g1.txt'

file =  'test_cases/1test_-10003.txt'
headerSize = 1
header = graphReader.readHeader(file, headerSize) # [nodeCount, edgeCount]
edgeList = graphReader.readNodes(file, headerSize) # [head, tail, weight]

graph = DirectedGraph.DirectedGraph(edgeList, header[0][0], header[0][1])

#graph.asapFloydWarshall()
print (graph.findShortestShortestPath())

#print (graph)




#print ([method for method in dir(graph) if callable(getattr(graph, method))])
