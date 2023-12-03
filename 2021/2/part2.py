def getResult( lines ):
	pos, dep, aim = 0, 0, 0
	for line in lines:
		l = line.split()
		if l[0] == "forward":
			pos += int(l[1])
			dep += int(l[1]) * aim
		if l[0] == "down":
			aim += int(l[1])
		if l[0] == "up":
			aim -= int(l[1])
	return pos * dep

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print("Test failed, expcted {} got {}".format( expected, result ) )
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 900 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
