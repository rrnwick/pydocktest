# initialise
bothlist = []
leftlist = []
rightlist = []
numrows = 0
distance = 0

# read in file
with open("input.txt") as inputfile:
    for daline in inputfile:
        line = ''.join(daline.split('\n'))
        x = line.split('   ')
        bothlist.append(x)
        leftlist.append(x[0])
        rightlist.append(x[1])

# count rows and sort lists
numrows = len(leftlist)
print('numrows - ',numrows)
leftlist.sort()
rightlist.sort()

# iterate over lists and calculate distance and add value
for row in range(numrows):
    leftnum = int(leftlist[row])
    rightnum = int(rightlist[row])
    distance += abs(leftnum - rightnum)

# answer
print('distance = ',distance)
# distance =  2031679 correct!
# added for testing live changes to source code for running container.
