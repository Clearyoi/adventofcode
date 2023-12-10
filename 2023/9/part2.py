def isAllZero(pattern):
	for x in pattern:
		if x != 0:
			return False
	return True

def figureOutNext(pattern):
	newPattern = []
	for i, x in enumerate(pattern):
		if i == 0:
			continue
		newPattern.append(x - pattern[i-1])
	if isAllZero(newPattern):
		return pattern[0]
	answer = pattern[0] - figureOutNext(newPattern)
	return answer

def getResult( lines ):
	result = 0
	for line in lines:
		result += figureOutNext([int(x) for x in line.split()])
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 2 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
