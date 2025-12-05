def getResult( lines ):
	total = 0
	ranges = []
	values = []
	space = False
	for line in lines:
		if not line:
			space = True
			continue
		if not space:
			l = line.split('-')
			ranges.append((int(l[0]), int(l[1])))
		else:
			values.append(int(line))
	for value in values:
		for r  in ranges:
			if value >= r[0] and value <= r[1]:
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

if runTest( readData( "input.tst" ), 3 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )