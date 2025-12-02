import re

def getResult( lines ):
	total = 0
	for line in lines:
		start, end = int(line.split('-')[0]), int(line.split('-')[1])
		for num in range(start, end+1):
			numStr = str(num)
			if re.match('^(.+)\\1+$', numStr):
				total += int(numStr)
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( ',' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 4174379265 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )