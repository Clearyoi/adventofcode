def getResult( lines ):
	oxy = trimLines(lines, 0, False)
	co2 = trimLines(lines, 0, True)
	print(oxy, co2)
	return oxy * co2

def trimLines( lines, index, inverted ):
	if len(lines) == 1:
		result = 0
		for i, c in enumerate(lines[0]):
			if c == '1':
				result += pow(2, len(lines[0])-(i + 1))
		return result
	count = 0
	for line in lines:
		char = line[index]
		if char == '0':
			count -= 1
		if char == '1':
			count += 1
	expected = count >= 0
	if inverted:
		expected = not expected
	expectedValue = 1 if expected else 0
	lines = [l for l in lines if int(l[index]) == expectedValue]
	return trimLines(lines, index + 1, inverted)
	


def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print("Test failed, expcted {} got {}".format( expected, result ) )
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 230 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
