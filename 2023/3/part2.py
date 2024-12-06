import re

def getResult( lines ):
	result = 0
	maxLines = len(lines)
	for i, line in enumerate(lines):
		lineLen = len(line)
		for j, symbol in enumerate(line):
			if symbol == '*':
				continue
			for k in (-1,0,1):
				for l in (-1,0,1):
					if i+k < 0 or j+l < 0 or i+k >= maxLines or j+l >= lineLen:
						print(f'not checking pos[{i+k}, {j+l}] i:{i} j:{j} k{k}')
						continue
					if not lines[i+k][j+l].isnumeric():
						continue
					parseNum(i+k, j+l)

		
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 467835 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
