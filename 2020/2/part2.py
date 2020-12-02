def validPass( pw, key, pos1, pos2 ):
	valid = False
	if pw[pos1 - 1] == key:
		valid = not valid
	if pw[pos2 - 1] == key:
		valid = not valid
	return valid
	

def parseLine( line ):
	policy, pw = line.split( ':' )
	minMax, key = policy.split( ' ' )
	pos1, pos2 = minMax.split( '-' )
	return pw.strip(), key, int( pos1 ), int( pos2 )

def countValid( lines ):
	valid, invalid = 0, 0
	for line in lines:
		pw, key, pos1, pos2 = parseLine ( line )
		if validPass( pw, key, pos1, pos2 ):
			valid += 1
		else:
			invalid += 1
	return valid, invalid

lines = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
valid, invalid = countValid( lines )
print( 'Valid: {}\nInvalid: {}'.format( valid, invalid ) )