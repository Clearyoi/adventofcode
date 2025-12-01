def processCell(lines, x, y):
	lines[x][y] = '#'
	return 0

def getResult( lines ):
	total = 0
	for i, line in enumerate(lines):
		for j, ch in enumerate(line):
			total += processCell(lines, i, j)
			print(lines)
	return total

def readData( filename ):
	return [list(x) for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 1930 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )