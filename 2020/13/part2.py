import operator

def getResult( data ):
	buses = dict()
	for i, bus in enumerate( data ):
		if bus == "x":
			continue
		buses[int( bus )] = int( bus ) - i
	return chineseRemainderTheorem( buses )

def chineseRemainderTheorem( buses ):
	n = buses.keys()
	a = [buses[x] for x in n]
	M = reduce( operator.mul, n )
	m = [ M//x for x in n ]
	mi = [ inv(m[i], x) for (i, x) in enumerate( n ) ]
	Y = sum ( [ mi[i] * m[i] * x for (i, x) in enumerate( a ) ] )
	return Y%M	

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ][1].split(",")

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print("Test failed, expected {} got {}".format( expected, result ) )
	return False

# This is not my method.
# I don't know it works *sigh*
# It was written by by Nikita Tiwari
def inv(a, m) : 
	m0 = m 
	x0 = 0
	x1 = 1
	if (m == 1) : 
		return 0
	# Apply extended Euclid Algorithm 
	while (a > 1) : 
		# q is quotient 
		q = a // m 
		t = m 
		# m is remainder now, process 
		# same as euclid's algo 
		m = a % m 
		a = t 
		t = x0 
		x0 = x1 - q * x0 
		x1 = t 
	# Make x1 positive 
	if (x1 < 0) : 
		x1 = x1 + m0 
	return x1 

tests = []
tests.append( ("17,x,13,19".split(","), 3417 ) )
tests.append( ("67,7,59,61".split(","), 754018 ) )
tests.append( ("67,x,7,59,61".split(","), 779210 ) )
tests.append( ("67,7,x,59,61".split(","), 1261476 ) )
tests.append( ("1789,37,47,1889".split(","), 1202161486 ) )

for test in tests:
	if not runTest( test[0], test[1] ):
		break

if runTest( readData( "input.tst" ), 1068781 ):
	print( "The asnwer is {}".format( getResult( readData( "input.txt" ) ) ) )
