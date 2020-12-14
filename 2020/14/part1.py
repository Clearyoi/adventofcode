def applyMask( mask, val ):
	andMask = int( mask.replace( "X", "1" ), 2 )
	orMask = int( mask.replace("X", "0"), 2 )
	val &= andMask
	val |= orMask
	return val


def getResult( data ):
	mem = dict()
	for line in data:
		partial = line.split(" = ")
		if partial[0] == "mask":
			mask = partial[1]
			continue
		address = int( partial[0].split("[")[1].split("]")[0] )
		val = int( partial[1].strip() )
		mem[address] = applyMask( mask, val )
	print(mem)
	result = sum( mem.values() )
	return result

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print("Test failed, expected {} got {}".format( expected, result ) )
	return False

if runTest( readData( "input.tst" ), 165 ):
	print( "The asnwer is {}".format( getResult( readData( "input.txt" ) ) ) )
