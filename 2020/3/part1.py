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

layout = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print("Number of trees hit: {}".format( countTreeHits( layout, ( 0, 0 ), ( 3, 1 ) ) ) )
