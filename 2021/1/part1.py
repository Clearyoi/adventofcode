def getResult( lines ):
	currentHeight = lines[0]
	result = 0
	for height in lines:
		if height > currentHeight:
			result += 1
		currentHeight = height
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print("Test failed, expcted {} got {}".format( expected, result ) )
	return False
	
def readData( filename ):
	return [ int(x) for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 7 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
