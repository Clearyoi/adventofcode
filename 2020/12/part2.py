def rotateWaypoint( wayX, wayY, val):
	angle = val % 360
	if angle == 90:
		tmp = wayX
		wayX = wayY
		wayY = -tmp
	if angle == 180:
		wayX = -wayX
		wayY = -wayY
	if angle == 270:
		tmp = wayX
		wayX = -wayY
		wayY = tmp
	return wayX, wayY

def computeDistance( instructions ):
	x, y = 0, 0
	wayX, wayY = 10, 1
	for instruction in instructions:
		op = instruction[0]
		val = int( instruction[1:] )
		if op == 'N':
			wayY += val
		if op == 'S':
			wayY -= val
		if op == 'E':
			wayX += val
		if op == 'W':
			wayX -= val
		if op == 'R':
			wayX, wayY = rotateWaypoint( wayX, wayY, val )
		if op == 'L':
			wayX, wayY = rotateWaypoint( wayX, wayY, -val )
		if op == 'F':
			x += wayX * val
			y += wayY * val
	return abs( y ) + abs( x )

instructions = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
print( computeDistance( instructions ) )