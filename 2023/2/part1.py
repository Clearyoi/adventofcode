import re

def getResult( lines ):
	result = 0
	for line in lines:
		gameNum = int(line.split(':')[0].split(' ')[-1])
		rounds = line.split(':')[1]
		reds = [ int(x.split(' ')[0]) for x in re.findall(r'\d* red', rounds, re.I)]
		greens = [ int(x.split(' ')[0]) for x in re.findall(r'\d* green', rounds, re.I)]
		blues = [ int(x.split(' ')[0]) for x in re.findall(r'\d* blue', rounds, re.I)]
		if max(reds) <= 12 and max(greens) <= 13 and max(blues) <= 14:
			result += gameNum
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 8 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
