import math
def generateOps(numOps, i):
	# capped at 100 digits
	s = f'{i:100b}'[::-1]
	ops = ['+'] * numOps
	for j, _ in enumerate(ops):
		if s[j] == '1':
			ops[j] = '*'
	return ops

def calculate(values, ops):
	if len(values) != len(ops)+1:
		print("Generated bad ops")
		return 0
	total = values[0]
	for i, op in enumerate(ops):
		if op == '+':
			total += values[i+1]
		elif op == '*':
			total *= values[i+1]
		else:
			print("Invalid op")
			return 0
	return total


def isValid(result, values):
	numOps = len(values)-1
	for i in range(int(math.pow(2,numOps))):
		ops = generateOps(numOps, i)
		if calculate(values, ops) == result:
			return result
	return 0

def getResult( lines ):
	total = 0
	for line in lines:
		result = int(line[0])
		values = [int(x) for x in line[1].split(' ')]
		total += isValid(result, values)
	return total

def readData( filename ):
	return [[ x for x in y.split(': ') ] for y in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 3749 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
