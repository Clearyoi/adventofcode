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
	steps = 75
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
	# No sample given
	return True

if runTest( readData( "input.tst" ), 0 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )