def getResult( lines ):
	result = 0
	for line in lines:
		firstDigit = 0
		for symbol in line:
			if symbol.isnumeric():
				lastDigit = symbol
				if not firstDigit:
					firstDigit = symbol
		result += int(firstDigit + lastDigit)
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 142 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
