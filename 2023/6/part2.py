import re

def calcDist(holdFor, time):
	if holdFor >= time:
		return 0
	return (time-holdFor)*(holdFor)


def getResult( lines ):
	result = 0
	time = int(re.sub(' ','',lines[0].split(':')[1]))
	reqDist = int(re.sub(' ','',lines[1].split(':')[1]))
	prev = 0
	valid = 0
	for j in range(time+1):
		dist = calcDist(j, time)
		if dist < prev:
			break
		if dist >= reqDist:
			valid += 1
	if valid != 0:
		result = valid
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 71503 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
