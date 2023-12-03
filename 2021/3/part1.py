def getResult( lines ):
	result = [0] * len(lines[0])
	gam, epi = 0, 0
	for line in lines:
		for i, char in enumerate(line):
			if char == '0':
				result[i] -= 1
			if char == '1':
				result[i] += 1
	for i, val in enumerate(result):
		if val == 0:
			print("logic hole")
			sys.exit(1)
		if val > 0:
			gam += pow(2, len(result)-(i + 1))
		if val < 0:
			epi += pow(2, len(result)-(i + 1)) 
	return gam * epi


def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print("Test failed, expcted {} got {}".format( expected, result ) )
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 198 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
