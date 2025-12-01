def getResult( lines ):
	left, amplitude, current = False, 0, 50
	total = 0
	for line in lines:
		left = line[0] == 'L'
		amplitude = int(line[1:])
		if left:
			current = (current - amplitude) % 100
		else:
			current = (current + amplitude) % 100
		if current == 0:
			total += 1
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 3 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )