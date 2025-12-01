import re

def getResult( lines ):
	total = 0
	claws = []
	print(lines)
	for line in lines:
		mA = re.match(r'Button A: X\+(\d+), Y\+(\d+)',line[0])
		mB = re.match(r'Button B: X\+(\d+), Y\+(\d+)',line[1])
		mP = re.match(r'Prize: X=(\d+), Y=(\d+)',line[2])
		a = (mA.group(1),mA.group(2))
		b = (mB.group(1),mB.group(2))
		p = (mP.group(1),mP.group(2))
		claws.append((p, a, b))
	print(claws)
	return total

def readData( filename ):
	return [x for x in open( filename ).read().strip().split( '\n' ) ]

def readData( filename ):
	return [[x for x in y.split('\n')] for y in open( filename ).read().strip().split( '\n\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 480 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )