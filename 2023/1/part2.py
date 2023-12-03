words = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 
'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

def getResult( lines ):
	result = 0
	for line in lines:
		firstDigit = 0
		for i, symbol in enumerate(line):
			if symbol.isnumeric():
				lastDigit = symbol
				if not firstDigit:
					firstDigit = symbol
			for word in words:
				if line[i:].startswith(word):
					lastDigit = words[word]
					if not firstDigit:
						firstDigit = words[word]

		result += int(firstDigit + lastDigit)
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input2.tst" ), 281 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
