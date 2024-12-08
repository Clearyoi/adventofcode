import math
from collections import defaultdict
def isValid(man, rules):
	for i,m in enumerate(man):
		if m in rules:
			for r in rules[m]:
				if r in man[i:]:
					return False
	return True

	

def middle(manual):
	return int(manual[math.floor(len(manual)/2)])

def getResult( lines ):
	total = 0
	rulesLines = lines[0]
	rules = defaultdict(list)
	for r in rulesLines:
		vals = r.split('|')
		rules[int(vals[1])].append(int(vals[0]))
	manuals = lines[1]
	for manual in manuals:
		man = [int(x) for x in manual.split(',')]
		if isValid(man, rules):
			total += middle(man)
	return total

def readData( filename ):
	return [ [x for x in y.split('\n') ] for y in open( filename ).read().strip().split( '\n\n' ) ]

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expected {expected} got {result}")
	return False

if runTest( readData( "input.tst" ), 143 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )