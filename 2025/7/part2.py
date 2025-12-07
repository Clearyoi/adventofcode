def getResult( lines ):
	total = 0
	for i, line in enumerate(lines[:-1]):
		for j, v in enumerate(line):
			if v != "." and v != "^":
				if lines[i+1][j] == "^":
					if lines[i+1][j-1] == ".":
						lines[i+1][j-1] = v
					else:
						lines[i+1][j-1] = str(int(lines[i+1][j-1]) + int(v))
					if lines[i+1][j+1] == ".":
						lines[i+1][j+1] = v
					else:
						lines[i+1][j+1] = str(int(v) + int(v))
				else:
					if lines[i+1][j] == ".":
						lines[i+1][j] = v
					else:
						lines[i+1][j] = str(int(v)+int(lines[i+1][j]))
	total = sum([int(x) for x in lines[-1] if x != "." and x != "^"])
	return total

def readData( filename ):
	return [ list(x) for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 40 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )