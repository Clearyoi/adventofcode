def addAntiNodes(antiNodes, lines, x, y, ch):
	for i, line in enumerate(lines):
		for j, c in enumerate(line):
			if i == x and j == y:
				continue
			if c == ch:
				newX = x+(2*(i-x))
				newY = y+(2*(j-y))
				antiNodes.add((newX,newY))

def inBounds(node, width, height):
	if node[0] < 0 or node[0] >= height:
		return False
	if node[1] < 0 or node[1] >= width:
		return False
	return True

def getResult( lines ):
	antiNodes, finalNodes = set(), set()
	for i, line in enumerate(lines):
		for j, ch in enumerate(line):
			if ch != '.':
				addAntiNodes(antiNodes, lines, i, j, ch)
	for node in antiNodes:
		if inBounds(node, len(lines), len(lines[0])):
			finalNodes.add(node)
	return len(finalNodes)

def readData( filename ):
	return [list(x) for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 14 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
