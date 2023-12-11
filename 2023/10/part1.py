def move(rows, curr, direction):
	north = ((curr[0]-1, curr[1]), 'north')
	south = ((curr[0]+1, curr[1]), 'south')
	west = ((curr[0], curr[1]-1), 'west')
	east = ((curr[0], curr[1]+1), 'east')
	symbol = rows[curr[0]][curr[1]]
	if direction == 'north':
		if symbol == '|':
			return north
		if symbol == '7':
			return west
		if symbol == 'F':
			return east

	if direction == 'south':
		if symbol == '|':
			return south
		if symbol == 'J':
			return west
		if symbol == 'L':
			return east

	if direction == 'east':
		if symbol == 'J':
			return north
		if symbol == '7':
			return south
		if symbol == '-':
			return east

	if direction == 'west':
		if symbol == 'L':
			return north
		if symbol == 'F':
			return south
		if symbol == '-':
			return west
	print(f'BAD symbol: {symbol}')

def traverse(rows, start, firstStep, direction):
	curr = firstStep
	steps = 1
	while curr != start:
		curr, direction = move(rows, curr, direction)
		steps += 1
	return steps

def findStart(rows):
	for i, row in enumerate(rows):
		for j, cell in enumerate(row):
			if cell == 'S':
				start = (i,j)
				if rows[i][j+1] in ['-','J','7']:
					firstStep = (i,j+1)
					direction = 'east'
				elif rows[i][j-1] in ['-','L','F']:
					firstStep = (i,j-1)
					direction = 'west'
				elif rows[i+1][j] in ['|','L','J']:
					firstStep = (i+1,j)
					direction = 'south'
				break
	return start, firstStep, direction

def getResult( rows ):
	start, firstStep, direction = findStart(rows)
	return traverse(rows, start, firstStep, direction)/2

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 4 ):
	if runTest( readData( "input2.tst" ), 8 ):
		print( getResult( readData( "input.txt" ) ) )
		print( "Done" )
