def getJoltage(nums, scale):
	if scale == 1:
		return max(nums)
	high, start = 0, 0
	for i, n in enumerate(nums[:-(scale-1)]):
		if n > high:
			high = n
			start = i
	return high*pow(10,scale-1)+getJoltage(nums[start+1:], scale-1)


def getResult( lines ):
	total = 0
	for line in lines:
		nums = [int(x) for x in line]
		total += getJoltage(nums, 12)
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 3121910778619 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )