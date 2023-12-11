def moveAndReplace(rows, curr, direction, mainPipe):
	i, j = curr
	maxRow = len(rows)-1
	maxCol = len(rows[0])-1
	north = ((i-1, j), 'north')
	south = ((i+1, j), 'south')
	west = ((i, j-1), 'west')
	east = ((i, j+1), 'east')
	symbol = rows[i][j]
	if direction == 'north':
		if symbol == '|':
			rows[i][j] = '$'
			if j < maxCol and (i,j+1) not in mainPipe:
				rows[i][j+1] = '1'
			if j > 0 and (i,j-1) not in mainPipe:
				rows[i][j-1] = '2'
			return north
		if symbol == '7':
			rows[i][j] = '$'
			if j < maxCol and (i,j+1) not in mainPipe:
				rows[i][j+1] = '1'
			if i > 0 and (i-1,j) not in mainPipe:
				rows[i-1][j] = '1'
			return west
		if symbol == 'F':
			rows[i][j] = '$'
			if j > 0 and (i,j-1) not in mainPipe:
				rows[i][j-1] = '2'
			if i > 0 and (i-1,j) not in mainPipe:
				rows[i-1][j] = '2'
			return east

	if direction == 'south':
		if symbol == '|':
			rows[i][j] = '$'
			if j < maxCol and (i,j+1) not in mainPipe:
				rows[i][j+1] = '2'
			if j > 0 and (i,j-1) not in mainPipe:
				rows[i][j-1] = '1'
			return south
		if symbol == 'J':
			rows[i][j] = '$'
			if j < maxCol and (i,j+1) not in mainPipe:
				rows[i][j+1] = '2'
			if i < maxRow and (i+1,j) not in mainPipe:
				rows[i+1][j] = '2'
			return west
		if symbol == 'L':
			rows[i][j] = '$'
			if j > 0 and (i,j-1) not in mainPipe:
				rows[i][j-1] = '1'
			if i < maxRow and (i+1,j) not in mainPipe:
				rows[i+1][j] = '1'
			return east

	if direction == 'east':
		if symbol == 'J':
			rows[i][j] = '$'
			if j < maxCol and (i,j+1) not in mainPipe:
				rows[i][j+1] = '1'
			if i > 0 and (i-1,j) not in mainPipe:
				rows[i-1][j] = '1'
			return north
		if symbol == '7':
			rows[i][j] = '$'
			if j < maxCol and (i,j+1) not in mainPipe:
				rows[i][j+1] = '2'
			if i > 0 and (i-1,j) not in mainPipe:	
				rows[i-1][j] = '2'
			return south
		if symbol == '-':
			rows[i][j] = '$'
			if i < maxRow and (i+1,j) not in mainPipe:
				rows[i+1][j] = '1'
			if i > 0 and (i-1,j) not in mainPipe:
				rows[i-1][j] = '2'
			return east

	if direction == 'west':
		if symbol == 'L':
			rows[i][j] = '$'
			if j > 0 and (i,j-1) not in mainPipe:
				rows[i][j-1] = '2'
			if i < maxRow and (i+1,j) not in mainPipe:
				rows[i+1][j] = '2'
			return north
		if symbol == 'F':
			rows[i][j] = '$'
			if j > 0 and (i,j-1) not in mainPipe:
				rows[i][j-1] = '1'
			if i < maxRow and (i+1,j) not in mainPipe:
				rows[i+1][j] = '1'
			return south
		if symbol == '-':
			rows[i][j] = '$'
			if i < maxRow and (i+1,j) not in mainPipe:
				rows[i+1][j] = '2'
			if i > 0 and (i-1,j) not in mainPipe:
				rows[i-1][j] = '1'
			return west
	print(f'BAD symbol: {symbol}')

def move(rows, curr, direction):
	i, j = curr
	maxRow = len(rows)
	maxCol = len(rows[0])
	north = ((i-1, j), 'north')
	south = ((i+1, j), 'south')
	west = ((i, j-1), 'west')
	east = ((i, j+1), 'east')
	symbol = rows[i][j]
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

def traverse(rows, start, firstStep, startDirection):
	curr = firstStep
	direction = startDirection
	mainPipe = [curr]
	# first find the pipe
	while curr != start:
		curr, direction = move(rows, curr, direction)
		mainPipe.append(curr)
	# now we replace
	curr = firstStep
	direction = startDirection
	rows[start[0]][start[1]] = '$'
	while curr != start:
		curr, direction = moveAndReplace(rows, curr, direction, mainPipe)
	return rows

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

def updateCell(rows, i, j):
	if i > 0 and rows[i-1][j] in ['1','2']:
		return rows[i-1][j]
	if i < len(rows)-1 and rows[i+1][j] in ['1','2']:
		return rows[i+1][j]
	if j > 0 and rows[i][j-1] in ['1','2']:
		return rows[i][j-1]
	if j < len(rows[0])-1 and rows[i][j+1] in ['1','2']:
		return rows[i][j+1]
	return rows[i][j]

def updateRows(rows):
	updated = True
	while updated:
		updated = False
		for i,row in enumerate(rows):
			for j,cell in enumerate(row):
				if cell not in ['1','2','$']:
					rows[i][j] = updateCell(rows, i, j)
					updated = True
	return rows

def countInternal(rows):
	for cell in rows[0]:
		if cell != '$':
			outside = cell
			break
	count = 0
	inside = '1'
	if outside == '1':
		inside = '2'
	for row in rows:
		for cell in row:
			if cell == inside:
				count += 1
	return count


def getResult( rows ):
	start, firstStep, direction = findStart(rows)
	rows = traverse(rows, start, firstStep, direction)
	rows = updateRows(rows)
	return countInternal(rows)

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False
	
def readData( filename ):
	return [ list(x) for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input3.tst" ), 4 ):
	if runTest( readData( "input4.tst" ), 8 ):
		if runTest( readData( "input5.tst" ), 10 ):
			print( getResult( readData( "input.txt" ) ) )
			print( "Done" )
