def simulateRound( grid ):
	newGrid = [[] for x in range( len( grid ) ) ]
	for i, row in enumerate( grid ):
		for j, val in enumerate( row ):
			if val == ".":
				newGrid[i].append( "." )
				continue
			seats = countNearbySeats(grid, i, j)
			if val == "L":
				if seats == 0:
					newGrid[i].append( "#" )
					continue
				newGrid[i].append( "L" )
				continue
			if val == "#":
				if seats >= 4:
					newGrid[i].append( "L" )
					continue
				newGrid[i].append( "#" )
				continue
	if newGrid == grid:
		return newGrid, True
	return newGrid, False

def countNearbySeats( grid, iVal, jVal ):
	count = 0
	for i in range( iVal - 1, iVal + 2 ):
		for j in range( jVal - 1, jVal + 2):
			if ( i >= 0 and i < len( grid ) and
			   j >= 0 and j < len( grid[0] ) and not
			   ( i == iVal and j == jVal ) ):
				if grid[i][j] == "#":
					count += 1
	return count


def findStable( grid ):
	while True:
		grid, stable = simulateRound( grid )
		if stable:
			return countOccupiedSeats( grid )

def countOccupiedSeats( grid ):
	return  sum( [ len( [  x for x in row if x == "#" ] ) for row in grid ] )


grid = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print( findStable( grid ) )