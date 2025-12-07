def getResult( lines ):
	total = 0
	for i, line in enumerate(lines[:-1]):
		for j, v in enumerate(line):
			if v == "S" or v == "B":
				if lines[i+1][j] == "^":
					lines[i+1][j-1] = "B"
					lines[i+1][j+1] = "B"
					total += 1
				else:
					lines[i+1][j] = "B"
	return total

def readData( filename ):
	return [ list(x) for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 21 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )