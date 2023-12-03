def getResult( lines ):
	currentHeight = lines[0] + lines[1] + lines[2]
	result = 0
	for i, h in enumerate(lines[:-2]):
		height = h + lines[i+1] + lines[i+2]
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

if runTest( readData( "input.tst" ), 5 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
