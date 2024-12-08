def safe(levels):
	curr = levels[0]
	ascending = False
	if levels[1] == curr:
		return False
	if levels[1] > curr:
		ascending = True
	for l in levels[1:]:
		if ascending and (l <= curr or l-3 > curr):
			return False
		if not ascending and (l >= curr or l+3 < curr):
			return False
		curr = l
	return True


def getResult( lines ):
	total = 0
	for line in lines:
		levels = [int(x) for x in line.split()]
		for i in range(len(levels)):
			short_levels = levels[:i] + levels[i+1:]
			if safe(short_levels):
				total += 1
				break
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 4 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )