import re

def getResult( lines ):
	result = 0
	for line in lines:
		rounds = line.split(':')[1]
		reds = [ int(x.split(' ')[0]) for x in re.findall(r'\d* red', rounds, re.I)]
		greens = [ int(x.split(' ')[0]) for x in re.findall(r'\d* green', rounds, re.I)]
		blues = [ int(x.split(' ')[0]) for x in re.findall(r'\d* blue', rounds, re.I)]
		result += max(reds) * max(greens) * max(blues)
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 2286 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
