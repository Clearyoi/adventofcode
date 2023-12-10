import re

def traverse(nodes, position, operation):
	if operation == 'L':
		return nodes[position][0]
	return nodes[position][1]

def getResult( lines ):
	result = 0
	nodes = {}
	operations = lines[0]
	position = 'AAA'
	for line in lines[2:]:
		name = line.split('=')[0].strip()
		left = re.sub(r'\(', '', line.split('=')[1].split(',')[0]).strip()
		right = re.sub(r'\)', '', line.split('=')[1].split(',')[1]).strip()
		nodes[name] = (left, right)
	while (position != 'ZZZ'):
		operation = operations[result%len(operations)]
		position = traverse(nodes, position, operation)
		result += 1
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 6 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
