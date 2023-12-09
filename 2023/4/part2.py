import re

def calculateScore(card, cards):
	val = cards[card]
	if type(val) == int:
		return val
	if type(val) == list:
		total = sum([calculateScore(x, cards) for x in val])
		cards[card] = total + 1
		return total

def getResult( lines ):
	result = 0
	cards = {}
	for i, line in enumerate(lines):
		wins = set([int(x) for x in line.split(':')[1].split('|')[0].strip().split()])
		have = set([int(x) for x in line.split(':')[1].split('|')[1].strip().split()])
		matches = wins.intersection(have)
		if len(matches) > 0:
			cards[i] = [x+i+1 for x in range(len(matches))]
		else:
			cards[i] = 1
	for card in sorted(cards.keys(), reverse=True):
		calculateScore(card, cards)
	print(cards)
	return sum(cards.values()) 

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 30 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
