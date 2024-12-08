import re

def isX(diag1,diag2):
	if re.match(r"MAS|SAM", diag1):
		if re.match(r"MAS|SAM", diag2):
			return 1
	return 0

def getResult( lines ):
	total = 0
	for i, line in enumerate(lines[:-1]):
		if i == 0:
			continue
		for j, ch in enumerate(line[:-1]):
			if j == 0:
				continue
			if ch == 'A':
				diag1 = lines[i-1][j-1] + 'A' + lines[i+1][j+1]
				diag2 = lines[i-1][j+1] + 'A' + lines[i+1][j-1]
				total += isX(diag1, diag2)
	return total

def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 9 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )