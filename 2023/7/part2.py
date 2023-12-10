import re
from functools import cmp_to_key

def rank(hand):
	unique = set(re.sub('J','',hand))
	if not unique:
		return 8
	result = 10 - ( 2 * len(unique))
	if result == 6:
		for l in unique:
			if re.search(r'(.)\1{3}', ''.join(sorted(re.sub('J', l, hand)))):
				return 7
	if result == 4:
		for l in unique:
			if re.search(r'(.)\1{2}', ''.join(sorted(re.sub('J', l, hand)))):
				return 5
	return result

def compareHands(hand1, hand2):
	rank1 = rank(hand1)
	rank2 = rank(hand2)
	if rank1 < rank2:
		return -1
	if rank1 > rank2:
		return 1
	hand1Replaced = re.sub('A','Z', re.sub('K','Y', re.sub('Q','X', re.sub('J','0', hand1))))
	hand2Replaced = re.sub('A','Z', re.sub('K','Y', re.sub('Q','X', re.sub('J','0', hand2))))
	for i, card in enumerate(hand1Replaced):
		if card < hand2Replaced[i]:
			return -1
		if card > hand2Replaced[i]:
			return 1
	return 0

def getResult( lines ):
	result = 0
	hands = {}
	for line in lines:
		hands[line.split()[0]] = line.split()[1]
	for i, val in enumerate(sorted(hands.keys(), key=cmp_to_key(compareHands))):
		result += (i+1) * int(hands[val])
	return result

def runTest( testData, expected ):
	result = getResult( testData )
	if expected == result:
		return True
	print(f"Test failed, expcted {expected} got {result}")
	return False
	
def readData( filename ):
	return [ x for x in open( filename ).read().strip().split( '\n' ) ]

if runTest( readData( "input.tst" ), 5905 ):
	print( getResult( readData( "input.txt" ) ) )
	print( "Done" )
