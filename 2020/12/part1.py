def computeDistance( instructions ):
	x, y = 0, 0
	angle = 90
	for instruction in instructions:
		op = instruction[0]
		val = int( instruction[1:] )
		if op == 'N':
			y += val
		if op == 'S':
			y -= val
		if op == 'E':
			x += val
		if op == 'W':
			x -= val
		if op == 'R':
			angle = ( angle + val ) % 360
		if op == 'L':
			angle = ( angle - val ) % 360
		if op == 'F':
			if angle == 0:
				y += val
			if angle == 180:
				y -= val
			if angle == 90:
				x += val
			if angle == 270:
				x -= val
	return abs( y ) + abs( x )

instructions = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print( computeDistance( instructions ) )