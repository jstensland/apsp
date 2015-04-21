edgeList = []

#cases: '1test_-10003.txt' 'g1.txt'

with open('g1.txt', 'r') as f:
    heading = f.readline()
    heading = list(map(int,(heading.split())))
    for line in f:
        line = line.split()
        line = list(map(int, line))
        edgeList.append(line)

print (heading)
print (edgeList)

##with open('g1.txt', 'r') as f:
##    data = f.readlines()
##
##    for line in data:
##        words = line.split()
##        

###read single line
##a = f.readline()
##
##print (a)
##
###read entire file
##b = f.read()
##
###print (b)
##
### good to read it in one line at a time.
##f = open('workfile', 'w')
##for line in f:
##    print(line, end='')
##
##
### better with a with statement
##with open('workfile', 'w') as f:
##    for line in f:
##        print(line, end='')
