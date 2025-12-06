import math

def getResult( lines ):
	total = 0
	width = len(lines[0])
	height = len(lines)
	op = ""
	nums = []
	for w in range(width):
		num = ""
		for h in range(height):
			if lines[h][w] == "+":
				op = "+"
			elif lines[h][w] == "*":
				op = "*"
			elif lines[h][w] != ' ':
				num += lines[h][w]
		if not num: #This only works because I added a space to the end of every line in the input
			if op == "+":
				total += sum([int(x) for x in nums if x])
			elif op == "*":
				total += math.prod([int(x) for x in nums if x])
			nums = []
		else:
			nums.append(num)
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 3263827 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )