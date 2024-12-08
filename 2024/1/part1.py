def getResult( lines ):
	left, right = [], []
	total = 0
	for line in lines:
		values = line.split()
		left.append(int(values[0]))
		right.append(int(values[1]))
	left.sort()
	right.sort()
	for i, l in enumerate(left):
		total += abs(right[i]-l)
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 11 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )