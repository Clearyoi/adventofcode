def getResult( lines ):
	total = 0
	for line in lines:
		nums = [int(x) for x in line]
		high, start = 0, 0
		for i, n in enumerate(nums[:-1]):
			if n > high:
				high = n
				start = i
		total += high*10 + max(nums[start+1:])
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 357 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )