def getResult( lines ):
	total = 0
	vals = []
	for line in lines:
		vals.append(line.split())
	for i, v in enumerate(vals[-1]):
		if v == "+":
			res = 0
		elif v == "*":
			res = 1
		for j in range(len(vals) -1 ):
			if v == "+":
				res += int(vals[j][i])
			elif v == "*":
				res *= int(vals[j][i])
		total += res
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 4277556 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )