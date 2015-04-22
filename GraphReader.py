class GraphReader(object):

    def __init__(self):
      pass
    
    def readHeader(self, file, headerSize = 1):
        header = []
        with open(file, 'r') as f:
            for x in range(0, headerSize):
                headerStr = f.readline()
                headerArr = self.lineToIntArr(headerStr)
                header.append(headerArr)
        return header

    def readNodes(self, file, headerSize = 1):
        edgeList = []
        with open(file, 'r') as f:
            for x in range(0, headerSize):
                f.readline()
            edgeList = [self.lineToIntArr(line) for line in f]           
        return edgeList

    
    def lineToIntArr(self, line):
        lineStrArr = line.split()
        lineIntArr = list(map(int, lineStrArr))

        #to not reindex the nodes, simply:
        return lineIntArr
        
##      #this part reindexes the nodes to start with node 0
##        if len(lineIntArr) == 3:
##            i = lineIntArr[0] - 1
##            j = lineIntArr[1] - 1
##            reIndex = [i, j, lineIntArr[2]]
##            return reIndex
##        else:
##            return lineIntArr
        





#squares = list(map(lambda x: x**2, range(10)))

#or, equivalently:

#squares = [x**2 for x in range(10)]


    #One line should be fast but less readable? 
    #edgeList = [list(map(int, line.split())) for line in f]


    # TEST THE SPEED DIFFERENCE FOR THIS BELOW COMPARED TO ABOVE/below.
    # ABOVE SUPPOSEDLY IS FASTER BECAUSE IT USES LIST COMPRESIONS
    # WHICH ARE SUPPOSED TO BE FASTER THAN APPENDING IN A LOOP

    ##    for line in f:
    ##        lineStrArr = line.split()
    ##        lineIntArr = list(map(int, lineStrArr))
    ##        edgeList.append(lineIntArr)


    # can I refactor the taking in of the first couple lines of the file?
    
