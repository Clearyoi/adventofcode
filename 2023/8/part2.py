import re
from math import lcm

def traverseStep(nodes, position, operation):
	if operation == 'L':
		return nodes[position][0]
	return nodes[position][1]

def traverseToEnd(start, nodes, operations, stepsTaken):
	result = 0
	position = start
	while True:
		operation = operations[result%len(operations)]
		position = traverseStep(nodes, position, operation)
		result += 1
		if position.endswith('Z'):
			break
	return result, position

def setupNodes(lines):
	nodes = {}
	for line in lines[2:]:
		name = line.split('=')[0].strip()
		left = re.sub(r'\(', '', line.split('=')[1].split(',')[0]).strip()
		right = re.sub(r'\)', '', line.split('=')[1].split(',')[1]).strip()
		nodes[name] = (left, right)
	return nodes

def getResult( lines ):
	nodes = setupNodes(lines)
	traverseTimes = {}
	operations = lines[0]
	for node in [x for x in nodes.keys() if x.endswith('A')]:
		initial, endpos = traverseToEnd(node, nodes, operations, 0)
		recurring, _ = traverseToEnd(endpos, nodes, operations, initial)
		traverseTimes[node] = (initial, recurring)
	totals = []
	for k in traverseTimes.values():
		totals .append(k[1])
	return lcm(*totals)

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input2.tst" ), 6 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
