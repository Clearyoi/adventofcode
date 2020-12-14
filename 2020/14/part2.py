def listVals( mask, baseVal ):
	if "X" not in mask:
		return [baseVal]
	i = mask.find( "X" )
	vals = listVals( mask[i+1:], baseVal[i+1:])
	prefix = baseVal[:i]
	allVals = []
	for val in vals:
		allVals.append( prefix + "0" + val )
		allVals.append( prefix + "1" + val )
	return allVals

def applyMask( mask, val ):
	orMask = int( mask.replace("X", "0"), 2 )
	val |= orMask
	return [ int ( x ) for x in listVals( mask, "{0:036b}".format( val ) ) ]

def getResult( data ):
	mem = dict()
	for line in data:
		partial = line.split(" = ")
		if partial[0] == "mask":
			mask = partial[1]
			continue
		address = int( partial[0].split("[")[1].split("]")[0] )
		val = int( partial[1].strip() )
		addresses = applyMask( mask, address )
		for addr in addresses:
			mem[addr] =  val
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

if runTest( readData( "input2.tst" ), 208 ):
	print( "The asnwer is {}".format( getResult( readData( "input.txt" ) ) ) )