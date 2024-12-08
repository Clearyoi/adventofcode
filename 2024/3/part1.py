import re
def getResult( lines ):
	total = 0
	ops = re.findall(r"mul\(\d{1,3},\d{1,3}\)", lines)
	for op in ops:
		nums = [int(x) for x in re.findall(r"\d+", op)]
		total += nums[0] * nums[1]
	return total

def readData( filename ):
	return  open( filename ).read().strip() 

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 161 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )