import re

def printMap(robots, width, height):
	row = [0]*width
	rows =[]
	for h in range(height):
		rows.append(row.copy())
	for r in robots:
		rows[r[1]][r[0]] += 1
	for rw in rows:
		print(rw)

def processRobots(robots, width, height):
	for i,robot in enumerate(robots):
		newX = ( robot[0] + robot[2] ) % width
		newY = ( robot[1] + robot[3] ) % height
		robots[i] = (newX, newY, robot[2], robot[3])

def countRobots(robots, width, height):
	counts = [0,0,0,0]
	for robot in robots:
		if robot[0] < width//2:
			if robot[1] < height//2:
				counts[0] += 1
			elif robot[1] > height//2:
				counts[1] += 1
		elif robot[0] > width//2:
			if robot[1] < height//2:
				counts[2] += 1
			elif robot[1] > height//2:
				counts[3] += 1
	total = 1
	for c in counts:
		total *= c
	return total

def getResult( lines, width, height ):
	total = 0
	robots = []
	for line in lines:
		m = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)',line)
		x,y,dx,dy = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
		robots.append((x,y,dx,dy))
	for i in range(100):
		processRobots(robots, width, height)
	total = countRobots(robots, width, height)
	return total

def readData( filename ):
	return [x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, width, height, expected ):
	result = getResult( testData, width, height )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 11, 7, 12 ):
	print( getResult( readData( "input.txt" ), 101,103 ) )
	print( "Done" )