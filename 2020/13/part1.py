def getResult( lines ):
	currentTime = int( lines[0] )
	bestTime = 100000
	result = 0
	for time in lines[1].split( "," ):
		if time == "x":
			continue
		time = int( time )
		nextDepart = time - ( currentTime % time )
		if nextDepart < bestTime:
			bestTime = nextDepart
			result = nextDepart * time
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print("Test failed, expcted {} got {}".format( expected, result ) )
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 295 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
