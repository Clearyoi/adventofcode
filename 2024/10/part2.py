def countPaths(lines, x, y):
	start = (x,y)
	nextSteps = [(x,y)]
	for i in range(1,10):
		nextSteps = nextStep(lines, nextSteps, i)
		if not nextSteps:
			return 0
	return len(nextSteps)

def nextStep(lines, starts, i):
	nextSteps = []
	height = len(lines)
	width = len(lines[0])
	for s in starts:
		node = (s[0]-1,s[1])
		if inBounds(node, width, height) and lines[node[0]][node[1]] == i:
			nextSteps.append(node)
		node = (s[0]+1,s[1])
		if inBounds(node, width, height) and lines[node[0]][node[1]] == i:
			nextSteps.append(node)
		node = (s[0],s[1]-1)
		if inBounds(node, width, height) and lines[node[0]][node[1]] == i:
			nextSteps.append(node)
		node = (s[0],s[1]+1)
		if inBounds(node, width, height) and lines[node[0]][node[1]] == i:
			nextSteps.append(node)
	return nextSteps

def inBounds(node, width, height):
	if node[0] < 0 or node[0] >= height:
		return False
	if node[1] < 0 or node[1] >= width:
		return False
	return True

def getResult( lines ):
	total = 0
	for i, line in enumerate(lines):
		for j, val in enumerate(line):
			if val == 0:
				total += countPaths(lines, i, j)
	return total

def readData( filename ):
	return [[int(y) for y in list(x) ]for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 81 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )