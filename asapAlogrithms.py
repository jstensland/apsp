import GraphReader

#cases: 'test_cases/1test_-10003.txt' 'test_cases/g1.txt'
graphReader = GraphReader.GraphReader()

file = 'test_cases/1test_-10003.txt'
headerSize = 1
header = graphReader.readHeader(file, headerSize)
edgeList = graphReader.readNodes(file, headerSize)


print (header)
print (edgeList)
