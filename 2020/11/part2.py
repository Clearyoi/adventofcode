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
				if seats >= 5:
					newGrid[i].append( "L" )
					continue
				newGrid[i].append( "#" )
				continue
	if newGrid == grid:
		return newGrid, True
	return newGrid, False

def countNearbySeats( grid, iVal, jVal ):
	count = 0
	# Up check
	i = iVal - 1
	while i >= 0:
		if grid[i][jVal] == "#":
			count += 1
			break
		if grid[i][jVal] == "L":
			break
		i -= 1

	# Down check
	i = iVal + 1
	while i < len( grid ):
		if grid[i][jVal] == "#":
			count += 1
			break
		if grid[i][jVal] == "L":
			break
		i += 1

	# Left check
	j = jVal - 1
	while j >= 0:
		if grid[iVal][j] == "#":
			count += 1
			break
		if grid[iVal][j] == "L":
			break
		j -= 1

	# Right check
	j = jVal + 1
	while j < len( grid[0] ):
		if grid[iVal][j] == "#":
			count += 1
			break
		if grid[iVal][j] == "L":
			break
		j += 1

	# Down right check
	i, j = iVal+1, jVal+1
	while i < len( grid ) and j < len( grid[0] ):
		if grid[i][j] == "#":
			count += 1
			break
		if grid[i][j] == "L":
			break
		i += 1
		j += 1

	# Up right check
	i, j = iVal-1, jVal+1
	while i >= 0 and j < len( grid[0] ):
		if grid[i][j] == "#":
			count += 1
			break
		if grid[i][j] == "L":
			break
		i -= 1
		j += 1
	
	# Down left check
	i, j = iVal+1, jVal-1
	while i < len( grid ) and j >= 0:
		if grid[i][j] == "#":
			count += 1
			break
		if grid[i][j] == "L":
			break
		i += 1
		j -= 1

	# Up Left check
	i, j = iVal-1, jVal-1
	while i >= 0 and j >= 0:
		if grid[i][j] == "#":
			count += 1
			break
		if grid[i][j] == "L":
			break
		i -= 1
		j -= 1
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