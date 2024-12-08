def safe(levels):
	curr = levels[0]
	ascending = False
	if levels[1] == curr:
		return False
	if levels[1] > curr:
		ascending = True
	for l in levels[1:]:
		if ascending and (l <= curr or l-3 > curr):
			return 0
		if not ascending and (l >= curr or l+3 < curr):
			return 0
		curr = l
	return 1

def getResult( lines ):
	total = 0
	for line in lines:
		levels = [int(x) for x in line.split()]
		total += safe(levels)
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 2 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )