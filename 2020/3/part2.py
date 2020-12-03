def countTreeHits( layout, startPos, slope ):
	height = len( layout )
	width = len( layout[0] )
	currentPos = startPos
	hits = 0
	for i in range( startPos[0], height, slope[1]):
		if layout[currentPos[1]][currentPos[0] % width] == '#':
			hits += 1
		currentPos = currentPos[0] + slope[0], currentPos[1] + slope[1]
	return hits

def countAllSlopes( layout ):
	total = 1
	slopesToCheck = [
	( 1, 1 ),
	( 3, 1 ),
	( 5, 1 ),
	( 7, 1 ),
	( 1, 2 ),
	]
	for slope in slopesToCheck:
		total *= countTreeHits( layout, ( 0, 0 ), slope )
	return total

layout = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print("Answer: {}".format( countAllSlopes( layout ) ) )
