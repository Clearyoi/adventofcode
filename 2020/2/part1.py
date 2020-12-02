def validPass( pw, key, minO, maxO ):
	count = 0
	for letter in pw:
		if letter == key:
			count += 1
	if count < minO or count > maxO:
		return False
	return True

def parseLine( line ):
	policy, pw = line.split( ':' )
	minMax, key = policy.split( ' ' )
	minO, maxO = minMax.split( '-' )
	return pw.strip(), key, int( minO ), int( maxO )

def countValid( lines ):
	valid, invalid = 0, 0
	for line in lines:
		pw, key, minO, maxO = parseLine ( line )
		if validPass( pw, key, minO, maxO ):
			valid += 1
		else:
			invalid += 1
	return valid, invalid

lines = [ x for x in open( "input.txt" ).read().strip().split( '\n' ) ]
valid, invalid = countValid( lines )
print( 'Valid: {}\nInvalid: {}'.format( valid, invalid ) )