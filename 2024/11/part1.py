from collections import defaultdict

def processStone(stone):
	if stone == 0:
		return [1]
	stringStone = str(stone)
	length = len(stringStone)
	if length%2 == 0:
		return [int(stringStone[:int(length/2)]),int(stringStone[int(length/2):])]
	return [stone*2024]


def processStep(stones):
	newStones = defaultdict(int)
	oldStones = list(stones.keys())
	for o in oldStones:
		count = stones[o]
		newStoneValues = processStone(o)
		for n in newStoneValues:
			newStones[n] += count
	return newStones

def getResult( line ):
	steps = 25
	total = 0
	stones = defaultdict(int)
	for stone in line:
		stones[stone] += 1
	for step in range(steps):
		stones = processStep(stones)
	for count in stones.values():
		total += count
	return total

def readData( filename ):
	return [int(x) for x in open( filename ).read().strip().split( ' ' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 55312 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )