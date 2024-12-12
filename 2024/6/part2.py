def walk(floorplan, visited, pos, direction):
	visited.add((pos, direction))
	match direction:
		case 'UP':
			if pos[0] == 0:
				return visited, pos, 'ESCAPED'
			nxt = (pos[0]-1,pos[1])
			if floorplan[nxt[0]][nxt[1]] == '#':
				return visited, pos, 'RIGHT'
		case 'DOWN':
			if pos[0] == len(floorplan)-1:
				return visited, pos, 'ESCAPED'
			nxt = (pos[0]+1,pos[1])
			if floorplan[nxt[0]][nxt[1]] == '#':
				return visited, pos, 'LEFT'
		case 'LEFT':
			if pos[1] == 0:
				return visited, pos, 'ESCAPED'
			nxt = (pos[0],pos[1]-1)
			if floorplan[nxt[0]][nxt[1]] == '#':
				return visited, pos, 'UP'
		case 'RIGHT':
			if pos[1] == len(floorplan[0])-1:
				return visited, pos, 'ESCAPED'
			nxt = (pos[0],pos[1]+1)
			if floorplan[nxt[0]][nxt[1]] == '#':
				return visited, pos, 'DOWN'
	return visited, nxt, direction


def isLooped(floorplan, start, direction):
	curr = start
	visited = set()
	for i in range(1,10000):
		visited, curr, direction = walk(floorplan, visited, curr, direction)
		if direction == 'ESCAPED':
			return False
		if (curr, direction) in visited:
			return True
	print('oops')
	return False

def getResult( lines ):
	# Out by 1 on my input. Works on other people inputs
	total = 0
	start = (0,0)
	for i, line in enumerate(lines):
		for j, ch in enumerate(line):
			if ch == '^':
				start = (i,j)
	for i, line in enumerate(lines):
		for j, ch in enumerate(line):
			if i == start[0] and j == start[0] or ch == '#':
				continue
			newFp = lines.copy()
			l = list(newFp[i])
			l[j] = '#'
			newFp[i] = ''.join(l)
			if isLooped(newFp, start, 'UP'):
				total += 1
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 6 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )