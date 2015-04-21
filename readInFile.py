edgeList = []

#cases: '1test_-10003.txt' 'g1.txt'


def lineToIntArr(line):
    lineStrArr = line.split()
    lineIntArr = list(map(int, lineStrArr))
    return lineIntArr

#One line should be fast but less readable?
    
#edgeList = [list(map(int, line.split())) for line in f]

# TEST THE SPEED DIFFERENCE FOR THIS BELOW COMPARED TO ABOVE/below.
# ABOVE SUPPOSEDLY IS FASTER BECAUSE IT USES LIST COMPRESIONS
# WHICH ARE SUPPOSED TO BE FASTER THAN APPENDING IN A LOOP

##    for line in f:
##        lineStrArr = line.split()
##        lineIntArr = list(map(int, lineStrArr))
##        edgeList.append(lineIntArr)


with open('test_cases/1test_-10003.txt', 'r') as f:
    heading = f.readline()
    heading = list(map(int,(heading.split())))

    edgeList = [lineToIntArr(line) for line in f]

print (heading)
print (edgeList)

