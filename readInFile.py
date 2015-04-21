edgeList = []

#cases: '1test_-10003.txt' 'g1.txt'

with open('test_cases/1test_-10003.txt', 'r') as f:
    heading = f.readline()
    heading = list(map(int,(heading.split())))

    edgeList = [list(map(int, line.split())) for line in f]

#TEST THE SPEED DIFFERENCE FOR THIS BELOW COMPARED TO ABOVE.
# ABOVE SUPPOSEDLY IS FASTER BECAUSE IT USES LIST COMPRESIONS
# WHICH ARE SUPPOSED TO BE FASTER THAN APPENDING IN A LOOP

##    for line in f:
##        lineStrArr = line.split()
##        lineIntArr = list(map(int, lineStrArr))
##        edgeList.append(lineIntArr)

    

print (heading)
print (edgeList)

