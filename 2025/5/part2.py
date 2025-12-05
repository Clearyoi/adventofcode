def getResult( lines ):
	total = 0
	ranges = []
	values = set()
	for line in lines:
		if not line:
			break
		l = line.split('-')
		ranges.append((int(l[0]), int(l[1])))
	removed = []
	ranges = sorted(ranges)
	newRanges = []
	count = 0
	while(count < 4): # I was lazy so I didnt make a real loop
		count += 1
		newRanges = []
		skipNext = False
		for i, r  in enumerate(ranges):
			if skipNext:
				skipNext=False
				continue
			if  i+1<len(ranges) and r[1] >= ranges[i+1][0]:
				newRanges.append((min(r[0],ranges[i+1][0]), max(r[1],ranges[i+1][1])))
				skipNext=True
			else:
				newRanges.append(r)
		ranges = newRanges
	for r in ranges:
		total += (r[1] - r[0]) + 1
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 14 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )