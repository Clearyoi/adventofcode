def factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]

def largestCommonFactor(num1, num2):
	f1 = sorted(factors(num1), reverse=True)
	f2 = factors(num2)
	for f in f1:
		if f in f2:
			return f
	print("oops")
	return 1

def addAntiNodes(antiNodes, lines, width, height, x, y, ch):
	for i, line in enumerate(lines):
		for j, c in enumerate(line):
			if i == x and j == y:
				continue
			if c == ch:
				distX = (2*(i-x))
				distY = (2*(j-y))
				lf = largestCommonFactor(abs(distX), abs(distY))
				distX = int(distX/lf)
				distY = int(distY/lf)
				newX = x + distX
				newY = y + distY
				while inBounds((newX,newY), width, height):
					antiNodes.add((newX,newY))
					newX += distX
					newY += distY

def inBounds(node, width, height):
	if node[0] < 0 or node[0] >= height:
		return False
	if node[1] < 0 or node[1] >= width:
		return False
	return True

def getResult( lines ):
	antiNodes, finalNodes = set(), set()
	width = len(lines)
	height = len(lines[0])
	for i, line in enumerate(lines):
		for j, ch in enumerate(line):
			if ch != '.':
				addAntiNodes(antiNodes, lines, width, height, i, j, ch)
	for node in antiNodes:
		if inBounds(node, width, height):
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

if runTest( readData( "input.tst" ), 34 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
