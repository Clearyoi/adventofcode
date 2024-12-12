def walk(floorplan, visited, pos, direction):
	#Longer than it should be I misread the question
	match direction:
		case 'UP':
			if pos[0] == 0:
				return visited, pos, 'RIGHT', True
			nxt = (pos[0]-1,pos[1])
			if floorplan[nxt[0]][nxt[1]] == '#':
				return visited, pos, 'RIGHT', False
			visited.add(nxt)
			return visited, nxt, 'UP', False
		case 'DOWN':
			if pos[0] == len(floorplan)-1:
				return visited, pos, 'LEFT', True
			nxt = (pos[0]+1,pos[1])
			if floorplan[nxt[0]][nxt[1]] == '#':
				return visited, pos, 'LEFT', False
			visited.add(nxt)
			return visited, nxt, 'DOWN', False
		case 'LEFT':
			if pos[1] == 0:
				return visited, pos, 'UP', True
			nxt = (pos[0],pos[1]-1)
			if floorplan[nxt[0]][nxt[1]] == '#':
				return visited, pos, 'UP', False
			visited.add(nxt)
			return visited, nxt, 'LEFT', False
		case 'RIGHT':
			if pos[1] == len(floorplan[0])-1:
				return visited, pos, 'DOWN', True
			nxt = (pos[0],pos[1]+1)
			if floorplan[nxt[0]][nxt[1]] == '#':
				return visited, pos, 'DOWN', False
			visited.add(nxt)
			return visited, nxt, 'RIGHT', False


def getResult( lines ):
	# checked by hand
	direction = 'UP'
	visited = set()
	curr, start = (0,0), (0,0)
	for i, line in enumerate(lines):
		for j, ch in enumerate(line):
			if ch == '^':
				start = (i,j)
				curr = start
	while True:
		visited, curr, direction, done = walk(lines, visited, curr, direction)
		if done:
			return len(visited)

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 41 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )