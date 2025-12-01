def getResult( lines ):
	left, amplitude, current = False, 0, 50
	total = 0
	for line in lines:
		left = line[0] == 'L'
		amplitude = int(line[1:])
		total += amplitude // 100
		if left:
			nxt = (current - amplitude) % 100
			if (nxt > current and current != 0) or nxt == 0:
				total += 1
		else:
			nxt = (current + amplitude) % 100
			if nxt < current:
				total += 1
		current = nxt
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 6 ):
	if runTest( readData( "input2.tst" ), 26 ):
		print( getResult( readData( "input.txt" ) ) )
	print( "Done" )