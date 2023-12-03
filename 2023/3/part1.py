import re

def getResult( lines ):
	result = 0
	maxLines = len(lines)
	for i, line in enumerate(lines):
		lineLen = len(line)
		for j, symbol in enumerate(line):
			if not symbol.isnumeric():
				continue
			if j != 0 and line[j-1].isnumeric():
				continue
			val = re.search(r'\d*', line[j:]).group()
			print(f'val {val}')
			matched = False
			for k in (-1,0,1):
				if matched:
					break
				for l in range(-1,len(val)+1):
					if i+k < 0 or j+l < 0 or i+k >= maxLines or j+l >= lineLen:
						print(f'not checking pos[{i+k}, {j+l}] i:{i} j:{j} k{k}')
						continue
					if lines[i+k][j+l] != '.' and not lines[i+k][j+l].isnumeric():
						print(f'Found pos[{i+k}, {j+l}] <<{lines[i+k][j+l]}>> i:{i} j:{j} k{k}')
						print(f'adding {val}')
						result += int(val)
						matched = True
						break
					print(f'checking pos[{i+k}, {j+l}] <<{lines[i+k][j+l]}>> i:{i} j:{j} k{k}')

		
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 4361 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
