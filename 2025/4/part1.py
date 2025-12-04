def getResult( lines ):
	total = 0
	height = len(lines)
	width = len(lines[0])
	for i in range(height):
		for j in range(width):
			if lines[i][j] != '@':
				continue
			count = 0
			for xOffset in range(3):
				for yOffset in range(3):
					x = i+xOffset-1
					y = j+yOffset-1
					if x >= 0 and y >= 0 and x < height and y < width and lines[x][y] == '@':
						count += 1
			if count < 5:
				total += 1
				continue
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 13 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )