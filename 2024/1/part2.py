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
		count = 0
		for r in right:
			if r == l:
				count += 1
		garbage = count * l
		total += garbage
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 31 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )