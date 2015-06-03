import GraphReader
import DirectedGraph

graphReader = GraphReader.GraphReader()

# cases: 'test_cases/1test_-10003.txt'
#       'test_cases/2test_-6.txt'
#       'test_cases/3test_negcycle.txt'
#       'test_cases/4test_larger_negativeCycle.txt'
#       'test_cases/5test_larger_-7.txt'
#       'test_cases/6test_larger_-2.txt'

#       'test_cases/g1.txt'
#       'test_cases/g2.txt'
#       'test_cases/g3.txt'

file = 'test_cases/hwQ4test.txt'
print('File: ' + file)
headerSize = 1
header = graphReader.readHeader(file, headerSize)  # [nodeCount, edgeCount]
edgeList = graphReader.readNodes(file, headerSize)  # [head, tail, weight]

print("read graph")
graph = DirectedGraph.DirectedGraph(edgeList, header[0][0], header[0][1])
print("created Graph")
# graph.asapFloydWarshall()

print(graph.findShortestShortestPath())

# print (graph)

# import cProfile
# import re
# cProfile.run('graph.findShortestShortestPath()')


# print ([method for method in dir(graph) if callable(getattr(graph, method))])
