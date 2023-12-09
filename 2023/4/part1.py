import re

def getResult( lines ):
	result = 0
	for line in lines:
		wins = set([int(x) for x in line.split(':')[1].split('|')[0].strip().split()])
		have = set([int(x) for x in line.split(':')[1].split('|')[1].strip().split()])
		matches = wins.intersection(have)
		if len(matches) > 0:
			result += pow(2,len(matches)-1)
		
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 13 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
